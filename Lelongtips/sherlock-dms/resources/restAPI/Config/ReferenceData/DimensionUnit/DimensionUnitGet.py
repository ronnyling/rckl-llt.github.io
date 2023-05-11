from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class DimensionUnitGet(object):

    @keyword("user retrieves all dimension unit")
    def get_all_dimension_unit(self):
        url = "{0}module-data/dimension-unit".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of dimension unit retrieved are ", len(body_result))
            BuiltIn().set_test_variable("${dim_unt_br}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code

    @keyword("user retrieves dimension unit by ID")
    def user_retrieves(self):
        dimension_id = BuiltIn().get_variable_value("${dimension_id}")
        url = "{0}module-data/dimension-unit/{1}".format(END_POINT_URL, dimension_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
