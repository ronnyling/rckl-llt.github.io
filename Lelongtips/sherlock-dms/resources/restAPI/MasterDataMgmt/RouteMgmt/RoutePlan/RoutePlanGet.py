from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.Distributor.DistributorGet import DistributorGet
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route.RouteGet import RouteGet

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class RoutePlanGet(object):
    """ Functions to retrieve route plan """
    ROUTE_PLAN_ID = "${route_plan_id}"

    def user_retrieves_all_route_plan(self):
        """ Function to retrieve all route plan """
        dist_id = BuiltIn().get_variable_value("${dist_id}")
        route_id = BuiltIn().get_variable_value("${route_id}")
        url = "{0}distributors/{1}/route/{2}/route-plan".format(END_POINT_URL, dist_id, route_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves route plan by ${type} id')
    def user_retrieves_route_plan_by_id(self, type):
        """ Function to retrieve route plan by using id """
        if type == 'valid':
            route_plan_id = BuiltIn().get_variable_value(self.ROUTE_PLAN_ID)
        else:
            route_plan_id = Common().generate_random_id("0")
            DistributorGet().user_retrieves_random_distributor()
            RouteGet().user_retrieves_random_route()

        dist_id = BuiltIn().get_variable_value("${dist_id}")
        route_id = BuiltIn().get_variable_value("${route_id}")
        url = "{0}distributors/{1}/route/{2}/route-plan/{3}".format(END_POINT_URL, dist_id, route_id, route_plan_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
