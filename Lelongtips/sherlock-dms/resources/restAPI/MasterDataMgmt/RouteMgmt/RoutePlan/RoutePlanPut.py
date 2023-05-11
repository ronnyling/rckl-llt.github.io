import json
import datetime
import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.RouteMgmt.RoutePlan.RoutePlanPost import RoutePlanPost
hq_dist_id = "3CAF4BF6:8C7572E0-F133-4341-9B42-8C5D32CC6352"

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class RoutePlanPut(object):
    """ Functions to update route plan """

    @keyword('When ${user_role} updates route plan with ${type} data')
    def user_updates_route_plan_with(self, user_role, type):
        """ Function to update route plan with random/fixed data"""
        route_plan_id = BuiltIn().get_variable_value("${route_plan_id}")
        dist_id = BuiltIn().get_variable_value("${dist_id}")
        route_id = BuiltIn().get_variable_value("${route_id}")
        url = "{0}distributors/{1}/route/{2}/route-plan/{3}".format(END_POINT_URL, dist_id, route_id, route_plan_id)
        common = APIMethod.APIMethod()
        payload = RoutePlanPost().payload(dist_id)
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${route_plan_id}", body_result['ID'])
            BuiltIn().set_test_variable("${route_id}", body_result['ROUTE_ID'])
            BuiltIn().set_test_variable("${dist_id}", body_result['DIST_ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)
