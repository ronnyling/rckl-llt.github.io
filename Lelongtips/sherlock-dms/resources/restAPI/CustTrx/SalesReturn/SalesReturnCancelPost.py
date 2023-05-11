import json
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
END_POINT_URL = PROTOCOL + "return" + APP_URL


class SalesReturnCancelPost(object):
    """ Functions to cancel return transaction """

    @keyword("user cancel ${cond} return")
    def user_cancel_return(self, cond):
        """ Function to retrieve cancel return """
        url = "{0}cancel-return".format(END_POINT_URL)
        payload = self.cancel_return_payload(cond)
        print("payload", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result == ", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def cancel_return_payload(self, cond):
        """ Status is is cancelled, so always will be hardcorded"""
        if cond == "invalid":
            return_id = COMMON_KEY.generate_random_id("0")
        else:
            return_id = BuiltIn().get_variable_value("${res_bd_return_id}")
        payload = [
            {
                "RETURN_ID": return_id,
                "STATUS":"C"
            }
        ]
        payload = json.dumps(payload)
        return payload