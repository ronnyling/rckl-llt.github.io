from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.Common import Common
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Config.ReferenceData.VSKpiType import VSKpiTypePost
END_POINT_URL = PROTOCOL + "vs-scorecard" + APP_URL

class VSKpiTypePut(object):


    @keyword("user updates kpi type with ${data_type} data")
    def user_updates_kpi_type(self, data_type):
        if data_type == "invalid":
            res_bd_kpi_id = Common().generate_random_id("0")
        else:
            res_bd_kpi_id = BuiltIn().get_variable_value("${res_bd_kpi_id}")
        url = "{0}vs-kpi-type/{1}".format(END_POINT_URL, res_bd_kpi_id)
        payload = VSKpiTypePost.VSKpiTypePost().payload_kpi_type("update")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)


