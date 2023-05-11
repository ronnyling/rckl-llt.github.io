from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL+"setting"+APP_URL

class BinDelete(object):

    @keyword('user deletes bin')
    def user_deletes_bin(self):
        res_bd_bin_id = BuiltIn().get_variable_value("${res_bd_bin_id}")
        url = "{0}warehouse-bin/{1}".format(END_POINT_URL, res_bd_bin_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)




