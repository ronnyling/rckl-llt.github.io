from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class RouteCoverageGet(object):
    """ Functions to retrieve route coverage """
    ROUTE_COVERAGE_ID = "${route_coverage_id}"

    def user_retrieves_all_route_coverage(self):
        """ Function to retrieve all route coverage """
        url = "{0}salesman-coverage-assignment".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves route coverage by ${type} id')
    def user_retrieves_route_coverage_by_id(self, type):
        """ Function to retrieve route coverage by using id """
        if type == 'valid':
            route_coverage_id = BuiltIn().get_variable_value(self.ROUTE_COVERAGE_ID)
        else:
            route_coverage_id = Common().generate_random_id("0")
        url = "{0}salesman-coverage-assignment/{1}".format(END_POINT_URL, route_coverage_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
