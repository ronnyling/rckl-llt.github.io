import json

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "user-info" + APP_URL


class UserApproval(object):

    @keyword("user perform ${action} on the created activation request")
    def approve_reject_user_license(self,action):
        user_id = BuiltIn().get_variable_value("${res_bd_salesperson_id}")
        url = "{0}user/{1}/{2}".format(END_POINT_URL, user_id, action)
        common = APIMethod.APIMethod()
        if action == "approval":
            payload = self.payload()
            payload = json.dumps(payload)
            response = common.trigger_api_request("PUT", url, payload)
        else :
            response = common.trigger_api_request("PUT", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)


    def payload(self):
        payload = {
            "DECISION":"A"
        }
        return payload
