import json
import datetime
import secrets

from resources.restAPI.Config.ReferenceData.ReasonType import ReasonWarehousePost, ReasonWarehouseGet
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.MasterDataMgmt.Product import ProductUomGet, ProductGet
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route import RouteGet
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod, TokenAccess
from resources.TransactionFormula import TransactionFormula
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn

import urllib3
from setup.hanaDB import HanaDB

urllib3.disable_warnings()

END_POINT_URL = PROTOCOL + "credit-note" + APP_URL


class CreditNoteProductPost(object):

    CN_HEADER = "${cn_header_details}"
    PRD_ID = "${prd_id}"

    @keyword('user creates credit note with ${data_type} data')
    def user_creates_credit_note(self, data_type):

        url = "{0}credit-note-prd".format(END_POINT_URL)
        payload = self.payload_credit_note(data_type)
        payload = json.dumps(payload)
        print(payload)
        common = APIMethod.APIMethod()
        user = BuiltIn().get_variable_value("${user_role}")
        TokenAccess.TokenAccess().get_token_by_role(user)
        response = common.trigger_api_request("POST", url, payload)
        print("POST Status code for credit_note_product is " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.text)
        if response.status_code != 200:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            res_bd_credit_note_id = body_result['TXN_HEADER']['ID']
            BuiltIn().set_test_variable("${res_bd_credit_note_id}", res_bd_credit_note_id)
            # res_bd_credit_note_id = str(res_bd_credit_note_id).replace(":", "").replace("-", "")
            # HanaDB.HanaDB().connect_database_to_environment()
            # result_header = HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM TXN_NOTEHDR where ID = '{0}'"
            #                                                             .format(res_bd_credit_note_id), 1)
            # result_body = HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM TXN_NOTEPRD where TXN_ID = '{0}'"
            #                                                           .format(res_bd_credit_note_id), 1)
            # HanaDB.HanaDB().disconnect_from_database()
            # assert result_header and result_body, "Record not found in database"
            print(body_result)

    def payload_credit_note(self, data_type):
        route_id = BuiltIn().get_variable_value("${route_id}")
        reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        rp_id = BuiltIn().get_variable_value("${rp_id}")
        header_details = BuiltIn().get_variable_value(self.CN_HEADER)
        body_details = BuiltIn().get_variable_value("${cn_body_details}")
        prime = header_details['PRIME_FLAG']

        TransactionFormula().tran_calculation_for_gross_and_cust_disc(prime,
                                                                      header_details['CUST'], 'No',
                                                                      header_details['PROD_ASS_DETAILS'])
        TransactionFormula().tax_calculation_for_multi_product()
        prd_info = BuiltIn().get_variable_value("${prd_info}")
        ttl_details = TransactionFormula().calculation_for_product_total(prd_info)
        TokenAccess.TokenAccess().get_token_by_role('distadm')
        amount = TransactionFormula().rounding_based_on_setup(ttl_details[1]["TTL_NET"])
        cust_response = CustomerGet.CustomerGet().user_retrieves_cust_name(header_details['CUST'])
        prd_id = BuiltIn().get_variable_value(self.PRD_ID)
        payload = {
            "TXN_HEADER": {
                "TXN_DT": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                "PRIME_FLAG": prime,
                "ROUTE_ID": route_id,
                "RP_ID": rp_id,
                "CUST_ID": cust_response['ID'],
                "DIRECT_CUST": secrets.choice([True, False]),
                "REASON_ID": reason_id,
                "INV_ID": None,
                "INV_NO": None,
                "CLAIMABLE_IND": secrets.choice([True, False]),
                "REMARK": "",
                "STATUS": 'P',
                "GROSS_TTL": str(ttl_details[1]["TTL_GROSS"]),
                "NET_TTL": str(ttl_details[1]["TTL_GROSS"]),
                "NET_TTL_TAX": str(ttl_details[1]["TTL_NET"]),
                "TAX_TTL": str(ttl_details[1]["TTL_TAX"]),
                "ADJ_AMT": str(amount[1]),
                "TAXABLE_AMT": str(ttl_details[1]["TTL_TAXABLE"]),
                "NONTAXABLE_AMT": str(ttl_details[1]["TTL_NONTAXABLE"]),
                "CUST_DISC_PERC": str(cust_response['CUST_DISC']),
                "CUST_DISC_AMT": str(ttl_details[1]["TTL_CUST_DISC"]),
                "PRD_DISC_TTL": "0.0000",
                "INV_DISC_TTL": "0.0000"
            },
            "TXN_PRODUCT": [
                {
                    "UOM_ID": prd_info[0]['PRD_UOM'][0]['UOM_ID'],
                    "PRD_ID": prd_id,
                    "REASON_ID": reason_id,
                    "DEF_UOM_ID": prd_info[0]['PRD_UOM'][0]['UOM_ID'],
                    "INV_ID": None,
                    "INV_DISC": "0.0000",
                    "PRD_DISC": "0.0000",
                    "HSN_CD": None,
                    "PRD_INDEX": 1,
                    "INVPRD_INDEX": 1,
                    "MRP": None,
                    "PRD_SLSTYPE": "S",
                    "PRD_QTY": int(prd_info[0]['PRD_UOM'][0]['QTY']),
                    "TAX_AMT": str(prd_info[0]['TOTAL_TAX']),
                    "NET_AMT": str(prd_info[0]['GROSS_AMT']),
                    "TOTAL_DISCAMT": "0.0000",
                    "UOM_LISTPRC": str(prd_info[0]['PRD_UOM'][0]['PRD_LISTPRC_UOM']),
                    "CUST_DISC": str(prd_info[0]['CUST_DISC']),
                    "GROSS_AMT": str(prd_info[0]['GROSS_AMT']),
                    "PROMO_DISC": "0.0000",
                    "PRD_LISTPRC": str(prd_info[0]['UNIT_PRICE']),
                    "NET_AMT_TAX": str(prd_info[0]['NET_TTL_TAX'])
                }
            ],
            "TXN_PRDTAX": []
        }
        if data_type == 'non prime':
            ProductGet.ProductGet().user_retrieves_prd_by_prd_code(header_details['PRD'])
            prd_id = BuiltIn().get_variable_value(self.PRD_ID)
            payload['TXN_PRODUCT'][0]['PRD_ID'] = prd_id
        elif data_type == 'prime':
            payload['TXN_HEADER']['INV_ID'] = header_details['INV_ID']
            payload['TXN_HEADER']['INV_NO'] = header_details['INV_NO']
        if body_details:
            payload['TXN_PRODUCT'][0].update((k, v) for k, v in body_details.items())
        print("CN Payload: ", payload)
        return payload

    @keyword("user creates ${cn_type} credit note as prerequisite")
    def user_creates_credit_note_as_prerequisite(self, cn_type):
        details = BuiltIn().get_variable_value("${CnDetailsPre}")
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        DistributorGet.DistributorGet().user_gets_distributor_by_using_code(details['distributor'])
        RouteGet.RouteGet().user_gets_route_by_using_code(details['route'])
        RouteGet.RouteGet().user_gets_route_plan_by_using_code(details['routeplan'])
        CustomerGet.CustomerGet().user_gets_cust_by_using_code(details['customer'])
        ReasonWarehousePost.ReasonWarehousePost().user_creates_prerequisite_for_reason(details['reasontype'])
        ReasonWarehousePost.ReasonWarehousePost().user_assigns_warehouse_to_reason('both')
        ReasonWarehouseGet.ReasonWarehouseGet().user_retrieves_reason_warehouse()
        cust_name = BuiltIn().get_variable_value("${cust_name}")
        if cn_type == "Prime":
            cn_header_details = {"PRIME_FLAG": "PRIME", "CUST": cust_name}
            BuiltIn().set_test_variable(self.CN_HEADER, cn_header_details)
            ProductGet.ProductGet().user_retrieves_prd_by_prd_code(details['productPrime'])
            prd = details['productPrime']
        else:
            cn_header_details = {"PRIME_FLAG": "NON_PRIME", "CUST": cust_name}
            TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
            BuiltIn().set_test_variable(self.CN_HEADER, cn_header_details)
            ProductGet.ProductGet().user_retrieves_prd_by_prd_code(details['productNPrime'])
            prd = details['productNPrime']
        prd_id = BuiltIn().get_variable_value(self.PRD_ID)
        uom = ProductUomGet.ProductUomGet().user_retrieves_prd_uom(prd_id)
        rand_uom = uom[0]['UOM_CD'] + ":" + str(secrets.choice(range(1, 10)))
        TransactionFormula().user_intends_to_insert_product_with_uom(prd, rand_uom)
        TokenAccess.TokenAccess().user_retrieves_token_access_as('distadm')
        self.user_creates_credit_note("Fixed")
