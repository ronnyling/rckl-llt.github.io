from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json

END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL


class CustomerTransferProcess(object):

    @keyword('user cancels created customer transfer')
    def user_cancels_customer_transfer(self):
        transfer_id = BuiltIn().get_variable_value("${transfer_id}")
        url = "{0}customer-transfer/{1}".format(END_POINT_URL, transfer_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword('user confirms created customer transfer')
    def user_confirms_customer_transfer(self):
        url = "{0}customer-transfer-validation-scheduler".format(END_POINT_URL)
        payload = self.confirm_payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, json.dumps(payload))
        if response.status_code == 202:
            body_result = response.json()
            print("Body Result: ", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def confirm_payload(self):
        transfer_id = BuiltIn().get_variable_value("${transfer_id}")
        payload = {
            "ACTION_LABEL": "SAVE_AND_CONFIRM",
            "CUST_TRANSFER_ID": transfer_id
        }
        return payload
