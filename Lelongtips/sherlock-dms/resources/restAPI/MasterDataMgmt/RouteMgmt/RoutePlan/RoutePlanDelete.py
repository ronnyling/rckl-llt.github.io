from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class RoutePlanDelete(object):
    """Function to delete route plan"""

    def user_deletes_route_plan(self):
        route_plan_id = BuiltIn().get_variable_value("${route_plan_id}")
        dist_id = BuiltIn().get_variable_value("${dist_id}")
        route_id = BuiltIn().get_variable_value("${route_id}")
        url = "{0}distributors/{1}/route/{2}/route-plan/{3}".format(END_POINT_URL, dist_id, route_id, route_plan_id)
        print("Delete URL: ", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
