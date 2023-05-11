import random
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.Common import Common

from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL


class RouteMappingDelete(object):


    @keyword("user deletes ${cond} route mapping data")
    def user_delete_route_mapping_data(self, cond):
        """ Function to delete mapped route record """
        print("cond",cond)
        if cond == 'invalid':
            route_id = Common().generate_random_id("0")
        else:
            route_id = BuiltIn().get_variable_value("${route_mapping_id_post}")
            print("route_mapping_id_post", route_id)
        url = "{0}supervisor-route-mapping/routes/{1}".format(END_POINT_URL, route_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

