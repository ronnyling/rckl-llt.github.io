from resources.restAPI import PROTOCOL, APP_URL, Common
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class RouteActivityAssignmentGet(object):
    """ Functions to retrieve playbook assignment"""

    @keyword("user retrieves route activity ${type} assignment")
    def user_retrieves_route_activity_assignment(self, type):
        activity_id = BuiltIn().get_variable_value("${res_bd_route_activity_id}")
        if type == "distributor":
            url = "{0}merchandising/merc-route-activity/{1}/merc-dist-assignment".format(END_POINT_URL, activity_id)
        elif type == "route":
            url = "{0}merchandising/merc-route-activity/{1}/merc-route-assignment".format(END_POINT_URL, activity_id)
        elif type == "customer":
            transaction_id = BuiltIn().get_variable_value("${transaction_id}")
            url = "{0}merchandising/merc-route-activity/{1}/transaction-list/{2}/merc-cust-assignment".format(END_POINT_URL, activity_id, transaction_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
