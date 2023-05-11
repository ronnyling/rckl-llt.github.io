import json
import datetime
from resources import TransactionFormula
from resources.restAPI.Config.ReferenceData.ReasonType import ReasonTypeGet
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.MasterDataMgmt.Product import ProductGet, ProductPut
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route import RouteGet
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod, TokenAccess
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from setup.hanaDB import HanaDB
from datetime import date, datetime, timedelta


END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class DebitNoteProductPost(object):

    @keyword('user creates debit note with ${data_type} data')
    def user_creates_debit_note(self, data_type):
        url = "{0}debitnote".format(END_POINT_URL)
        payload = self.payload_debit_note("creates")

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print("POST Status code for debit_note_product is " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.text)
        if response.status_code != 201:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            res_bd_debit_note_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_debit_note_id}", res_bd_debit_note_id)
            # res_bd_debit_note_id = str(res_bd_debit_note_id).replace(":", "").replace("-", "")
            # HanaDB.HanaDB().connect_database_to_environment()
            # result_header = HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM TXN_DBN WHERE ID = '{0}'"
            #                                                             .format(res_bd_debit_note_id), 1)
            # result_body = HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM TXN_DBNPRD WHERE TXN_ID = '{0}'"
            #                                                           .format(res_bd_debit_note_id), 1)
            # HanaDB.HanaDB().disconnect_from_database()
            # assert result_header and result_body, "Record not found in database"
            print(body_result)

    def payload_debit_note(self, action):
        route_id = BuiltIn().get_variable_value("${route_id}")
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        header_details = BuiltIn().get_variable_value("${dn_header_details}")
        prime_flag = header_details['PRIME_FLAG']
        TransactionFormula.TransactionFormula().tran_calculation_for_gross_and_cust_disc(prime_flag, header_details['CUST'], 'No', header_details['PROD_ASS_DETAILS'])
        prd_info = BuiltIn().get_variable_value("${prd_info}")
        if prime_flag == 'PRIME':
            TransactionFormula.TransactionFormula().tax_calculation_for_multi_product()
        ttl_details = TransactionFormula.TransactionFormula().calculation_for_product_total(prd_info)

        TokenAccess.TokenAccess().get_token_by_role('distadm')
        amount = TransactionFormula.TransactionFormula().rounding_based_on_setup(ttl_details[1]["TTL_NET"])
        payload = {
            "DIST_ID": dist_id,
            "CUST_ID": cust_id,
            "TXN_DT": date.today().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "PRIME_FLAG": prime_flag,
            "ROUTE_ID": route_id,
            "CUST_TAX_IND": True,
            "PRD_RELATED": True,
            "STATUS": "D",
            "INVTERM_ID": "E6FC108E:214DBCB9-18BA-406F-B649-39070E178FFB",
            "REF_DOC_TYPE": None,
            "REF_DOC_NO": None,
            "REF_DOC_ID": None,
            "BILLTO_ID": "B7BA0A51:1E2846DA-4C07-4185-BBB1-C07A5F48C9EB",
            "REASON_ID": reason_id,
            "GROSS_TTL": ttl_details[1]["TTL_GROSS"],
            "TAX_TTL": ttl_details[1]["TTL_TAX"],
            "NET_TTL": ttl_details[1]["TTL_GROSS"],
            "NET_TTL_TAX": ttl_details[1]["TTL_NET"],
            "ADJ_AMT": amount[1],
            "TAXABLE_AMT": ttl_details[1]["TTL_TAXABLE"],
            "NONTAXABLE_AMT": ttl_details[1]["TTL_NONTAXABLE"],
            "REF_DOC_ORI_NET_TTL": 0,
            "RP_ID": None,
            "DUE_DT": (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "PRODUCTS": ttl_details[0]
        }
        if action == 'updates':
            payload.update({"VERSION": 1})
        payload = json.dumps(payload)
        print("Payload is {0}".format(payload))
        return payload

    @keyword("user creates ${dn_type} debit note as prerequisite")
    def user_creates_debit_note_as_prerequisite(self, dn_type):
        TokenAccess.TokenAccess().user_retrieves_token_access_as('hqadm')
        CustomerGet.CustomerGet().user_gets_cust_by_using_code('CT0000001549')
        if dn_type == "Prime":
            ProductGet.ProductGet().user_retrieves_prd_by_prd_code('A1001')
            update_product_details = {
                "STATUS": "Active",
                "SELLING_IND": "1"
            }
            BuiltIn().set_test_variable("${update_product_details}", update_product_details)
            BuiltIn().set_test_variable("${user_role}", 'hqadm')
            ProductPut.ProductPut().user_updates_product("fixed")
            BuiltIn().set_test_variable("${user_role}", 'distadm')
        else:
            ProductGet.ProductGet().user_retrieves_prd_by_prd_code('testNp123')
        DistributorGet.DistributorGet().user_gets_distributor_by_using_code('DistEgg')

        TokenAccess.TokenAccess().user_retrieves_token_access_as('distadm')
        RouteGet.RouteGet().user_gets_route_by_using_code('Rchoon')
        ReasonTypeGet.ReasonTypeGet().user_gets_reason_by_using_code('JunReasonTypeCode', 'DN')
        details = {
            "CUST": "CXTESTTAX",
            "PRIME_FLAG": dn_type.upper(),
            "PROD_ASS_DETAILS":[{
                "PRD_CODE": "A1001",
                "PRD_UOM": [{
                    "UOM": "EA",
                    "QTY": 3
                }]
            }]
        }
        BuiltIn().set_test_variable("${dn_header_details}", details)
        TokenAccess.TokenAccess().user_retrieves_token_access_as('distadm')
        self.user_creates_debit_note("Fixed")
