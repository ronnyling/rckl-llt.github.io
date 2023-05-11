from resources.restAPI.Common import APIMethod, TokenAccess
from resources.restAPI import PROTOCOL, APP_URL
import urllib3
from resources.restAPI.CustTrx.SalesReturn import SalesReturnPost
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
urllib3.disable_warnings()

END_POINT_URL = PROTOCOL + "return" + APP_URL


class SalesReturnPut(object):

    @keyword("user updates return with ${data_type} data")
    def user_updates_return_with_data(self, data_type):
        url = "{0}return".format(END_POINT_URL)
        rtn_id = BuiltIn().get_variable_value("${res_bd_return_id}")
        rtn_header_details = BuiltIn().get_variable_value("${rtn_header_details}")
        rtn_type = BuiltIn().get_variable_value("${rtn_type}")
        rtn_header_details.update({"ID": rtn_id, "PRIME_FLAG": rtn_type})
        BuiltIn().set_test_variable("${rtn_header_details}", rtn_header_details)
        payload = SalesReturnPost.SalesReturnPost().payload_return()
        user = BuiltIn().get_variable_value("${user_role}")
        TokenAccess.TokenAccess().get_token_by_role(user)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code != 200:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            print("Respond for SalesReturn: ", body_result)
