import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, TokenAccess
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.Config.ReferenceData.ReasonType import ReasonTypeGet
from resources.restAPI.MasterDataMgmt.Warehouse import WarehouseGet
from resources.TransactionFormula import TransactionFormula
from resources.restAPI.Merchandising.PosmManagement.PosmInstallation import PosmInstallationPost
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json

END_POINT_URL = PROTOCOL + "posm-management" + APP_URL


class PosmRemovalPost(object):

    @keyword('user creates posm direct removal using ${data} data')
    def user_creates_posm_removal(self, data):
        url = "{0}posm-removal/".format(END_POINT_URL)
        posm_details = BuiltIn().get_variable_value("${posm_details}")
        dist_id = DistributorGet.DistributorGet().user_gets_distributor_by_using_code(posm_details['DIST'])
        unit_price = TransactionFormula().calculate_posm_prd_net(posm_details['PRODUCT'])
        header = self.posm_removal_header_payload(posm_details, dist_id, unit_price)
        prd = PosmInstallationPost.PosmInstallationPost().posm_prd_payload(posm_details, unit_price)
        payload = self.posm_removal_payload(header, prd)
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        common = APIMethod.APIMethod()
        print("loadload",payload)
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body = response.json()
        try:
            print("Result: ", response.json())
            BuiltIn().set_test_variable("${res_body}", response.json())
            BuiltIn().set_test_variable("${direct_removal_id}", body['TXN_HEADER']['ID'])
        except IOError:
            print("ResultFail: ", response.status_code)
        BuiltIn().set_test_variable("${status_code}", response.status_code)


    def posm_removal_header_payload(self, posm_details, dist_id, unit_price):
        prd = posm_details['PRODUCT'].split(":")
        header = {
             "DIST_ID": dist_id,
            "CUST_ID": CustomerGet.CustomerGet().user_retrieves_cust_name(posm_details['CUST'])['ID'],
            "REQ_REASON_ID": ReasonTypeGet.ReasonTypeGet().user_gets_reason_by_using_code(posm_details['REASON'], "POSM_REM"),
            "WHS_ID": WarehouseGet.WarehouseGet().user_retrieves_warehouse_by_using_code(posm_details['WAREHOUSE']),
            "NET_TTL": (int(unit_price) * int(prd[1])),
            "TXN_TYPE": "WOR",
            "POSM_CAT": "D",
            "POSM_STOCK_TYPE": "G"

        }
        return header


    def posm_removal_payload(self, txn_header, txn_prd):
        payload = {
            "TXN_HEADER": txn_header,
            "TXN_PRODUCT": [
                txn_prd
            ]
        }
        payload = json.dumps(payload)
        return payload
