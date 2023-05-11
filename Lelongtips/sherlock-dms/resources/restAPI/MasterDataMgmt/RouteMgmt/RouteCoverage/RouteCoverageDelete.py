from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class RouteCoverageDelete(object):
    """Function to delete route coverage"""

    def user_deletes_route_coverage(self):
        route_coverage_id = BuiltIn().get_variable_value("${route_coverage_id}")
        url = "{0}salesman-coverage-assignment/{1}".format(END_POINT_URL, route_coverage_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
