from resources.restAPI.Config.ReferenceData.ReasonType import ReasonWarehousePost, ReasonWarehouseGet
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.MasterDataMgmt.Product import ProductGet, ProductUomGet
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route import RouteGet
from resources.restAPI.CustTrx.SalesOrder import SalesOrderPost
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod, TokenAccess
from resources.TransactionFormula import TransactionFormula
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from setup.hanaDB import HanaDB
import urllib3
import secrets
import json

urllib3.disable_warnings()
END_POINT_URL = PROTOCOL + "return" + APP_URL


class SalesReturnPost(object):

    @keyword('user post return with ${data_type} data')
    def user_post_return_with_data(self, data_type):
        url = "{0}return".format(END_POINT_URL)
        payload = self.payload_return()
        user = BuiltIn().get_variable_value("${user_role}")
        TokenAccess.TokenAccess().get_token_by_role(user)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        print(response.text)
        if response.status_code != 200:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            res_bd_return_id = body_result['TXN_HEADER']['ID']
            res_bd_return_no = body_result['TXN_HEADER']['TNOTE_NO']
            rtn_type = body_result['TXN_HEADER']['PRIME_FLAG']
            BuiltIn().set_test_variable("${res_bd_return_id}", res_bd_return_id)
            BuiltIn().set_test_variable("${res_bd_return_no}", res_bd_return_no)
            BuiltIn().set_test_variable("${return_rs_bd}", body_result)
            BuiltIn().set_test_variable("${rtn_type}", rtn_type)
            # res_bd_return_id = str(res_bd_return_id).replace(":", "").replace("-", "")
            # HanaDB.HanaDB().connect_database_to_environment()
            # result_header = HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM TXN_NOTEHDR where ID = '{0}'"
            #                                                             .format(res_bd_return_id), 1)
            # result_body = HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM TXN_NOTEPRD where TXN_ID = '{0}'"
            #                                                           .format(res_bd_return_id), 1)
            # HanaDB.HanaDB().disconnect_from_database()
            # assert result_header and result_body, "Record not found in database"
            print(body_result)

    @keyword('update return to draft status')
    def update_return_to_draft_return(self):
        txn_id = COMMON_KEY.convert_id_to_string(BuiltIn().get_variable_value("${res_bd_return_id}"))
        HanaDB.HanaDB().connect_database_to_environment()
        update_hdr_query = "UPDATE TXN_NOTEHDR SET STATUS = 'T' where ID = '{0}'".format(txn_id)
        update_prd_query = "UPDATE TXN_NOTEPRD SET GROSS_AMT = null, NET_AMT = null, NET_AMT_TAX = NULL, " \
                           "TAX_AMT = null WHERE TXN_ID = '{0}'".format(txn_id)
        HanaDB.HanaDB().execute_sql_string(update_hdr_query)
        HanaDB.HanaDB().execute_sql_string(update_prd_query)
        HanaDB.HanaDB().disconnect_from_database()

    def payload_return(self):
        route_id = BuiltIn().get_variable_value("${route_id}")
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        rp_id = BuiltIn().get_variable_value("${rp_id}")

        header_details = BuiltIn().get_variable_value("${rtn_header_details}")
        prd_asg_details = BuiltIn().get_variable_value("${rtn_header_details['PROD_ASS_DETAILS']}")
        rtn_id = BuiltIn().get_variable_value("${rtn_header_details['ID']}")
        if header_details:
            principal = header_details['PRIME_FLAG']
        else:
            principal = secrets.choice(["PRIME", "NON_PRIME"])
        if principal == "PRIME":
            whs_id = BuiltIn().get_variable_value("${WAREHOUSE_ID}")
        else:
            whs_id = BuiltIn().get_variable_value("${WAREHOUSE_ID_NP}")
        if not prd_asg_details or rtn_id:
            BuiltIn().set_test_variable("${fixedData}", header_details)
            prd_id = BuiltIn().get_variable_value("${prd_id}")
            prd_cd = BuiltIn().get_variable_value("${prd_cd}")
            uom = ProductUomGet.ProductUomGet().user_retrieves_prd_uom(prd_id)
            rand_uom = uom[0]['UOM_CD'] + ":" + str(secrets.choice(range(1, 10)))
            header_details = TransactionFormula().user_intends_to_insert_product_with_uom(prd_cd, rand_uom)
        TransactionFormula().tran_calculation_for_gross_and_cust_disc(principal,
                                                header_details['CUST'], 'percent', header_details['PROD_ASS_DETAILS'])

        prd_info = BuiltIn().get_variable_value("${prd_info}")
        prd_info[0]['NET_TTL_TAX'] = prd_info[0]['GROSS_AMT']
        prd_info[0]['TOTAL_TAX'] = "0.0000"
        if principal == 'PRIME':
            TransactionFormula().tax_calculation_for_multi_product()
        prd_info = BuiltIn().get_variable_value("${prd_info}")
        print("ADE PROD TAX!! ", prd_info)
        prd_id = BuiltIn().get_variable_value("${prd_id}")
        ttl_details = TransactionFormula().calculation_for_product_total(prd_info)
        TokenAccess.TokenAccess().get_token_by_role('distadm')
        amount = TransactionFormula().rounding_based_on_setup(ttl_details[1]["TTL_NET"])
        BuiltIn().set_test_variable("${res_bd_cust_id}", cust_id)
        cust_response = CustomerGet.CustomerGet().user_retrieves_cust_by_id()
        grpdisc_list = SalesOrderPost.SalesOrderPost().so_groupdisc(prd_info)
        ttl_groupdisc = BuiltIn().get_variable_value("${ttl_groupdisc}")

        if "INV_ID" in header_details:
            inv_id = header_details['INV_ID']
        else:
            inv_id = None

        payload = {
            "TXN_HEADER": {
                "TXN_DT": COMMON_KEY.get_local_time(),
                "ROUTE_ID": route_id,
                "RP_ID": rp_id,
                "WHS_ID": None,
                "CUST_ID": cust_id,
                "STOCK_MOVEMENT": "A",
                "FULL_IND": False,
                "CN_TYPE": "G",
                "INV_ID": inv_id,
                "CLAIMABLE_IND": False,
                "REASON_ID": None,
                "REMARK": None,
                "STATUS": "P",
                "NET_TTL": str(ttl_details[1]["TTL_GROSS"]),
                "NET_TTL_TAX": str(ttl_details[1]["TTL_NET"]),
                "PRD_DISC_TTL": "0.0000",
                "CUST_DISC_PERC": cust_response["CUST_DISC"],
                "CUST_DISC_AMT": str(ttl_details[1]["TTL_CUST_DISC"]),
                "GROSS_TTL": str(ttl_details[1]["TTL_GROSS"]),
                "TAX_TTL": str(ttl_details[1]["TTL_TAX"]),
                "ADJ_AMT": str(amount[1]),
                "PRIME_FLAG": principal,
                "GRPDISC_AMT": ttl_groupdisc
            },
            "TXN_PRODUCT": [
                {
                    "PRD_ID": prd_id,
                    "PRD_INDEX": 1,
                    "PRD_SLSTYPE": "S",
                    "UOM_ID": prd_info[0]['PRD_UOM'][0]['UOM_ID'],
                    "UOM_DESC": "D01",
                    "DEF_UOM_ID": prd_info[0]['PRD_UOM'][0]['UOM_ID'],
                    "PRD_UOM_ID": prd_info[0]['PRD_UOM'][0]['UOM_ID'],
                    "PRICE_EA": str(prd_info[0]['UNIT_PRICE']),
                    "UOM_LISTPRC": str(prd_info[0]['PRD_UOM'][0]['PRD_LISTPRC_UOM']),
                    "PRD_LISTPRC": str(prd_info[0]['UNIT_PRICE']),
                    "CONV_UOM": "1",
                    "DEF_CONV_UOM": "1",
                    "GROSS_AMT": str(prd_info[0]['GROSS_AMT']),
                    "INV_ID": inv_id,
                    "INV_NO": None,
                    "PRD_DISC": "0.0000",
                    "PROMO_DISC": "0.0000",
                    "DISC_AMT": "0.0000",
                    "CUST_DISC": str(prd_info[0]['CUST_DISC']),
                    "INV_DISC": "0.0000",
                    "INVPRD_INDEX": 1,
                    "HSN_CD": "",
                    "WHS_ID": whs_id,
                    "REASON_ID": reason_id,
                    "PRD_QTY": int(prd_info[0]['PRD_UOM'][0]['QTY']),
                    "NET_AMT_TAX": str(prd_info[0]['NET_TTL_TAX']),
                    "TAX_AMT": str(prd_info[0]['TOTAL_TAX']),
                    "NET_AMT": str(prd_info[0]['GROSS_AMT']),
                    "TAX_VAL": 0,
                    "GRPDISC_AMT": str(prd_info[0]['GRPDISC_AMT']),
                    "GRPDISC_ID": prd_info[0]['GRPDISC_ID']
                }
            ],
            "TXN_PRDTAX": [],
            "TXN_PRDBIN": [],
            "TXN_INVBAL_PRD": [],
            "TXN_INVBAL_PROMO": [],
            "TXN_INVBAL_PROMO_FOC": [],
            "TXN_NOTEPROMO": [],
            "TXN_NOTEPROMO_FOC": [],
            "TXN_NOTEPROMO_QPS_PRD": [],
            "TXN_NOTEPRD_CUSTGRP_DISC": grpdisc_list
        }
        rtn_status = BuiltIn().get_variable_value("${rtn_status}")
        if rtn_status:
            payload['TXN_HEADER'].update({"STATUS": rtn_status})
        if rtn_id:
            payload['TXN_HEADER']['ID'] = rtn_id
        payload = json.dumps(payload)
        print("Payload: ", payload)
        return payload

    @keyword("user creates ${rtn_type} return as prerequisite")
    def user_creates_return_as_prerequisite(self, rtn_type):
        details=BuiltIn().get_variable_value("${RtnDetailsPre}")
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        DistributorGet.DistributorGet().user_gets_distributor_by_using_code(details['distributor'])
        RouteGet.RouteGet().user_gets_route_by_using_code(details['route'])
        CustomerGet.CustomerGet().user_gets_cust_by_using_code(details['customer'])
        TokenAccess.TokenAccess().user_retrieves_token_access_as('distadm')
        ReasonWarehousePost.ReasonWarehousePost().user_creates_prerequisite_for_reason(details['reasontype'])
        ReasonWarehousePost.ReasonWarehousePost().user_assigns_warehouse_to_reason('both')
        ReasonWarehouseGet.ReasonWarehouseGet().user_retrieves_reason_warehouse()
        ProductGet.ProductGet().user_retrieves_prd_by_prd_code(details['product'])
        cust_name = BuiltIn().get_variable_value("${cust_name}")
        if rtn_type == "Prime":
            rtn_header_details = {"PRIME_FLAG": "PRIME", "CUST": cust_name}
        else:
            rtn_header_details = {"PRIME_FLAG": "NON_PRIME", "CUST": cust_name}
        BuiltIn().set_test_variable("${rtn_header_details}", rtn_header_details)
        BuiltIn().set_test_variable("${rtn_type}", rtn_header_details["PRIME_FLAG"])
        TokenAccess.TokenAccess().user_retrieves_token_access_as('distadm')
        self.user_post_return_with_data("Fixed")
