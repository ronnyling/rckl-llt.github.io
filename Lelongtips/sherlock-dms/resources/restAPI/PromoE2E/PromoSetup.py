from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Promo import PromoBuyTypeGet
from resources.restAPI.SysConfig.LineOfBusiness import LineOfBusinessGet
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure import StructureGet
from resources.restAPI.MasterDataMgmt.Product import ProductGet, ProductUomGet
from resources.restAPI.Config.ReferenceData.Uom import UomGet
from resources.restAPI.Config.ReferenceData.ClaimType import ClaimTypeGet
from resources.restAPI.Config.AppSetup import AppSetupGet
from resources.restAPI.MasterDataMgmt.Promo.PromoCalculation import PromoDealCalculation
from resources.restAPI.MasterDataMgmt.Promo import PromoApprove, PromoEntitlementPost, PromoApply, PromoAssignPost, PromoDelete, PromoPost
from resources.restAPI import PROTOCOL, APP_URL, YamlDataManipulator, BuiltIn, COMMON_KEY
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.TransactionFormula import TransactionFormula
from setup.hanaDB import HanaDB
from robot.api.deco import keyword
from resources.restAPI.Common import TokenAccess, APIAssertion


import secrets, datetime
import json


NOW = datetime.datetime.now()
DT_FORMAT = "%Y-%m-%dT00:00:00.000Z"
DISC_METHOD = 'Discount Method'
PROMO_END_POINT_URL = PROTOCOL + "promotion" + APP_URL


