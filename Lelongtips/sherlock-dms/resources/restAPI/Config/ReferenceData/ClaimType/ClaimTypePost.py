from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import secrets
import json
import ast
import re
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class ClaimTypePost(object):

    @keyword('user creates ${status} claim type with ${data_type} data')
    def user_creates_claim_type_with_data(self, status, data_type):
        url = "{0}claim-type/".format(END_POINT_URL)
        payload = self.payload_claim()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            response_dict = json.loads(response.text)
            print("Result: ", response_dict)
            BuiltIn().set_test_variable("${claim_type_id}", response_dict['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return payload

    def payload_claim(self):    # make use of random string values with specified word limit, will be replaced by data from &{claim_type_details} if it is not null
        payload = \
            {
                'CLAIM_TYPE_CD': ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(12)),
                'CLAIM_TYPE_DESC': ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
                'TYPE': {"ID": "CF4FFF42:FB22915F-4C75-454F-B4D4-60BF24684D12"},
                'VERSION': 1
            }   # random type ID will cause error 409 request conflict

        details = BuiltIn().get_variable_value("&{claim_type_details}")
        if details:
            for k, v in details.items():
                if v == "" or type(v) is int:  # skip empty or integer cells
                    pass
                elif v[0] == '{' and v[-1] == '}':  # handling data input with bracket character, prevent auto assign of quote character
                    details[k] = ast.literal_eval(v)

            payload.update((k, v) for k, v in details.items() if v)  # only update payload if data input is not null

        payload = json.dumps(payload)
        BuiltIn().set_test_variable("${payload}", payload)
        print("Claim Type Payload: ", payload)
        return payload
