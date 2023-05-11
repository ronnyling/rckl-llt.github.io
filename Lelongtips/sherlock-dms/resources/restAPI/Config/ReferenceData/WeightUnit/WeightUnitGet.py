from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class WeightUnitGet(object):

    @keyword("user retrieves all weight unit")
    def get_all_weight_unit(self):
        url = "{0}module-data/weight-unit".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of weight unit retrieved are ", len(body_result))
            BuiltIn().set_test_variable("${weight_unt_br}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code

    @keyword("user retrieves weight unit by ID")
    def user_retrieves(self):
        weight_id = BuiltIn().get_variable_value("${weight_id}")
        url = "{0}module-data/weight-unit/{1}".format(END_POINT_URL, weight_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
