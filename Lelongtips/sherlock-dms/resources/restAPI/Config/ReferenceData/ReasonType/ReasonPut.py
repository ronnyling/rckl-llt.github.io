from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import secrets
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.Common import Common
from resources.restAPI.Config.ReferenceData.ReasonType.ReasonGet import ReasonGet
END_POINT_URL = PROTOCOL + "setting" + APP_URL


class ReasonPut(object):
    REASON_TYPE_ID = "${res_bd_reason_type_id}"

    @keyword('user updates reason with ${data_type} id')
    def user_updates_reason_with(self, data_type):
        if data_type == "invalid":
            res_bd_reason_id = Common().generate_random_id("0")
        else:
            res_bd_reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        res_bd_reason_type_id = BuiltIn().get_variable_value("${res_bd_reason_type_id}")
        url = "{0}setting-reasontype/{1}/setting-reason/{2}".format(END_POINT_URL, res_bd_reason_type_id,res_bd_reason_id)
        payload = self.payload_reason(res_bd_reason_type_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_reason(self,reason_type):

        body_result = ReasonGet.user_retrieves_reason_by_id(self, "valid")

        payload = {
                "REASON_CD": body_result['REASON_CD'],
                "REASON_TYPE_ID": reason_type,
                "REASON_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20))
            }
        details = BuiltIn().get_variable_value("${new_reason_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Reason Payload: ", payload)
        return payload
