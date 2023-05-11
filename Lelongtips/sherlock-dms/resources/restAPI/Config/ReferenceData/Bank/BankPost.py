import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class BankPost(object):
    @keyword('user creates bank using ${data} data')
    def user_creates_bank(self, data):
        url = "{0}bank".format(END_POINT_URL)
        payload = self.bank_payload(data)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body = response.json()
        try:
            print("Result: ", response.json())
            BuiltIn().set_test_variable("${res_body}", response.json())
            BuiltIn().set_test_variable("${bank_id}", body['ID'])
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @staticmethod
    def bank_payload(data):
        char_num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        payload = {
            'CODE': ''.join(secrets.choice(char_num) for _ in range(15)),
            'BANK_DESC': ''.join(secrets.choice(char_num) for _ in range(30)),
        }
        if data == 'fix':
            details = BuiltIn().get_variable_value("&{bank_details}")
            payload.update((k, v) for k, v in details.items())
        BuiltIn().set_test_variable("${payload}", payload)
        dump_payload = json.dumps(payload)
        return dump_payload
