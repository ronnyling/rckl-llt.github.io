from PageObjectLibrary import PageObject
from resources.restAPI.Common import TokenAccess
from resources.restAPI import COMMON_KEY
from setup.hanaDB import HanaDB
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet, CustomerOptionGet
from resources.restAPI.Config.TaxMgmt.ServiceMaster import ServiceMasterGet
from resources.restAPI.Config.TaxMgmt.TaxStructure import TaxStructureGet
from resources.restAPI.Config.TaxMgmt.TaxSetting import TaxSettingGet
from resources.restAPI.MasterDataMgmt.PriceGroup import ProductPriceGet
from resources.restAPI.MasterDataMgmt.Product import ProductGet, ProductUomGet
from resources.restAPI.Config.AppSetup import AppSetupGet
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import math, json, urllib3
import datetime
NOW = datetime.datetime.now()
urllib3.disable_warnings()


class TransactionFormula(PageObject):

    PRD_INFO = "${prd_info}"
    APPSETUP_INFO = "${body_result}"
    STORE_ROUNDING = "${store_rounding}"
    INV_DETAILS = "${InvDetails}"
    RTN_DETAILS = "${ReturnDetails}"
    SUPP_INFO = "${supplierinfo}"
    INV_LVL = "${inv_level}"
    PRD_ID = "${prd_id}"

    def validate_stock_movement_after_create_invoice(self):
        product = self.builtin.get_variable_value(self.INV_DETAILS)
        product = product['productUom'].split(":")
        product_qty = product[1]
        inv_lvl = self.builtin.get_variable_value(self.INV_LVL)
        inv_lvl = inv_lvl[0]
        qty_oh_hand = float(inv_lvl[0]) - float(product_qty)
        qty_available = float(inv_lvl[1]) - float(product_qty)
        wh = self.builtin.get_variable_value("${wh_id}")
        prd = self.builtin.get_variable_value(self.PRD_ID)
        self.get_current_inventory(wh, prd)
        current_inv_lvl = self.builtin.get_variable_value(self.INV_LVL)
        current_inv_lvl = current_inv_lvl[0]
        assert float(current_inv_lvl[0]) == qty_oh_hand , "QTY ON HAND Stock Movement NOT MATCH"
        assert float(current_inv_lvl[1]) == qty_available, "AVAILABLE QTY Stock Movement NOT MATCH"

    def get_current_inventory(self, wh_id, prod_id):
        wh_id = COMMON_KEY.convert_id_to_string(wh_id)
        prod_id = COMMON_KEY.convert_id_to_string(prod_id)
        query = "select CAST(ON_HAND_QTY as VARCHAR),CAST(AVAILABLE_QTY as VARCHAR)," \
                "CAST(ALLOCATE_QTY as VARCHAR)  from INVT_MASTER WHERE " \
                "WHS_ID='{0}' AND PRD_ID='{1}'".format(wh_id, prod_id)
        HanaDB.HanaDB().connect_database_to_environment()
        result = HanaDB.HanaDB().fetch_all_record(query)
        HanaDB.HanaDB().disconnect_from_database()
        self.builtin.set_test_variable(self.INV_LVL, result)
        self.builtin.set_test_variable("${wh_id}", wh_id)
        self.builtin.set_test_variable(self.PRD_ID, prod_id)
        return result

    def get_current_inventory_temp(self, wh_id, prod_id):
        wh_id = COMMON_KEY.convert_id_to_string(wh_id)
        prod_id = COMMON_KEY.convert_id_to_string(prod_id)
        query = "select CAST(QTY as VARCHAR) from INVT_TEMP WHERE TXN_TYPE ='COMPANY_INVOICE' " \
                "AND WHS_ID='{0}' AND PRD_ID='{1}' ORDER BY TXN_DATE DESC".format(wh_id, prod_id)
        HanaDB.HanaDB().connect_database_to_environment()
        result = HanaDB.HanaDB().fetch_all_record(query)
        HanaDB.HanaDB().disconnect_from_database()
        return result

    def get_current_inventory_master_history(self, wh_id, prod_id):
        today_date = str((NOW + datetime.timedelta(days=0)).strftime("%Y-%m-%d"))
        wh_id = COMMON_KEY.convert_id_to_string(wh_id)
        prod_id = COMMON_KEY.convert_id_to_string(prod_id)
        query = "select CAST(STKRCP_QTY as VARCHAR),CAST(CLOSEBAL as VARCHAR)" \
                " from INVT_MASTERHIS WHERE INVT_DATE like '%{0}%' " \
                "AND WHS_ID='{1}' AND PRD_ID='{2}'".format(today_date, wh_id, prod_id)
        HanaDB.HanaDB().connect_database_to_environment()
        result = HanaDB.HanaDB().fetch_all_record(query)
        HanaDB.HanaDB().disconnect_from_database()
        return result

    @keyword("Calculate Gross and Cust Discount Amount")
    def tran_calculation_for_gross_and_cust_disc(self, prime_flag, cust_name, cust_disc_method, prd_info):
        TokenAccess.TokenAccess().user_retrieves_token_access_as('hqadm')
        TokenAccess.TokenAccess().get_token_by_role('distadm')
        cust = CustomerGet.CustomerGet().user_retrieves_cust_name(cust_name)
        BuiltIn().set_test_variable("${cust_disc}", cust['CUST_DISC'])
        BuiltIn().set_test_variable("${cust_id}", cust['ID'])
        cust_opt = CustomerOptionGet.CustomerOptionGet().user_retrieves_cust_option()
        if prime_flag.upper() == 'PRIME':
            price_group_id = cust['PRICE_GRP']
        else:
            price_group_id = cust_opt['NON_PRIME_PRICE_GRP']
        prd_info = self.get_unit_price_and_default_uom(price_group_id, prd_info)
        prd_info = self.calculate_gross_and_cust_disc(prd_info, cust_disc_method)
        BuiltIn().set_test_variable(self.PRD_INFO, prd_info)
        BuiltIn().set_test_variable("${cust_info}", cust)
        return prd_info

    def calculate_posm_prd_net(self, prd):
        prd = prd.split(":")
        dist_other_pg_id = BuiltIn().get_variable_value("${dist_other_pg}")
        unit_price = ProductPriceGet.ProductPriceGet().get_prd_price(dist_other_pg_id, prd[0])
        unit_price = float(unit_price['SELLING_PRC'])
        return unit_price

    @keyword("Calculate Product Tax Amount")
    def tax_calculation_for_multi_product(self):
        prd_info = BuiltIn().get_variable_value(self.PRD_INFO)
        print("CALCULATE TAX")
        cust = BuiltIn().get_variable_value("${cust_info}")
        count = 0
        for item in prd_info:
            prd_res_body = ProductGet.ProductGet().user_retrieves_prd_by_prd_code(item['PRD_CODE'])
            prd_info[count] = self.calculate_tax_for_single_prd(item, cust['CUST_TAX_GRP'], prd_res_body['PRD_TAX_GRP'])
            count = count + 1
        BuiltIn().set_test_variable(self.PRD_INFO, prd_info)

    def get_app_setup_store_rounding(self):
        AppSetupGet.AppSetupGet().user_retrieves_details_of_application_setup()
        body_result = BuiltIn().get_variable_value(self.APPSETUP_INFO)
        store_rounding = int(body_result['ROUND_OFF_DECIMAL']['ROUND_OFF_DECIMAL'])
        display_rounding = int(body_result['ROUND_OFF_DECIMAL_DISPLAY']['ROUND_OFF_DECIMAL_DISPLAY'])
        BuiltIn().set_test_variable(self.STORE_ROUNDING, store_rounding)
        BuiltIn().set_test_variable('${display_rounding}', display_rounding)

    def company_tax_calculation_for_multi_product(self):
        self.get_app_setup_store_rounding()
        prd_info = BuiltIn().get_variable_value(self.PRD_INFO)
        supplier = BuiltIn().get_variable_value(self.SUPP_INFO)
        count = 0
        for item in prd_info:
            prd_res_body = ProductGet.ProductGet().user_retrieves_prd_by_prd_code(item['PRD_CODE'])

            prd_info[count] = self.calculate_tax_for_single_prd(item, supplier['TAX_GROUP'], prd_res_body['PRD_TAX_GRP'])
            count = count + 1
        prd_info = BuiltIn().get_variable_value(self.PRD_INFO)
        print("prd_info",prd_info)

    def all_tax_info_payload(self, tax_cd, tax_rate, tax_amt):
        payload = {
            "TAX_CD": tax_cd,
            "TAX_RATE": tax_rate,
            "TAX_AMT": tax_amt
        }
        return payload

    def non_product_accumulative_tax(self, prev_lvl_tax, item, tax_setting,
                                     gross, count, total, num, store_rounding, all_level_tax_details):
        if prev_lvl_tax != 0:
            gross = float(gross) + prev_lvl_tax
        else:
            gross = item['AMT']
        for _ in range(count):
            num = num - 1
            tax_sett_info = tax_setting[num]
            tax_rate = tax_sett_info['TAX_RATE']
            if prev_lvl_tax != 0:
                gross = float(gross) + prev_lvl_tax
            tax_amt = float(gross) * float(tax_rate) / 100
            prev_lvl_tax = tax_amt
            tax_amt = round(tax_amt, store_rounding)
            total += tax_amt
            tax_cd = tax_sett_info['TAX_CD']
            all_tax_info = self.all_tax_info_payload(tax_cd, float(tax_rate), float(tax_amt))
            all_level_tax_details.append(all_tax_info)
            item['TAX_AMT'] = round(total, store_rounding)
        return all_level_tax_details

    def loop_tax_apply_on_and_calculate_tax(self, apply_on, tax_rate, item, all_level_tax_details, prev_lvl_tax):
        for apply_on_item in apply_on:
            if apply_on_item == 'Net' or apply_on_item == 'Gross':
                tax_amt = float(item['AMT']) * float(tax_rate) / 100
            else:
                for prev_tax in all_level_tax_details:
                    if apply_on_item == prev_tax['TAX_CD']:
                        tax_amt = prev_tax['TAX_AMT'] * tax_rate / 100
                        prev_lvl_tax = tax_amt

        return tax_amt, prev_lvl_tax

    def non_product_non_accumulative_tax(self, prev_lvl_tax, item, tax_setting,
                                     gross, count, num, total, store_rounding, all_level_tax_details):
        for _ in range(count):
            num = num - 1
            tax_sett_info = tax_setting[num]
            tax_rate = float(tax_sett_info['TAX_RATE'])
            tax_amt = float(item['AMT']) * float(tax_rate) / 100
            tax_amt = round(tax_amt, store_rounding)
            apply_on = tax_sett_info['APPLY_ON']
            if prev_lvl_tax != 0:
                gross = float(gross) + prev_lvl_tax
            for apply_on_item in apply_on:
                if apply_on_item == 'Net' or apply_on_item == 'Gross':
                    tax_amt = float(item['AMT']) * float(tax_rate) / 100
                else:
                    tax_amt, prev_lvl_tax = self.loop_tax_apply_on_and_calculate_tax(apply_on, tax_rate, item, all_level_tax_details, prev_lvl_tax)
            tax_cd = tax_sett_info['TAX_CD']
            total += tax_amt
            all_tax_info = self.all_tax_info_payload(tax_cd, float(tax_rate), float(tax_amt))
            all_level_tax_details.append(all_tax_info)
            item['TAX_AMT'] = round(total, store_rounding)
        return all_level_tax_details

    def company_tax_calculation_for_non_product_service(self):
        all_level_tax_details = []
        self.get_app_setup_store_rounding()
        service_info = BuiltIn().get_variable_value("${service_info}")
        supplier = BuiltIn().get_variable_value(self.SUPP_INFO)
        self.get_app_setup_store_rounding()
        store_rounding = BuiltIn().get_variable_value(self.STORE_ROUNDING)
        for item in service_info:
            prev_lvl_tax = 0
            gross = 0
            svc_tg = ServiceMasterGet.ServiceMasterGet().user_get_service_master_by_code(item['SVC_CD'])

            tax_struct = TaxStructureGet.TaxStructureGet().get_tax_structure_by_cust_and_prd_tax_group(supplier['TAX_GROUP'],
                                                                                                       svc_tg['TAX_GROUP_ID'])
            tax_setting = TaxSettingGet.TaxSettingGet().get_tax_sett(tax_struct['ID'])
            count = len(tax_setting)
            num = count
            total = 0
            accumulative = tax_setting[0]['TAX_ACCUMULATIVE']
            if accumulative is True:
                all_level_tax_details = self.non_product_accumulative_tax(prev_lvl_tax, item, tax_setting,
                                                                          gross, count, total, num, store_rounding, all_level_tax_details)

            else:
                all_level_tax_details = self.non_product_non_accumulative_tax(prev_lvl_tax, item, tax_setting,
                                                                          gross, count, num, total, store_rounding, all_level_tax_details)
            item['ALL_LEVEL_TAX'] = all_level_tax_details
        BuiltIn().set_test_variable("${service_info}", service_info)

    def calculate_tax_for_single_prd(self, prd, cust_tax_group, prd_tax_group):
        if cust_tax_group is None or prd_tax_group is None:
            prd['NET_TTL_TAX'] = prd['NET_AMT']
            prd['ALL_LEVEL_TAX'] = 0
            prd['ALL_TAX_DESC'] = 0
            prd['TAXABLE_AMT'] = 0
            prd['TOTAL_TAX'] = 0
        else:
            tax_struct = TaxStructureGet.TaxStructureGet().get_tax_structure_by_cust_and_prd_tax_group(cust_tax_group, prd_tax_group)
            if tax_struct == 0:
                prd['NET_TTL_TAX'] = prd['NET_AMT']
                prd['ALL_LEVEL_TAX'] = 0
                prd['ALL_TAX_DESC'] = 0
                prd['TAXABLE_AMT'] = 0
                prd['TOTAL_TAX'] = 0
            else:
                TAXSETT = TaxSettingGet.TaxSettingGet().get_tax_sett(tax_struct['ID'])
                prd = self.tax_calculation(TAXSETT, prd)
        return prd

    def find_default_uom(self, uom_res_body, prod_details):
        """ Loop product uom response to find out default uom before calculate gross amt"""
        default_sml_uom = 0
        for item in uom_res_body:
            if item['DEFAULT_UOM']:
                default_sml_uom = int(item['CONV_FACTOR_SML'])

        for i in range(len(prod_details["PRD_UOM"])):
            for j in range(len(uom_res_body)):
                if prod_details["PRD_UOM"][i]["UOM"] in uom_res_body[j]["UOM_CD"]:
                    del uom_res_body[j]
                    break
        for i in range(len(uom_res_body)):
            details = {
                "UOM": uom_res_body[i]["UOM_CD"],
                "QTY": "0"
            }
            prod_details["PRD_UOM"].append(details)

        print ("def_uom :", default_sml_uom)
        print ("prod_det:" ,prod_details)
        return default_sml_uom, prod_details

    def get_unit_price_and_default_uom(self, pg_id, prd_info):
        excel_flag = False
        if isinstance(prd_info, str):
            excel_flag = True
            if ";" in prd_info:
                prd_info = prd_info.split(';')
        prd_details = []
        for item in prd_info:
            if excel_flag:
                item = json.loads(item)
            product_code = item['PRD_CODE']

            prd_res_body = ProductGet.ProductGet().user_retrieves_prd_by_prd_code(product_code)
            unit_price = ProductPriceGet.ProductPriceGet().get_prd_price(pg_id, product_code)
            unit_price = float(unit_price['SELLING_PRC'])
            item['UNIT_PRICE'] = unit_price
            all_uom_res_body = ProductUomGet.ProductUomGet().user_retrieves_prd_uom(prd_res_body['ID'])
            default_sml_uom, item = self.find_default_uom(all_uom_res_body, item)
            prd_uom = item['PRD_UOM']
            for uom in prd_uom:
                prd_res_body = ProductGet.ProductGet().user_retrieves_prd_by_prd_code(product_code)
                uom_res_body = ProductUomGet.ProductUomGet().user_retrieves_prd_uom_by_code(prd_res_body['ID'], uom['UOM'])
                uom['UOM_ID'] = uom_res_body['ID']
                uom['CONV_FACTOR'] = uom_res_body['CONV_FACTOR_SML']
                if uom['CONV_FACTOR'] == str(default_sml_uom):
                    item['DEFAULT_UOM'] = uom_res_body['ID']
            item['PRD_ID'] = prd_res_body['ID']
            item['SELLING_IND'] = prd_res_body['SELLING_IND']
            item['DEFAULT_FACTOR'] = default_sml_uom
            prd_details.append(item)
        return prd_details

    def calculate_gross_and_cust_disc(self, prd_info, cust_disc):
        self.get_app_setup_store_rounding()
        store_rounding = BuiltIn().get_variable_value('${store_rounding}')
        grpdisc = BuiltIn().get_variable_value("${res_grpdisc}")
        for prd in prd_info:
            gross_total_all_uom = 0
            smallest_uom = 0
            prd_uom = prd['PRD_UOM']
            for user_input_uom in prd_uom:
                uom_con_factor = int(float(user_input_uom['CONV_FACTOR']))
                uom_list_price = (float(prd['UNIT_PRICE'])/float(prd['DEFAULT_FACTOR'])) * uom_con_factor
                user_input_uom['PRD_LISTPRC_UOM'] = round(uom_list_price, store_rounding)
                uom_gross = user_input_uom['PRD_LISTPRC_UOM'] * float(user_input_uom['QTY'])
                user_input_uom['GROSS_PER_UOM'] = round(uom_gross, store_rounding)
                gross_total_all_uom = gross_total_all_uom + uom_gross
                smallest_uom = smallest_uom + (float(user_input_uom['QTY'])*float(uom_con_factor))
            prd['GROSS_AMT'] = round(gross_total_all_uom, store_rounding)
            prd['BUY_QTY'] = int(smallest_uom)
            prd['GRPDISC_AMT'] = 0
            prd['DISCOUNT'] = None
            prd['GRPDISC_ID'] = None
            if grpdisc is not None:
                self.calculate_cust_disc(prd, store_rounding, gross_total_all_uom)
            if cust_disc == "percent":
                self.calculate_cust_disc(prd, store_rounding, gross_total_all_uom)
            elif cust_disc == "No":
                prd['CUST_DISC'] = 0
                prd['PROMO_DISC'] = 0
            else:
                prd['CUST_DISC'] = round(cust_disc, store_rounding)
            prd['NET_AMT'] = round(prd['GROSS_AMT'] - prd['CUST_DISC'] - prd['PROMO_DISC'] - prd['GRPDISC_AMT'], store_rounding)
        return prd_info

    def calculate_cust_disc(self, prd, store_rounding, gross_total_all_uom):
        disc = BuiltIn().get_variable_value("${cust_disc}")
        promo_disc = BuiltIn().get_variable_value("${promo_disc}")
        prd['CUST_DISC'] = 0
        prd['PROMO_DISC'] = 0
        if disc and promo_disc is not None:
            prd['CUST_DISC_PERC'] = disc
            disc = (float(disc) / 100) * (float(gross_total_all_uom) - float(promo_disc) - prd['GRPDISC_AMT'])
            prd['CUST_DISC'] = round(disc, store_rounding)
            prd['PROMO_DISC'] = float(promo_disc)
        elif disc is not None and promo_disc is None:
            prd['CUST_DISC_PERC'] = disc
            disc = (float(disc) / 100) * (float(gross_total_all_uom) - prd['GRPDISC_AMT'])
            prd['CUST_DISC'] = round(disc, store_rounding)

    def calculate_group_disc(self, grpdisc, prd, store_rounding, gross_total_all_uom):
        for discount in grpdisc:
            if discount['PRD_ID'] == ProductGet.ProductGet().user_retrieves_prd_by_prd_code(prd['PRD_CODE'])['ID']:
                group_disc = discount
                prd['GRPDISC_AMT'] = (float(group_disc['DISCOUNT']) / 100) * float(gross_total_all_uom)
                prd['GRPDISC_AMT'] = round(prd['GRPDISC_AMT'], store_rounding)
                print("DONE ROUND :", prd['GRPDISC_AMT'])
                prd['DISCOUNT'] = group_disc['DISCOUNT']
                prd['GRPDISC_ID'] = group_disc['GRPDISC_ID']

    def accumulative_tax(self, count, tax_setting, cust_disc, disc_impact, promo_disc, group_disc, prd, store_rounding):
        total_of_all_lvl_tax = 0
        tax_list = []
        tax_desc_list = []
        prev_lvl_tax = 0
        gross = prd['GROSS_AMT']
        num = count
        for _ in range(count):
            num = num - 1
            tax_sett_info = tax_setting[num]
            tax_rate = tax_sett_info['TAX_RATE']
            print("tax rate",tax_rate)
            """Accumulative tax if gross =50, leve 1 tax = 5%  amt of tax= 2.5 """
            """level 2 tax will apply on gross + previous level tax amt which is 50 +2.5 = 52.5"""
            if prev_lvl_tax != 0:
                gross = gross + prev_lvl_tax
            if tax_sett_info['APPLY_ON'][0] == 'Net':
                """Net Amout will always - promo and customer discount"""
                tax_amt = (gross - cust_disc) * float(tax_rate) / 100
                taxable_amt = gross - cust_disc
                prev_lvl_tax = tax_amt
                tax_amt = round(tax_amt, store_rounding)
            else:
                """Check discount impact on promo disc or cust disc"""
                tax_amt, taxable_amt = self.discount_impact(disc_impact, gross, cust_disc, promo_disc, group_disc, tax_rate)
                prev_lvl_tax = tax_amt
                tax_amt = round(tax_amt, store_rounding)
            tax_list.append(tax_amt)
            tax_desc_list.append(tax_sett_info['TAX_CD'])
            total_of_all_lvl_tax += tax_amt
        prd['NET_TTL_TAX'] = tax_amt
        prd['ALL_LEVEL_TAX'] = tax_list
        prd['ALL_TAX_DESC'] = tax_desc_list
        prd['TAXABLE_AMT'] = round(taxable_amt, store_rounding)
        prd['TOTAL_TAX'] = round(total_of_all_lvl_tax, store_rounding)
        return prd

    def tax_calculation(self, tax_setting, prd):
        promo_disc = BuiltIn().get_variable_value("${promo_disc}")
        if promo_disc is None:
            promo_disc = 0
        TokenAccess.TokenAccess().get_token_by_role('hqadm')

        if BuiltIn().get_variable_value(self.SUPP_INFO) is not None:
            disc_impact = None
        else:
            AppSetupGet.AppSetupGet().user_retrieves_details_of_application_setup()
            app_setup = BuiltIn().get_variable_value(self.APPSETUP_INFO)
            disc_impact = app_setup['DISCOUNTS_TO_BE_INCLUDED_FOR_TAX_COMPUTATION']
        store_rounding = BuiltIn().get_variable_value(self.STORE_ROUNDING)
        count = len(tax_setting)
        accumulative = tax_setting[0]['TAX_ACCUMULATIVE']
        cust_disc = prd['CUST_DISC']
        if 'GRPDISC_AMT' in prd:
            group_disc = prd['GRPDISC_AMT']
        else:
            group_disc = 0
        if accumulative:
            """When Accumulative tax = on, then multi apply will auto off """
            prd = self.accumulative_tax(count, tax_setting, cust_disc, disc_impact, promo_disc, group_disc, prd, store_rounding)
        else:
            print("no accumlat tax")
            """When Tax accumulative is off"""
            prd = self.non_accumulative_tax_calculation(prd, tax_setting, cust_disc, promo_disc, group_disc, disc_impact, store_rounding)
        return prd

    def non_accumulative_tax_calculation(self, prd, tax_setting, cust_disc, promo_disc, group_disc, disc_impact, store_rounding):
        count = len(tax_setting)
        prev_lvl_tax = 0
        prev_tax_info = []
        num = count
        gross = prd['GROSS_AMT']
        tax_list = []
        tax_desc_list = []
        total_of_all_lvl_tax = 0
        for i in range(count):
            num = num - 1
            tax_sett_info = tax_setting[num]
            apply_on = tax_sett_info['APPLY_ON']
            tax_rate = float(tax_sett_info['TAX_RATE'])
            """when multi apply is on and level have many apply on, it will add on into total variable"""
            total_of_current_lvl_tax = 0
            for item in apply_on:
                tax_amt, taxable_amt = self.non_accumulative_tax(item,gross,cust_disc,promo_disc, group_disc, tax_rate, disc_impact, prev_tax_info)
                total_of_current_lvl_tax += tax_amt
                prev_lvl_tax = total_of_current_lvl_tax
            total_of_all_lvl_tax += prev_lvl_tax
            print("LEVEL {0} Tax = {1}".format((i + 1), total_of_current_lvl_tax))
            tax_list.append(round(total_of_current_lvl_tax, store_rounding))
            tax_desc_list.append(tax_sett_info['TAX_CD'])
            prev_tax_details = {
                "TAX_CD": tax_sett_info['TAX_CD'],
                "TAX_AMT": tax_amt
            }
            prev_tax_info.append(prev_tax_details)
            print("total tax = ", total_of_all_lvl_tax)
        total_net_tax = round(gross - cust_disc - float(promo_disc) - group_disc + total_of_all_lvl_tax, store_rounding)
        prd['TAX_SETTING'] = tax_setting[0]
        prd['NET_TTL_TAX'] = total_net_tax
        prd['ALL_LEVEL_TAX'] = tax_list
        prd['ALL_TAX_DESC'] = tax_desc_list
        prd['TAXABLE_AMT'] = round(taxable_amt, store_rounding)
        prd['TOTAL_TAX'] = round(total_of_all_lvl_tax, store_rounding)
        return prd

    def non_accumulative_tax(self, item,gross, cust_disc, promo_disc, group_disc, tax_rate, disc_impact, prev_tax_info):
        taxable_amt = ""
        if item == 'Net':
            taxable_amt = gross - cust_disc - float(promo_disc) - group_disc
            tax_amt = taxable_amt * tax_rate / 100
        elif item == 'Gross':
            """Check discount impact on promo disc or cust disc"""
            tax_amt = self.discount_impact(disc_impact, gross, cust_disc, promo_disc, group_disc, tax_rate)
            taxable_amt = tax_amt[1]
            tax_amt = tax_amt[0]
        else:
            for prev_tax in prev_tax_info:
                if item == prev_tax['TAX_CD']:
                    tax_amt = prev_tax['TAX_AMT'] * tax_rate / 100
                    taxable_amt = prev_tax['TAX_AMT']

        return tax_amt, taxable_amt

    def discount_impact(self, disc_impact, gross, cust_disc, promo_disc, group_disc, tax_rate):
        cust_flag = False
        promo_flag = False
        group_flag = False
        tax_able_amt = gross
        if disc_impact:
            self.check_disc(disc_impact)
        if cust_flag and promo_flag and group_flag:
            tax_able_amt = tax_able_amt - float(cust_disc) - float(promo_disc) - float(group_disc)
        elif cust_flag and promo_flag:
            tax_able_amt = tax_able_amt - float(cust_disc) - float(promo_disc)
        elif group_flag and promo_flag:
            tax_able_amt = tax_able_amt - float(group_disc) - float(promo_disc)
        elif cust_flag:
            tax_able_amt = tax_able_amt - float(cust_disc)
        elif promo_flag:
            tax_able_amt = tax_able_amt - float(promo_disc)
        elif group_flag:
            tax_able_amt = tax_able_amt - float(group_disc)
            print("in promo flag tax_able_amt", tax_able_amt)
        tax_amt = tax_able_amt * float(tax_rate) / 100
        return tax_amt, tax_able_amt

    def check_disc(self, disc_impact):
        cust_flag = False
        promo_flag = False
        group_flag = False
        for item in disc_impact:
            if item.get('VAL_CODE') == 'CUST_DISC':
                cust_flag = True
            elif item.get('VAL_CODE') == 'PROMO_DISC':
                promo_flag = True
            elif item.get('VAL_CODE') == 'CUSTGRP_DISC':
                group_flag = True
        return cust_flag, promo_flag, group_flag

    def round_half_up(self, n, decimals=0):
        multiplier = 10 ** decimals
        return math.floor(n * multiplier + 0.5) / multiplier

    def rounding_based_on_setup(self, num):
        body_result = BuiltIn().get_variable_value(self.APPSETUP_INFO)
        if body_result is None:
            AppSetupGet.AppSetupGet().user_retrieves_details_of_application_setup()
            body_result = BuiltIn().get_variable_value(self.APPSETUP_INFO)
        round_value = body_result['ROUND_OFF_VALUE']['ROUND_OFF_VALUE']
        round_to = body_result['ROUND_OFF_TO_THE']['ROUND_OFF_TO_THE']
        round_decimal = int(body_result['ROUND_OFF_DECIMAL']['ROUND_OFF_DECIMAL'])
        output = 0
        if round_to == 'Lowest' and round_value == '0.5':
            floor = math.floor(num)
            decimal = num - floor
            if decimal < 0.5:
                output = math.floor(num)
            else:
                output = floor + 0.5
        elif round_to == 'Nearest' and round_value == '0.5':
            output = round(num * 2) / 2
        adjust_num = round(num - output, 4)
        adjust_num = float(0 - adjust_num)
        return format(output, ".{0}f".format(int(round_decimal))), adjust_num

    def calculation_for_product_total(self, prd_info):
        prd_list = []
        total_gross = 0
        total_taxable = 0
        total_nontaxable = 0
        total_tax = 0
        total_net = 0
        total_net_tax = 0
        total_cust_disc = 0
        total_promo_disc = 0
        store_rounding = BuiltIn().get_variable_value(self.STORE_ROUNDING)
        for prd in prd_info:
            prd_type = BuiltIn().get_variable_value("${prdType}")
            if prd_type is not None:
                if prd_type['PRD_SLSTYPE'] == 'P':
                    break
            uom_list = []
            print("ADE PRD DETAILS", prd)
            for i in range(len(prd['PRD_UOM'])):
                tax_list = []
                if "TAX_SETTING" in prd:
                    try:
                        tax_amt = prd['ALL_LEVEL_TAX'][i]
                        unit_tax = round(tax_amt / int(prd['PRD_UOM'][i]['QTY']), store_rounding)
                    except Exception as e:
                        print(e.__class__, "occured")
                        tax_amt = 0
                        unit_tax = 0

                    tax_details = {
                        "TAX_STRUCTURE_ID": prd['TAX_SETTING']['TAX_STRUCTURE_ID'],
                        "TAX_ID": prd['TAX_SETTING']['ID'],
                        "UNIT_TAX": unit_tax,
                        "TAX_AMT": tax_amt,
                        "TAXABLE_AMT": prd['PRD_UOM'][i]['GROSS_PER_UOM'],
                        "TAX_PERC": int(prd['TAX_SETTING']['TAX_RATE']),
                        "APPLY_SEQ": int(prd['TAX_SETTING']['SEQ_NO']),
                        "TAX_CODE": prd['TAX_SETTING']['TAX_CD']
                    }
                    tax_list.append(tax_details)
                uom_details = {
                    "UOM_ID": prd['PRD_UOM'][i]['UOM_ID'],
                    "PRD_QTY": int(prd['PRD_UOM'][i]['QTY']),
                    "UOM_LISTPRC": prd['PRD_UOM'][i]['PRD_LISTPRC_UOM'],
                    "GROSS_AMT": prd['PRD_UOM'][i]['GROSS_PER_UOM'],
                    "TAXES": tax_list
                }
                uom_list.append(uom_details)
            product_details = {
                "PRD_ID": ProductGet.ProductGet().user_retrieves_prd_by_prd_code(prd['PRD_CODE'])['ID'],
                "MRP": 0,
                "PRD_LISTPRC": prd['UNIT_PRICE'],
                "PRD_INDEX": 1,
                "UOMS": uom_list
            }
            total_gross = total_gross + prd['GROSS_AMT']
            total_cust_disc = round(float(total_cust_disc + prd['CUST_DISC']), 5)
            total_groupdisc = BuiltIn().get_variable_value("${ttl_groupdisc}")
            if total_groupdisc is None :
                total_groupdisc = 0
            print ("GRP DISC TOTAL :", total_groupdisc)
            store_rounding = BuiltIn().get_variable_value(self.STORE_ROUNDING)
            if prd.get('PROMO_DISC'):
                total_promo_disc = total_promo_disc + prd['PROMO_DISC']
            total_net = round(total_gross - total_cust_disc - total_promo_disc - total_groupdisc,  store_rounding)

            if len(tax_list) != 0:
                total_taxable = total_taxable + prd['TAXABLE_AMT']
                total_tax = total_tax + prd['TOTAL_TAX']
                total_net_tax = total_net_tax + prd['NET_TTL_TAX']
            else:
                total_net_tax = total_net_tax + total_net
                total_nontaxable = total_nontaxable + total_net
            prd_list.append(product_details)
        total = {
            "TTL_GROSS": round(total_gross, store_rounding),
            "TTL_CUST_DISC": total_cust_disc,
            "TTL_PROMO_DISC": total_promo_disc,
            "TTL_TAXABLE": total_taxable,
            "TTL_NONTAXABLE": round(total_nontaxable, store_rounding),
            "TTL_TAX": round(total_tax, store_rounding),
            "TTL_NET_NON_TAX": total_net,
            "TTL_NET": round(total_net_tax, store_rounding)
        }
        return prd_list, total

    @keyword("user intends to insert product '${prod}' with uom '${prod_uom}'")
    def user_intends_to_insert_product_with_uom(self, prod, prod_uom):
        details = self.builtin.get_variable_value('${fixedData}')
        if not details:
            if self.builtin.get_variable_value(self.RTN_DETAILS):
                details = self.builtin.get_variable_value(self.RTN_DETAILS)
            elif self.builtin.get_variable_value(self.INV_DETAILS):
                details = self.builtin.get_variable_value(self.INV_DETAILS)
            if details is None:
                details = self.builtin.get_variable_value('${cn_header_details}')
        prod_uom_split = prod_uom.split(",")
        prd_list = []
        uom_list = []
        for uom in prod_uom_split:
            uom_selected = uom.split(":")
            uom_details = {
                "UOM": uom_selected[0],
                "QTY": uom_selected[1]
            }
            uom_list.append(uom_details)
        prd_type = BuiltIn().get_variable_value("${prdType}")
        print("TYPE IS TRX: ", prd_type)
        if prd_type is None or prd_type['PRD_SLSTYPE'] == 'S':
            sls_type = 'S'
        else:
            sls_type = 'P'
        prd_details = {
            "PRD_CODE": prod,
            "PRD_UOM": uom_list,
            "PRD_UOM_DETAILS": prod_uom,
            "PRD_SLSTYPE": sls_type,
        }
        data = details.get('PROD_ASS_DETAILS')
        if data:
            details['PROD_ASS_DETAILS'].append(prd_details)
        else:
            prd_list.append(prd_details)
            details['PROD_ASS_DETAILS'] = prd_list
        self.builtin.set_test_variable('${fixedData}', details)
        self.builtin.set_test_variable(self.INV_DETAILS, details)
        if self.builtin.get_variable_value(self.RTN_DETAILS):
            self.builtin.set_test_variable(self.RTN_DETAILS, details)
        self.builtin.set_test_variable('${cn_header_details}', details)
        return details
