from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.Config.ReferenceData.ReasonType import ReasonTypeGet
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json

END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL


class CustomerTransferPost(object):

    @keyword('user creates customer transfer using ${data} data')
    def user_creates_customer_transfer(self, data):
        url = "{0}customer-transfer".format(END_POINT_URL)
        payload = self.transfer_payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, json.dumps(payload))
        if response.status_code == 201:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${transfer_id}", body_result['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def transfer_payload(self):
        transfer_details = BuiltIn().get_variable_value("${transfer_details}")
        from_dist_id = DistributorGet.DistributorGet().user_gets_distributor_by_using_code(
            transfer_details['FROM_DIST'])
        to_dist_id = DistributorGet.DistributorGet().user_gets_distributor_by_using_code(transfer_details['TO_DIST'])
        reason_id = ReasonTypeGet.ReasonTypeGet().user_gets_reason_by_using_code(transfer_details['REASON'], "PCT")
        payload = {
            "FROM_DIST_ID": from_dist_id,
            "TO_DIST_ID": to_dist_id,
            "REASON": reason_id,
            "STATUS": "O"
        }
        return payload
