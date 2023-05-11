from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class ReasonDelete(object):
    """ Functions to delete reason record """
    @keyword('user deletes reason with ${type} data')
    def user_deletes_reason_with_created_data(self,type):
        """ Function to delete reason by using id given """
        if type=="invalid":
            res_bd_reason_id = Common().generate_random_id("0")
        else:
            res_bd_reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        res_bd_reason_type_id = BuiltIn().get_variable_value("${res_bd_reason_type_id}")
        url = "{0}setting-reasontype/{1}/setting-reason/{2}" \
            .format(END_POINT_URL, res_bd_reason_type_id, res_bd_reason_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
