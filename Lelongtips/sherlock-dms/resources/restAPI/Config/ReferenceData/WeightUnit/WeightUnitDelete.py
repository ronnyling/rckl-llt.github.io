from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "product" + APP_URL


class WeightUnitDelete(object):

    @keyword('user deletes weight unit with ${data}')
    def user_deletes_weight_unit_with(self, data):
        if data == "created data":
            weight_id = BuiltIn().get_variable_value("${weight_id}")
        url = "{0}weight-setting/{1}".format(END_POINT_URL, weight_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
