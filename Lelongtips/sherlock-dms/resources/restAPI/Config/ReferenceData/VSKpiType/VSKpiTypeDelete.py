from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.Common import Common
from resources.restAPI import PROTOCOL, APP_URL

END_POINT_URL = PROTOCOL + "vs-scorecard" + APP_URL

class VSKpiTypeDelete(object):


    @keyword("user deletes kpi type with ${type} ID")
    def user_retrieves_user_setup(self, type):
        if type == "invalid":
            res_bd_kpi_id = Common().generate_random_id("0")
        else:
            res_bd_kpi_id = BuiltIn().get_variable_value("${res_bd_kpi_id}")
        url = "{0}vs-kpi-type/{1}".format(END_POINT_URL, res_bd_kpi_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)



