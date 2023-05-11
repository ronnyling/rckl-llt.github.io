from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL+"merchandising"+APP_URL


class RouteActivityDelete:

    def user_deletes_created_route_activity(self):
        res_bd_route_activity_id = BuiltIn().get_variable_value("${res_bd_route_activity_id}")
        url = "{0}merchandising/merc-route-activity/{1}".format(END_POINT_URL, res_bd_route_activity_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        assert response.status_code == 200, "Route Activity not deleted"
