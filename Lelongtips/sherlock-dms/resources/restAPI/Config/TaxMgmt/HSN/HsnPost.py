import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json

END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class HsnPost(object):

    @keyword('user creates hsn using ${data} data')
    def user_creates_hsn(self, data):
        url = "{0}hsn-master/".format(END_POINT_URL)
        payload = self.hsn_payload(data)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body = response.json()
        try:
            print("Result: ", response.json())
            BuiltIn().set_test_variable("${res_body}", response.json())
            BuiltIn().set_test_variable("${hsn_id}", body['ID'])
        except IOError:
            print("ResultFail: ", response.status_code)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def hsn_payload(self, data):
        payload = {
            "HSN_CODE": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8)),
            "HSN_DESCRIPTION": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15)),
        }
        if data == 'fixed':
            details = BuiltIn().get_variable_value("&{hsn_details}")
            payload.update((k, v) for k, v in details.items())
        BuiltIn().set_test_variable("${payload}", payload)
        payload = json.dumps(payload)
        return payload