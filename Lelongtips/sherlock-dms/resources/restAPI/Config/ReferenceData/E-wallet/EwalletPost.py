from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import secrets
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL

class EwalletPost(object):
    """ Functions to create e-wallet """

    @keyword('user creates ewallet type with ${data_type}')
    def user_creates_ewallet_type_with(self):
        url = "{0}e-wallet".format(END_POINT_URL)
        payload = self.payload_ewallet()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            res_bd_ewallet_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_ewallet_id}", res_bd_ewallet_id)
            BuiltIn().set_test_variable("${res_bd_ewallet}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_ewallet(self):
        payload = {
            "EWALLET_CD": 'EW2020' + str(secrets.choice(range(1, 99))),
            "EWALLET_DESC":  ''.join(secrets.choice('EFGHIJKLMNOPQRSTUVWXYZ') for _ in range(40))
        }
        details = BuiltIn().get_variable_value("${ewallet_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("ewallet Payload: ", payload)
        return payload