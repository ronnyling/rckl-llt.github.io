from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import secrets
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class ReasonPost(object):
    """ Functions to create reason type record """

    @keyword('user creates reason with ${data_type} data')
    def user_creates_reason_with(self, data_type):
        """ Functions to create reason type using given/fixed data"""
        res_bd_reason_type_id = BuiltIn().get_variable_value("${res_bd_reason_type_id}")
        url = "{0}setting-reasontype/{1}/setting-reason".format(END_POINT_URL, res_bd_reason_type_id)
        payload = self.payload_reason(data_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            res_bd_reason_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_reason_id}", res_bd_reason_id)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_reason(self,data_type):
        """ Functions for reason payload content """

        payload = {
            "REASON_CD": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "REASON_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20))
        }

        if data_type == "existing":
            payload['REASON_CD'] = BuiltIn().get_variable_value("${reason_cd}")
            payload['REASON_DESC'] = BuiltIn().get_variable_value("${reason_desc}")

        details = BuiltIn().get_variable_value("${reason_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        BuiltIn().set_test_variable("${reason_cd}", payload['REASON_CD'])
        BuiltIn().set_test_variable("${reason_desc}", payload['REASON_DESC'])
        payload = json.dumps(payload)
        print("Reason Payload: ", payload)
        return payload
