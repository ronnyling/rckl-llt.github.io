from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, TokenAccess
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.Config.ReferenceData.ReasonType import ReasonTypeGet
from resources.TransactionFormula import TransactionFormula
from resources.restAPI.Merchandising.PosmManagement.PosmInstallation import PosmInstallationPost
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json

END_POINT_URL = PROTOCOL + "posm-management" + APP_URL


class PosmRequestPost(object):

    @keyword('user creates posm request using ${data} data')
    def user_creates_posm_request(self, data):
        url = "{0}posm-request-header".format(END_POINT_URL)
        posm_details = BuiltIn().get_variable_value("${posm_details}")
        dist_id = DistributorGet.DistributorGet().user_gets_distributor_by_using_code(posm_details['DIST'])
        unit_price = TransactionFormula().calculate_posm_prd_net(posm_details['PRODUCT'])
        posm_category = posm_details['CATEGORY']
        header = self.posm_request_header_payload(posm_details, dist_id, unit_price, posm_category)
        prd = PosmInstallationPost.PosmInstallationPost().posm_prd_payload(posm_details, unit_price)
        payload = self.posm_request_payload(header, prd)
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, json.dumps(payload))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        payload['TXN_PRODUCT'][0]['APPR_QTY'] = payload['TXN_PRODUCT'][0]['REQ_QTY']
        BuiltIn().set_test_variable("${request_payload}", payload)
        body = response.json()
        try:
            print("Result: ", response.json())
            BuiltIn().set_test_variable("${res_body}", response.json())
            BuiltIn().set_test_variable("${request_id}", body['TXN_HEADER']['ID'])
        except IOError:
            print("ResultFail: ", response.status_code)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def posm_request_header_payload(self, posm_details, dist_id, unit_price, posm_category):
        prd = posm_details['PRODUCT'].split(":")
        if posm_category == "Principal":
            posm_cat = "P"
        else:
            posm_cat = "T"
        request_type = posm_details['REQUEST']
        if request_type == "New Installation":
            req_type = "POSM_INS"
        elif request_type == "Maintenance":
            req_type = "POSM_MAI"
        else:
            req_type = "POSM_REM"
        print("REQ TYPE = ", req_type)
        ReasonTypeGet.ReasonTypeGet().user_gets_reason_by_using_code(posm_details['REASON'], req_type)
        reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        header = {
            "REQ_TYPE": req_type,
            "DIST_ID": dist_id,
            "CUST_ID": CustomerGet.CustomerGet().user_retrieves_cust_name(posm_details['CUST'])['ID'],
            "POSM_CAT": posm_cat,
            "REQ_REASON": reason_id,
            "TXN_STATUS": "O",
            "NET_TTL": (int(unit_price) * int(prd[1]))
        }
        return header

    def posm_request_payload(self, txn_header, txn_prd):
        payload = {
            "TXN_HEADER": txn_header,
            "TXN_PRODUCT": [
                txn_prd
            ]
        }
        return payload
