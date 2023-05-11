import json
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class TransferReasonPut(object):
    @keyword("user puts to transfer reason")
    def user_puts_to_transfer_reason(self):
        tr_id = BuiltIn().get_variable_value("${tr_id}")
        url = "{0}trade-asset/transfer-reason/{1}".format(END_POINT_URL, tr_id)
        common = APIMethod.APIMethod()
        payload = self.gen_transfer_reason_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print("payload " + str(payload))
        return str(response.status_code), response.json()

    def gen_transfer_reason_payload(self):
        tr_details = BuiltIn().get_variable_value("${tr_details}")
        keys_to_remove = []
        for i in tr_details.keys():
            if i != "TFREASON_DESC":
                keys_to_remove.append(i)
        for j in keys_to_remove:
            tr_details.pop(j)
        payload = tr_details
        return payload
