from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.RouteMgmt.RouteCoverage.RouteCoveragePost import RouteCoveragePost

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class RouteCoveragePut(object):
    """ Functions to update route coverage """

    @keyword('When ${user_role} updates route coverage with ${type} data')
    def user_updates_route_coverage_with(self, user_role, type):
        """ Function to update route coverage with random/fixed data"""
        route_coverage_id = BuiltIn().get_variable_value("$route_coverage_id")
        url = "{0}salesman-coverage-assignment/{1}".format(END_POINT_URL, route_coverage_id)
        payload = RouteCoveragePost().payload(user_role)
        print("Payload before put: ", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${route_coverage_id}", body_result['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)