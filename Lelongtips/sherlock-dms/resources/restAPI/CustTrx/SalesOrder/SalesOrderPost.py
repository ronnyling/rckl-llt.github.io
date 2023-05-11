import json
import secrets
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.MasterDataMgmt.Product import ProductUomGet, ProductGet
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route import RouteGet
from resources.restAPI.MasterDataMgmt.Warehouse import WarehouseGet
from resources.TransactionFormula import TransactionFormula
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod, TokenAccess
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from setup.hanaDB import HanaDB

END_POINT_URL = PROTOCOL + "salesorder" + APP_URL


class SalesOrderPost(object):
    SO_ID = "${res_bd_sales_order_id}"
    SO_NO = "${res_bd_so_no}"
    SO_HEADER_DETAILS = "${so_header_details}"
    SO_BODY_DETAILS = "${so_body_details}"
    WAREHOUSE_ID = "${WAREHOUSE_ID}"

    @keyword('user creates sales order with ${data_type} data')
    def user_creates_sales_order(self, data_type):
        url = "{0}salesorder".format(END_POINT_URL)
        BuiltIn().set_test_variable("${action}", "create")
        payload = self.payload_sales_order()
        payload = self.so_payload(payload[0], payload[1], payload[2],payload[3])
        print("Payload is {0}".format(payload))
        user = BuiltIn().get_variable_value("${user_role}")
        TokenAccess.TokenAccess().get_token_by_role(user)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print("POST Status code for sales order is " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.text)
        if response.status_code != 200:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            res_bd_sales_order_id = body_result['TXN_HEADER']['ID']
            dist_id = body_result['TXN_HEADER']['DIST_ID']
            whs_id = body_result['TXN_HEADER']['WHS_ID']
            principal = body_result['TXN_HEADER']['PRIME_FLAG']
            BuiltIn().set_test_variable("${dist_id}", dist_id)
            BuiltIn().set_test_variable("${whs_id}", whs_id)
            BuiltIn().set_test_variable("${principal}", principal)
            ids = BuiltIn().get_variable_value(self.SO_ID)
            if isinstance(ids, str):
                so_id_list = [BuiltIn().get_variable_value(self.SO_ID)]
                so_no_list = [BuiltIn().get_variable_value(self.SO_NO)]
            else:
                so_id_list = BuiltIn().get_variable_value(self.SO_ID)
                so_no_list = BuiltIn().get_variable_value(self.SO_NO)
            so_nos = body_result['TXN_HEADER']['TXN_NO']
            if ids is None:
                BuiltIn().set_test_variable(self.SO_ID, res_bd_sales_order_id)
                BuiltIn().set_test_variable(self.SO_NO, so_nos)
            else:
                so_id_list.append(res_bd_sales_order_id)
                so_no_list.append(body_result['TXN_HEADER']['TXN_NO'])
                BuiltIn().set_test_variable(self.SO_ID, so_id_list)
                BuiltIn().set_test_variable(self.SO_NO, so_no_list)
            print("IDS IS {0}".format(BuiltIn().get_variable_value(self.SO_ID)))
            res_bd_sales_order_id = str(res_bd_sales_order_id[0]).replace(":", "").replace("-", "")
            HanaDB.HanaDB().connect_database_to_environment()
            result_header = HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM TXN_ORDHDR where ID = '{0}'"
                                                                         .format(res_bd_sales_order_id), 1)
            result_body = HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM TXN_ORDPRD where TXN_ID = '{0}'"
                                                                       .format(res_bd_sales_order_id), 1)
            HanaDB.HanaDB().disconnect_from_database()
            assert result_header and result_body, "Record not found in database"
            print(body_result)

    def payload_sales_order(self):
        so_header_payload = self.so_header()
        prd_info = BuiltIn().get_variable_value("${prd_info}")
        so_prod_payload = self.so_products(prd_info)
        so_tax_payload = self.so_tax(prd_info)
        so_groupdisc_payload = self.so_groupdisc(prd_info)
        ttl_groupdisc = BuiltIn().get_variable_value("${ttl_groupdisc}")
        so_header_payload.update({"GRPDISC_AMT":str(ttl_groupdisc)})
        return so_header_payload, so_prod_payload, so_tax_payload, so_groupdisc_payload

    def so_header(self):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        route_id = BuiltIn().get_variable_value("${route_id}")
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        header_details = BuiltIn().get_variable_value('${fixedData}')
        if header_details is None:
            header_details = BuiltIn().get_variable_value(self.SO_HEADER_DETAILS)
        shipto_id = BuiltIn().get_variable_value("${shipto_id}")
        prime = header_details['PRIME_FLAG']
        if prime == "PRIME":
            whs_id = BuiltIn().get_variable_value(self.WAREHOUSE_ID)
        else:
            whs_id = BuiltIn().get_variable_value("${WAREHOUSE_ID_NP}")
        prd_id = BuiltIn().get_variable_value("${prd_id}")
        ProductGet.ProductGet().user_retrieves_prd_cd_by_prd_id(prd_id)
        prd_cd = BuiltIn().get_variable_value("${prd_cd}")
        if header_details.get('PROD_ASS_DETAILS') is None:
            uom = ProductUomGet.ProductUomGet().user_retrieves_prd_uom(prd_id)
            small_uom = len(uom) - 1
            rand_uom = uom[small_uom]['UOM_CD'] + ":" + str(secrets.choice(range(1, 5)))
            BuiltIn().set_test_variable("${fixedData}", header_details)
            header_details = TransactionFormula().user_intends_to_insert_product_with_uom(prd_cd, rand_uom)
        BuiltIn().set_test_variable("${res_bd_cust_id}", cust_id)
        cust_response = CustomerGet.CustomerGet().user_retrieves_cust_by_id()
        print("PRod details:", header_details['PROD_ASS_DETAILS'])
        TransactionFormula().tran_calculation_for_gross_and_cust_disc(prime, cust_response['CUST_NAME'], 'percent',
                                                                      header_details['PROD_ASS_DETAILS'])
        TransactionFormula().tax_calculation_for_multi_product()
        prd_info = BuiltIn().get_variable_value("${prd_info}")
        self.so_groupdisc(prd_info)
        ttl_details = TransactionFormula().calculation_for_product_total(prd_info)
        amount = TransactionFormula().rounding_based_on_setup(ttl_details[1]["TTL_NET"])
        ord_type = BuiltIn().get_variable_value("${invType}")
        if ord_type is None :
            txn_type = 'S'
        else :
            txn_type = ord_type['INVOICE_TXNTYPE']
            cust_response["CUST_DISC"] = '0.0000'
        sample_id = BuiltIn().get_variable_value("${sampling_id}")
        if sample_id is None:
            sample_id = None
        time = COMMON_KEY.get_local_time()
        payload = {
            "PRIME_FLAG": prime,
            "DIST_ID": dist_id,
            "ROUTE_ID": route_id,
            "CUST_ID": cust_id,
            "WHS_ID": whs_id,
            "SHIPTO_ID": shipto_id,
            "TXN_DT": time,
            "DELIVERY_DT": time,
            "PO_NO": None,
            "PO_ID": None,
            "PO_DT": time,
            "GROSS_TTL": str(ttl_details[1]["TTL_GROSS"]),
            "NET_TTL": str(ttl_details[1]['TTL_NET_NON_TAX']),
            "NET_TTL_TAX": str(ttl_details[1]["TTL_NET"]),
            "ADJ_AMT": str(amount[1]),
            "TAXABLE_AMT": str(ttl_details[1]["TTL_TAXABLE"]),
            "NONTAXABLE_AMT": str(ttl_details[1]["TTL_NONTAXABLE"]),
            "TAX_TTL": str(ttl_details[1]["TTL_TAX"]),
            "CUST_DISC_PERC": cust_response["CUST_DISC"],
            "CUST_DISC_AMT": str(ttl_details[1]["TTL_CUST_DISC"]),
            "PROMO_DISC": str(ttl_details[1]["TTL_PROMO_DISC"]),
            "RP_ID": None,
            "REMARK": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45)),
            "STATUS": 'P',
            "CUST_TYPE": cust_response['TYPE']['ID'],
            "ORDER_TXNTYPE":txn_type,
            "SAMPLE_ID":sample_id
        }
        if BuiltIn().get_variable_value(self.SO_ID) and BuiltIn().get_variable_value('${action}') == 'update':
            payload['ID'] = BuiltIn().get_variable_value(self.SO_ID)
        return payload

    def so_products(self, prd_info):
        prd_payload = []
        count = 0
        for prd in prd_info:
            if prd['PRD_SLSTYPE']=='P':
                prd['GROSS_AMT'] = 0.0000
                prd['PROMO_DISC'] = 0.0000
                prd['CUST_DISC'] = 0.0000
                prd['NET_AMT'] = 0.0000
                prd['NET_TTL_TAX'] = 0.0000
                prd['TOTAL_TAX'] = 0.0000
            prd_def_uom = None
            print("PRODUCT INFO HERE : " , prd)
            count = count + 1
            tax_ind = False
            if prd['TAXABLE_AMT'] != 0:
                tax_ind = True
            prod_details = ProductGet.ProductGet().user_retrieves_prd_by_prd_code(prd['PRD_CODE'])
            prod_hier = prod_details['HIERARCHY_LEVEL_1']

            for i in prod_details:
                print(i)
                if 'HIERARCHY_LEVEL' in i and prod_details[i] is not None:
                    print("output", prod_details[i])
                    prod_hier = prod_details[i]
                    break

            for item in prd['PRD_UOM']:
                print("uom item",item)
                if item['CONV_FACTOR'] == 1 :
                    prd_def_uom = item['UOM_ID']
                    print(prd['PRD_CODE'] , "default ", prd_def_uom)
            for uom in prd['PRD_UOM']:

                if int(uom['QTY']) > 0:

                    payload = {
                        "PRD_ID": ProductGet.ProductGet().user_retrieves_prd_by_prd_code(prd['PRD_CODE'])['ID'],
                        "PRD_INDEX": count,
                        "ORDPRD_INDEX": count,
                        "PRD_SLSTYPE": prd['PRD_SLSTYPE'],
                        "PROCESS_ERROR": None,
                        "PRD_HEIR_ID": prod_hier,
                        "UOM_ID": uom['UOM_ID'],
                        "TAX_IND": tax_ind,
                        "DEF_UOM_ID": prd_def_uom,
                        "PRD_QTY": uom['QTY'],
                        "MRP": "0.00",
                        "DISCOUNT": prd['DISCOUNT'],
                        "GRPDISC_AMT": prd['GRPDISC_AMT'],
                        "GRPDISC_ID": prd['GRPDISC_ID'],
                        "PRD_LISTPRC": str(prd['UNIT_PRICE']),
                        "PRD_DISC": str(prd['CUST_DISC']),
                        "UOM_LISTPRC": str(uom['PRD_LISTPRC_UOM']),
                        "GROSS_AMT": str(prd['GROSS_AMT']),
                        "PROMO_DISC": str(prd['PROMO_DISC']),
                        "NET_AMT": str(prd['NET_AMT']),
                        "NET_AMT_TAX": str(prd['NET_TTL_TAX']),
                        "CUST_DISC": str(prd['CUST_DISC']),
                        "TAX_AMT": str(prd['TOTAL_TAX']),
                        "INV_FLAG": 0,
                        "REMARKS": '',
                        "INV_DISC": str(prd['CUST_DISC']),
                        "HSN_CD": None
                        }
                    prd_payload.append(payload)
        return prd_payload

    def so_tax(self, prd_info):
        tax_list = []
        count = 0
        for prd in prd_info:
            if 'TAX_SETTING' not in prd:
                continue
            count = count + 1
            payload = {
                    "PRD_INDEX": count,
                    "PRD_ID": ProductGet.ProductGet().user_retrieves_prd_by_prd_code(prd['PRD_CODE'])['ID'],
                    "UOM_ID": prd['PRD_UOM'][0]['UOM_ID'],
                    "UNIT_TAX": str(prd['TOTAL_TAX']),
                    "TAX_AMT": str(prd['TOTAL_TAX']),
                    "TAX_ID": prd['TAX_SETTING']['ID'],
                    "TAX_PERC": prd['TAX_SETTING']['TAX_RATE'],
                    "APPLY_SEQ": str(prd['TAX_SETTING']['SEQ_NO']),
                    "TAXABLE_AMT": str(prd['TAXABLE_AMT'])
            }
            tax_list.append(payload)
        return tax_list

    def so_groupdisc(self, prd_info):
        groupdisc_list = []
        count = 0
        ttl_amount = 0
        grpdisc = BuiltIn().get_variable_value("${res_grpdisc}")
        store_rounding = BuiltIn().get_variable_value("${store_rounding}")
        if grpdisc is not None :
            for disc in grpdisc:
                for prd in prd_info:
                    count = count + 1
                    prd_id = ProductGet.ProductGet().user_retrieves_prd_by_prd_code(prd['PRD_CODE'])['ID']
                    if disc['PRD_ID'] == prd_id :
                        amount = round(float(disc['DISCOUNT'])/100*(prd['GROSS_AMT']), store_rounding)
                        payload = {
                                "PRD_INDEX": count,
                                "PRD_ID": ProductGet.ProductGet().user_retrieves_prd_by_prd_code(prd['PRD_CODE'])['ID'],
                                "UOM_ID": prd['PRD_UOM'][0]['UOM_ID'],
                                "APPLY_ON": disc['APPLY_ON'],
                                "DISCOUNT": disc['DISCOUNT'],
                                "DISC_TYPE": disc['DISC_TYPE'],
                                "GRPDISC_AMT": str(amount),
                                "GRPDISC_ID": disc['GRPDISC_ID']
                        }
                        ttl_amount = ttl_amount + amount
                        BuiltIn().set_test_variable("${ttl_groupdisc}", ttl_amount)
                        groupdisc_list.append(payload)
            BuiltIn().set_test_variable("${payload_groupdisc}", payload)
        else :
            BuiltIn().set_test_variable("${ttl_groupdisc}", 0.0000)
        return groupdisc_list

    def so_payload(self, so_header, so_prd, so_tax, so_groupdisc):
        if so_groupdisc is None :
            so_groupdisc = []
        payload = {
            "TXN_HEADER": so_header,
            "TXN_PRODUCT": so_prd,
            "TXN_PROMO": [],
            "TXN_FOC_ALLOCATE": [],
            "TXN_PRDTAX": so_tax,
            "QPS_PRODUCT": [],
            "PRODUCT_CUSTGRP_DISC": so_groupdisc
        }
        prd_details = BuiltIn().get_variable_value(self.SO_BODY_DETAILS)
        if prd_details:
            payload['TXN_PRODUCT'][0].update((k, v) for k, v in prd_details.items())
        payload = json.dumps(payload)
        return payload

    @keyword("user POST ${data_type} sales order as prerequisite")
    def user_post_sales_order_as_prerequisite(self, data_type):
        details = BuiltIn().get_variable_value("${SODetailsPre}")
        user_role = BuiltIn().get_variable_value("${user_role}")
        TokenAccess.TokenAccess().user_retrieves_token_access_as(user_role)
        DistributorGet.DistributorGet().user_gets_distributor_by_using_code(details['distributor'])
        RouteGet.RouteGet().user_gets_route_by_using_code(details['route'])
        CustomerGet.CustomerGet().user_gets_cust_by_using_code(details['customer'])
        CustomerGet.CustomerGet().user_gets_customer_shipto_by_desc(details['shipTo'])
        whs = WarehouseGet.WarehouseGet().user_gets_warehouse_by_using_data("WHS_CD:{0}".format(details['warehouse']))
        BuiltIn().set_test_variable(self.WAREHOUSE_ID, whs[0])
        ProductGet.ProductGet().user_retrieves_prd_by_prd_code(details['product'])
        if details['PRIME_FLAG'] == "Prime":
            so_header_details = {"PRIME_FLAG": "PRIME"}
        else:
            so_header_details = {"PRIME_FLAG": "NON_PRIME"}
        BuiltIn().set_test_variable(self.SO_HEADER_DETAILS, so_header_details)
        self.user_creates_sales_order("Fixed")