class PromoSetup(object):
    FOC_FLAG = "${foc_flag}"
    YAML_PROMO_SETUP = "${promo_setup}"
    SALE_ORDER = "Sales Order"
    PROMO_ID = "${promo_id}"
    PROMO_RES = "${promo_res_list}"
    PRD_INFO = "${prd_info}"
    PRD_ARRAY = "${PRD_ARRAY}"

    @keyword('user creates promotion using ${data_type}')
    def user_creates_promotion_using(self, data_type):
        list_of_promo = {
            "Discount By Value - By Amount": "PromoDealValueAmt.yaml",
            "Discount By Value - By Quantity": "PromoDealValueQty.yaml",
            "Discount By Percentage - By Amount": "PromoDealPercentAmt.yaml",
            "Discount By Percentage - By Quantity": "PromoDealPercentQty.yaml",
            "Discount By Free Product (OR condition) - By Amount": "PromoDealFOCORAmt.yaml",
            "Discount By Free Product (OR condition) - By Quantity": "PromoDealFOCORQty.yaml",
            "Discount By Free Product (AND condition) - By Amount": "PromoDealFOCANDAmt.yaml",
            "Discount By Free Product (AND condition) - By Quantity": "PromoDealFOCANDQty.yaml",
            # With Budget
            "Discount By Percentage - By Amount with Budget": "PromoDealPercentAmtBudget.yaml",
            # With Claim
            "Discount By Percentage - By Quantity with Claim": "PromoDealPercentQtyClaim.yaml",
            # With POSM Assignment
            "Discount By Percentage - By Amount with POSM Assignment": "PromoDealPercentAmtPOSMAsg.yaml",
            # With Max Count
            "Discount By Value with Max Count - By Amount": "PromoDealMaxValueAmt.yaml",
            "Discount By Value with Max Count - By Quantity": "PromoDealMaxValueQty.yaml",
            "Discount By Percentage with Max Count - By Amount": "PromoDealMaxPercentAmt.yaml",
            "Discount By Percentage with Max Count - By Quantity": "PromoDealMaxPercentQty.yaml",
            "Discount By Free Product (OR condition) with Max Count - By Amount": "PromoDealMaxFOCORAmt.yaml",
            "Discount By Free Product (OR condition) with Max Count - By Quantity": "PromoDealMaxFOCORQty.yaml",
            "Discount By Free Product (AND condition) with Max Count - By Amount": "PromoDealMaxFOCANDAmt.yaml",
            "Discount By Free Product (AND condition) with Max Count - By Quantity": "PromoDealMaxFOCANDQty.yaml",
            # With QPS
            "Discount By Value with QPS - By Amount": "PromoDealQPSValueAmt.yaml",
            "Discount By Value with QPS - By Quantity": "PromoDealQPSValueQty.yaml",
            "Discount By Percentage with QPS - By Amount": "PromoDealQPSPercentAmt.yaml",
            "Discount By Percentage with QPS - By Quantity": "PromoDealQPSPercentQty.yaml",
            "Discount By Free Product (OR condition) with QPS - By Amount": "PromoDealQPSFOCORAmt.yaml",
            "Discount By Free Product (OR condition) with QPS - By Quantity": "PromoDealQPSFOCORQty.yaml",
            "Discount By Free Product (AND condition) with QPS - By Amount": "PromoDealQPSFOCANDAmt.yaml",
            "Discount By Free Product (AND condition) with QPS - By Quantity": "PromoDealQPSFOCANDQty.yaml",
            # With Combi
            "Discount By Value with Combi - By Amount": "PromoDealCombiValueAmt.yaml",
            "Discount By Value with Combi - By Quantity": "PromoDealCombiValueQty.yaml",
            "Discount By Percentage with Combi - By Amount": "PromoDealCombiPercentAmt.yaml",
            "Discount By Percentage with Combi - By Quantity": "PromoDealCombiPercentQty.yaml",
            "Discount By Free Product (OR condition) with Combi - By Amount": "PromoDealCombiFOCORAmt.yaml",
            "Discount By Free Product (OR condition) with Combi - By Quantity": "PromoDealCombiFOCORQty.yaml",
            "Discount By Free Product (AND condition) with Combi - By Amount": "PromoDealCombiFOCANDAmt.yaml",
            "Discount By Free Product (AND condition) with Combi - By Quantity": "PromoDealCombiFOCANDQty.yaml",
            # With FOC Recurring
            "Discount By Free Product (OR condition) with FOC Recurring - By Amount": "PromoDealFOCRecFOCORAmt.yaml",
            "Discount By Free Product (OR condition) with FOC Recurring - By Quantity": "PromoDealFOCRecFOCORQty.yaml",
            "Discount By Free Product (AND condition) with FOC Recurring - By Amount": "PromoDealFOCRecFOCANDAmt.yaml",
            "Discount By Free Product (AND condition) with FOC Recurring - By Quantity": "PromoDealFOCRecFOCANDQty.yaml"
        }
        result = []
        promo_res_list = []
        promo_setup = YamlDataManipulator.YamlDataManipulator().user_retrieves_data_from_yaml(list_of_promo[data_type])
        BuiltIn().set_test_variable("${yaml_file}", list_of_promo[data_type])
        BuiltIn().set_test_variable(self.YAML_PROMO_SETUP, promo_setup)
        for i in range(len(promo_setup)):
            count = i + 1
            setup_details = promo_setup[f"Promo {count}"]['Setup']
            print("DATA Retrieved", setup_details)
            DistributorGet.DistributorGet().user_retrieves_all_distributors_list()
            respond = self.promotion_creation(setup_details)
            promo_res_list.append(respond[1])
            APIAssertion.APIAssertion().expected_return_status_code("201")
            result.append(respond[1]['ID'])
            assignment_details = promo_setup[f"Promo {count}"][self.SALE_ORDER]
            PromoAssignPost.PromoAssignPost().assign_promotion(assignment_details['Distributor'], assignment_details['Customer'], "without")
            BuiltIn().set_test_variable(self.PROMO_ID, respond[1]['ID'])
            BuiltIn().set_test_variable(self.PROMO_RES, promo_res_list)
        BuiltIn().set_test_variable("${result}", result)

    def output_payload(self, prd_id, prd_uom_id, foc_qty):
        BuiltIn().set_test_variable("${prd_id}", prd_id)
        ProductGet.ProductGet().user_retrieves_product_by_id()
        uom_res = ProductUomGet.ProductUomGet().user_retrieves_prd_uom_by_id(prd_id,
                                                                             prd_uom_id)
        prd_res = BuiltIn().get_variable_value("${prd_res}")
        prd_cd = prd_res['PRD_CD']
        foc_details = {
            "PRD_CODE": prd_cd,
            "PRD_UOM": uom_res['UOM_CD'],
            "PRD_FOC_QTY": foc_qty
        }
        return foc_details

    def check_foc_result(self, yaml_file, python_r, dms_r, promo_count):
        true_count = 0
        python_foc_details_info = []
        dms_foc_details_info = []
        for i in range(len(python_r)):
            for dms_result in dms_r:
                if python_r[i]['FOC_PRD_ID'] == dms_result['PRD_ID'] and int(dms_result['FOC_QTY']) == int(python_r[i]['FOC_QTY']):
                        true_count = true_count + 1
                        payload = self.output_payload(python_r[i]['FOC_PRD_ID'],
                                                       python_r[i]['FOC_UOM_ID'],int(python_r[i]['FOC_QTY']))
                        python_foc_details_info.append(payload)
                        print("dms_r[i]",dms_r[i])
                        payload = self.output_payload(dms_r[i]['PRD_ID'],
                                                      dms_r[i]['FOC_UOM_ID'], int(dms_r[i]['FOC_QTY']))
                        dms_foc_details_info.append(payload)
                        break;
        if true_count == len(python_r):
            flag = True
        else:
            flag = False
        output = {
            "API_RESULT": python_foc_details_info,
            "PYTHON_RESULT": dms_foc_details_info
        }
        output1 = {"Output": output}
        YamlDataManipulator.YamlDataManipulator().user_updates_yaml_data(yaml_file, f"Promo {promo_count + 1}",
                                                                         **output1)
        return flag

    def assert_api_result_with_calculated_result(self):
        promo_setup = BuiltIn().get_variable_value(self.YAML_PROMO_SETUP)
        yaml_file = BuiltIn().get_variable_value("${yaml_file}")
        dms_result = BuiltIn().get_variable_value("${dms_result}")
        python_result = BuiltIn().get_variable_value("${python_result}")
        store_rounding = BuiltIn().get_variable_value('${store_rounding}')
        foc_flag = BuiltIn().get_variable_value(self.FOC_FLAG)
        flag = True
        if foc_flag:
            for i in range(len(promo_setup)):
                flag = self.check_foc_result(yaml_file, python_result[i], dms_result[i], i)
        else:
            for i in range(len(promo_setup)):
                api_result = round(float(dms_result[i]), store_rounding)
                py_calculation = round(float(python_result[i][0]['PROMO_DISC']), store_rounding)
                if py_calculation != api_result:
                    flag = False
                    break
                output = {
                    "API_RESULT": api_result,
                    "PYTHON_RESULT": py_calculation
                }
                output1 = {"Output": output}
                YamlDataManipulator.YamlDataManipulator().user_updates_yaml_data(yaml_file, f"Promo {i+1}", **output1)
        BuiltIn().set_test_variable("${overall_result}", flag)

    def asserted_result_is_matched(self):
        result = BuiltIn().get_variable_value("${overall_result}")
        assert result is True, "Promo discount is not match"

    def user_approve_promotion(self):
        promo_res_list = BuiltIn().get_variable_value(self.PROMO_RES)
        for item in promo_res_list:
            BuiltIn().set_test_variable(self.PROMO_ID, item['ID'])
            PromoApprove.PromoApprove().approve_promotion()

    def user_create_sales_order(self):
        all_prd_array = []
        promo_setup = BuiltIn().get_variable_value(self.YAML_PROMO_SETUP)
        for promo_details in promo_setup:
            sales_order = promo_setup[promo_details][self.SALE_ORDER]
            prd = self.product(sales_order)
            prd_array = []
            uom_array = []
            for product in prd:
                for x in range(len(product['UOM'])):
                    key = list(product['UOM'].keys())[x]
                    uom_qty = {
                        'UOM': key,
                        'QTY': product['UOM'][key]
                    }
                    uom_array.append(uom_qty)
                    prd_info = {
                    "PRD_CODE": product['Code'],
                    "PRD_UOM": uom_array
                }
                prd_array.append(prd_info)
            TransactionFormula().tran_calculation_for_gross_and_cust_disc('PRIME', sales_order['Customer'], "percent", prd_array)
            TransactionFormula().tax_calculation_for_multi_product()
            prd_info = BuiltIn().get_variable_value(self.PRD_INFO)
            BuiltIn().set_test_variable(self.PRD_INFO, "")
            all_prd_array.append(prd_info)
        BuiltIn().set_test_variable(self.PRD_ARRAY, all_prd_array)

    def user_entitle_promotion(self):
        promo_res_list = BuiltIn().get_variable_value(self.PROMO_RES)
        promo_setup = BuiltIn().get_variable_value(self.YAML_PROMO_SETUP)
        prd_array = BuiltIn().get_variable_value(self.PRD_ARRAY)
        count = 0
        prd_payload = []
        for promo_details in promo_setup:
            BuiltIn().set_test_variable("${promo_cd}", promo_res_list[count]['PROMO_CD'])
            BuiltIn().set_test_variable(self.PRD_INFO, prd_array[count])
            PromoEntitlementPost.PromoEntitlementPost().entitle_promotion(promo_setup[promo_details][self.SALE_ORDER])
            count = count + 1
            prd_list = BuiltIn().get_variable_value("${prd_list}")
            prd_payload.append(prd_list)
        BuiltIn().set_test_variable("${prd_list_payload}", prd_payload)

    def user_apply_promotion(self):
        promo_setup = BuiltIn().get_variable_value(self.YAML_PROMO_SETUP)
        promo_res_list = BuiltIn().get_variable_value(self.PROMO_RES)
        prd_array = BuiltIn().get_variable_value(self.PRD_ARRAY)
        prd_list_payload = BuiltIn().get_variable_value("${prd_list_payload}")
        foc_flag = BuiltIn().get_variable_value(self.FOC_FLAG)
        promo_disc_list = []
        for i in range(len(promo_setup)):
            BuiltIn().set_test_variable("${prd_list}", prd_list_payload[i])
            BuiltIn().set_test_variable(self.PRD_INFO, prd_array[i])
            BuiltIn().set_test_variable("${promo_response}", promo_res_list[i])
            BuiltIn().set_test_variable(self.PROMO_ID, promo_res_list[i]['ID'])
            dms_result = PromoApply.PromoApply().apply_promotion()
            if foc_flag:
                promo_disc_list.append(dms_result['TXN_PROMO_ALLOCFOC'])
            else:
                promo_disc_list.append(dms_result['TXN_PROMO'][0]['DISC_AMT'])
        BuiltIn().set_test_variable("${dms_result}", promo_disc_list)

    def user_calculate_promo_disc_amount(self):
        promo_setup = BuiltIn().get_variable_value(self.YAML_PROMO_SETUP)
        promo_res = BuiltIn().get_variable_value(self.PROMO_RES)
        prd_array = BuiltIn().get_variable_value(self.PRD_ARRAY)
        python_disc_list = []
        for i in range(len(promo_setup)):
            BuiltIn().set_test_variable(self.PRD_INFO, prd_array[i])
            BuiltIn().set_test_variable("${promo_response}", promo_res[i])
            python_disc_result = PromoDealCalculation.PromoDealCalculation().calculate_promo_disc_percentage()
            python_disc_list.append(python_disc_result)
        print("py result", python_disc_list)
        BuiltIn().set_test_variable("${python_result}", python_disc_list)


    def product(self, sales_order):
        flag = True
        count = 1
        prd = []
        product = "Product {0}".format(count)
        while flag:
            try:
                prd.append(sales_order[product])
                count += 1
                product = "Product {0}".format(count)
            except Exception as e:
                print(e.__class__, "occured")
                flag = False
        return prd

    def promotion_creation(self, setup_details):
        ttl_prod_assign = self.promo_product_assign(setup_details)
        ttl_promo_slab = self.promo_slab_creation(setup_details, ttl_prod_assign)
        payload = self.promo_setup(setup_details, ttl_promo_slab)
        payload = json.dumps(payload)
        print('Promotion Payload: ', payload)
        url = "{0}promotion".format(PROMO_END_POINT_URL)
        user_role = BuiltIn().get_variable_value("${user_role}")
        TokenAccess.TokenAccess().get_token_by_role(user_role)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${promo}", body_result)
            promotion_id = body_result['ID']
            promotion_cd = body_result['PROMO_CD']
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM PROMO where ID = '{0}'".format(promotion_id), 1)
            # HanaDB.HanaDB().disconnect_from_database()
            BuiltIn().set_test_variable(self.PROMO_ID, promotion_id)
            BuiltIn().set_test_variable("${promotion_cd}", promotion_cd)
        else:
            body_result = response.json()
            print("ERROR Message: ", body_result['message'])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return response.status_code, body_result

    def promo_product_assign(self, promo_setup):
        ttl_prod_assign = []
        count = 0
        for key in promo_setup.keys():
            if "Product " in key:
                count = count + 1
                product_assign = {
                    "ID": None,
                    "PROMO_SLAB_ID": None,
                    "PROMO_COMBI_GROUP_ID": None,
                    "PRDCAT_ID": None,
                    "PRDCAT_VALUE_ID": ProductGet.ProductGet().user_retrieves_prd_by_prd_code(promo_setup[f'Product {count}'])['ID'],
                    "UOM_ID": None,
                    "MIN_QTY": None,
                    "MUST_IND": None,
                    "VERSION": 1,
                    "action": "create"
                }
                ttl_prod_assign.append(product_assign)
        return ttl_prod_assign

    def promo_combi_assign(self, promo_setup):
        combi_assign = []
        count = 0
        for key in promo_setup.keys():
            if "Group " in key:
                buy_uom = None
                count = count + 1
                promo_prd = self.promo_product_assign(promo_setup[f'Group {count}'])
                if promo_setup[f'Group {count}'].get('BUY UOM'):
                    buy_uom = UomGet.UomGet().user_retrieves_uom_by_code_in_uom_listing(promo_setup[f'Group {count}'].get('BUY UOM'))['ID']
                product_assign = {
                    "ID": None,
                    "PROMO_SLAB_ID": None,
                    "GROUP_CD": str(count),
                    "MIN_BUY": promo_setup[f'Group {count}']['Min Buy'],
                    "MUST_IND": True,
                    "UOM_ID": buy_uom,
                    "PROMO_PRD": promo_prd,
                    "VERSION": 1,
                    "action": "create"
                }
                combi_assign.append(product_assign)
        return combi_assign

    def promo_foc_product_assign(self, promo_setup):
        ttl_foc_prod_assign = []
        count = 0
        and_cond = BuiltIn().get_variable_value('${and_cond}')
        for key in promo_setup.keys():
            if "Product " in key:
                count = count + 1
                print(promo_setup)
                if and_cond is True:
                    prd_id = ProductGet.ProductGet().user_retrieves_prd_by_prd_code(promo_setup[f'Product {count}']['Product'])['ID']
                    cost_price = str(promo_setup[f'Product {count}']['Cost Price'])
                    foc_qty = promo_setup[f'Product {count}']['Free Quantiy']
                    foc_uom = ProductUomGet.ProductUomGet().user_retrieves_prd_uom_by_code(prd_id, promo_setup[f'Product {count}']['Free UOM'])['ID']
                else:
                    prd_id = ProductGet.ProductGet().user_retrieves_prd_by_prd_code(promo_setup[f'Product {count}'])['ID']
                    cost_price = "0.00"
                    foc_qty = None
                    foc_uom = None
                product_assign = {
                    "ID": None,
                    "COST_PRC": cost_price,
                    "FOC_QTY": foc_qty,
                    "FOC_UOM_ID": foc_uom,
                    "PROMO_SLAB_ID": None,
                    "PRDCAT_ID": None,
                    "PRDCAT_VALUE_ID": prd_id,
                    "VERSION": 1,
                    "action": "create"
                }
                ttl_foc_prod_assign.append(product_assign)
        return ttl_foc_prod_assign

    def if_foc_promo(self, promo_setup, count):
        free_qty = None
        free_uom = None
        BuiltIn().set_test_variable(self.FOC_FLAG, True)
        and_cond = True
        if promo_setup.get('FOC Condition') == 'OrCond':
            free_qty = promo_setup[f'Tier {count}']['Free Quantiy']
            free_uom = UomGet.UomGet().user_retrieves_uom_by_code_in_uom_listing(promo_setup.get('FOC UOM'))['ID']
            and_cond = False
        BuiltIn().set_test_variable('${and_cond}', and_cond)
        foc_cond = PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_foc_cond(promo_setup.get('FOC Condition'))['ID']
        foc_details = self.promo_foc_product_assign(promo_setup[f'Tier {count}']['Free Product'])
        return free_qty, free_uom, foc_cond, foc_details

    def set_fe_uom_id(self, promo_setup):
        if promo_setup.get('Buy Type') != 'Amount' and \
                promo_setup.get('Discount Method') != 'DiscountByPerc' and bool(promo_setup.get('Scheme')['Forevery']):
            fe_uom_id = UomGet.UomGet().user_retrieves_uom_by_code_in_uom_listing(promo_setup.get('BUY UOM'))['ID']
            return fe_uom_id
        else:
            return None

    def promo_slab_creation(self, promo_setup, ttl_prod_assign):
        ttl_promo_slab = []
        count = 0
        fe_uom_id = None
        AppSetupGet.AppSetupGet().user_retrieves_details_of_application_setup()
        body_result = BuiltIn().get_variable_value('${body_result}')
        store_rounding = int(body_result['ROUND_OFF_DECIMAL']['ROUND_OFF_DECIMAL'])
        fe_uom_id = self.set_fe_uom_id(promo_setup)
        for key in promo_setup.keys():
            if "Tier " in key:
                count = count + 1
                free_qty = None
                free_uom = None
                foc_cond = None
                dist_amt = '0'
                dist_perc = 0
                for_every = 0
                foc_details= []
                combi_assign = []
                if promo_setup[f'Tier {count}']['Forevery']:
                    for_every = int(round(promo_setup[f'Tier {count}']['Forevery'], store_rounding))
                if promo_setup.get(DISC_METHOD) == 'DiscountByValue':
                    dist_amt = str(round(promo_setup[f'Tier {count}']['Discount'], store_rounding))
                elif promo_setup.get(DISC_METHOD) == 'DiscountByPerc':
                    dist_perc = promo_setup[f'Tier {count}']['Percentage']
                elif promo_setup.get(DISC_METHOD) == 'FreeProduct':
                    free_qty, free_uom, foc_cond, foc_details = self.if_foc_promo(promo_setup, count)
                if promo_setup['Scheme'].get('Combi') is True:
                    ttl_prod_assign = []
                    combi_assign = self.promo_combi_assign(promo_setup[f'Tier {count}']['Combi'])
                promo_slab_details = {
                    "ID": None,
                    "PROMO_ID": None,
                    "MECHANIC_TYPE": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_promo_mechanic_type(promo_setup.get(DISC_METHOD), "refParam")[0]['ID'],
                    "APPLY_ON": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_apply_on(promo_setup.get('Apply On'))['ID'],
                    "APPLY_UOM_ID": None,
                    "TOTAL_BUY": int(promo_setup[f'Tier {count}']['Total Buy']),
                    "MIN_BUY": 0,
                    "MAX_BUY": 0,
                    "FOR_EVERY": for_every,
                    "FOR_EVERY_UOM_ID": fe_uom_id,
                    "FOC_UOM_ID": free_uom,
                    "FOC_COND": foc_cond,
                    "DISC_AMT": dist_amt,
                    "DISC_PERC": dist_perc,
                    "FOC_QTY": free_qty,
                    "VERSION": 0,
                    "action": "create",
                    "FOC": foc_details,
                    "PROMO_PRD": ttl_prod_assign,
                    "PROMO_COMBI_GROUP": combi_assign
                }
                ttl_promo_slab.append(promo_slab_details)
        return ttl_promo_slab

    def promo_setup(self, setup_details, ttl_promo_slab):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        buy_uom = None
        claim_date = None
        claim_perc = None
        claim_type_id = None
        claim_ind = False
        max_flag = False
        max_count = 0
        budget_amt = "0.00"
        if setup_details.get('BUY UOM'):
            buy_uom = UomGet.UomGet().user_retrieves_uom_by_code_in_uom_listing(setup_details.get('BUY UOM'))['ID']
            if bool(setup_details.get('Scheme')['Forevery']):
                BuiltIn().set_test_variable("${fe_uom_id}", buy_uom)
        if setup_details['Scheme'].get('Max Flag'):
            max_flag = setup_details.get('Scheme')['Max Flag']
            max_count = setup_details.get('Scheme')['Max Count']
        if setup_details.get('Budget'):
            budget_amt = str(setup_details.get('Budget'))
        lob_details = LineOfBusinessGet.LineOfBusinessGet().get_lob_by_field_and_value("DEFAULT_IND", "true")

        start_time = COMMON_KEY.get_local_time()
        current_time = datetime.datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S.000Z')
        start_time = current_time.strftime(DT_FORMAT)
        end_time = (current_time + datetime.timedelta(days=365)).strftime(DT_FORMAT)
        if setup_details.get('Claim'):
            promo_type = setup_details.get('Type')
            ClaimTypeGet.ClaimTypeGet().get_claim_type_by_promo(promo_type)
            claim_ind = bool(setup_details.get('Claim'))
            claim_perc = int(setup_details.get('Claim Percent'))
            claim_date = (current_time + datetime.timedelta(days=369)).strftime(DT_FORMAT)
            claim_type_id = BuiltIn().get_variable_value("${rand_claim_type_id}")
        payload = {
            "ID": None,
            "PROMO_CD": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15)),
            "PROMO_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15)),
            "START_DT": str(start_time),
            "END_DT": str(end_time),
            "SPACEBUY_END_DT": None,
            "CLAIMABLE_IND": claim_ind,
            "CLAIM_ENDDT": claim_date,
            "TYPE": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_promo_type(setup_details.get('Type'), 'refParam')[0][
                'ID'],
            "PRIME_FLAG": "PRIME",
            "PROMO_SEQ_ID": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_promo_seq_by_code("random")['ID'],
            "BUY_TYPE": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_promo_buy_type(setup_details.get('Buy Type'),
                                                                                        'refParam')[0]['ID'],
            "BUY_UOM_ID": buy_uom,
            "CLAIM_TYPE_ID": claim_type_id,
            "AUTO_CHECKED": False,
            "AUTO_PROMO": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_auto_promo(setup_details.get('Apply Promo'))[
                'ID'],
            "SCHEME_QPS": False,
            "SCHEME_PRORATA": bool(setup_details.get('Scheme')['Prorata']),
            "SCHEME_RANGE": bool(setup_details.get('Scheme')['Range']),
            "SCHEME_COMBI": bool(setup_details.get('Scheme')['Combi']),
            "SCHEME_MRP": bool(setup_details.get('Scheme')['MRP']),
            "SCHEME_POSM_ASSIGNMENT": bool(setup_details.get('Scheme')['POSM Assignment']),
            "DISC_METHOD": False,
            "FOC_RECURRING": bool(setup_details.get('Scheme')['FOC Recurring']),
            "MAX_COUNT_FLAG": max_flag,
            "MAX_COUNT": max_count,
            "FOR_EVERY_FLAG": bool(setup_details.get('Scheme')['Forevery']),
            "PROMO_STATUS": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_promo_status('Active')['ID'],
            "APPR_IND": None,
            "APPR_DT": None,
            "NOTES": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15)),
            "RETAIL_CAP_FLAG": False,
            "RETAILER_CAP": None,
            "EXCL_PROMO": False,
            "NEW_POS": False,
            "BATCH": False,
            "MIN_BUY_IND": False,
            "CASH_CUST": None,
            "CREDIT_CUST": None,
            "LOB": lob_details['ID'],
            "PRD_ASS_TYPE": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_prod_assign_type(
                setup_details.get('Prod Assignment Type'))['ID'],
            "CUST_ASS_ALL": True,
            "DIST_ASS_ALL": True,
            "PRD_HIER_ID": StructureGet.StructureGet().user_get_hierid_from_hierarchy_structure_name("General Product Hierarchy"),
            "GEO_HIER_ID": None,
            "CUST_HIER_ID": None,
            "BUDGET": budget_amt,
            "SERVICE_TAX_ID": None,
            "SPACEBUY_PAYOUT_CUST_SPEC": False,
            "PROMO_SLABS": ttl_promo_slab,
            "PROMO_PRD_EX": [],
            "PROMO_MRP": [],
            "VERSION": 0,
            "action": "create",
            "CLAIMABLE_PERC": claim_perc
        }
        return payload

    def user_deletes_all_promotion_created(self):
        result = BuiltIn().get_variable_value("${result}")
        for data in result:
            BuiltIn().set_test_variable("${promo_id}", data)
            PromoPost.PromoPost().set_start_promotion("tomorrow")
            PromoDelete.PromoDelete().user_deletes_promotion()
            APIAssertion.APIAssertion().expected_return_status_code("200")
