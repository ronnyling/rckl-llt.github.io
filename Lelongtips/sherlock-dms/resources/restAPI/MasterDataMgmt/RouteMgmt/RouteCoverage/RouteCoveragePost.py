import json
import datetime
import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route.RouteGet import RouteGet

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL
current_date = datetime.datetime.now()
start_date = str((current_date + datetime.timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z")
end_date = str((current_date + datetime.timedelta(days=3)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z")
dist_op_type = ['O', 'V', 'M', 'T']
hq_op_type = dist_op_type + ['H', 'A']


class RouteCoveragePost(object):
    """ Functions to create route coverage """

    @keyword('When ${user_role} creates route coverage with ${type} data')
    def user_creates_route_coverage_with(self, user_role, type):
        """ Function to create route coverage with random/fixed data"""
        url = "{0}salesman-coverage-assignment".format(END_POINT_URL)
        payload = self.payload(user_role)
        print("Payload before post: ", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${route_coverage_id}", body_result['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload(self, user_role):
        """ Function for route coverage payload content """
        from_route_id = BuiltIn().get_variable_value("${from_route_id}")
        to_route_id = BuiltIn().get_variable_value("${to_route_id}")

        if from_route_id is None and to_route_id is None:
            if user_role == "hqadm":
                op_type = secrets.choice(hq_op_type)
            else:
                op_type = secrets.choice(dist_op_type)
            RouteGet().get_route_list_by_operation_type(op_type)
            route_br = BuiltIn().get_variable_value("${route_br}")
            route_count = len(route_br)
            assert route_count > 1, "Require at least 2 route with sane operation type to proceed route coverage"
            first_rand_no = secrets.randbelow(route_count)
            second_rand_no = secrets.randbelow(route_count)
            try_count = 0
            while first_rand_no == second_rand_no:
                try_count += 1
                second_rand_no = secrets.randbelow(route_count)
            print("Total try: {0}".format(try_count))
            print("First route: {0}".format(route_br[first_rand_no]))
            print("First route ID: {0}".format(route_br[first_rand_no]['ID']))
            print("Second route: {0}".format(route_br[second_rand_no]))
            print("Second route ID: {0}".format(route_br[second_rand_no]['ID']))

            from_route_id = route_br[first_rand_no]['ID']
            to_route_id = route_br[second_rand_no]['ID']
            BuiltIn().set_test_variable("${from_route_id}", from_route_id)
            BuiltIn().set_test_variable("${to_route_id}", to_route_id)

        cust = []
        self.retrieve_all_route_plan(from_route_id)
        rp_rs_bd = BuiltIn().get_variable_value("${rp_rs_bd}")
        if rp_rs_bd:
            print("rp_rs_bd: {0}".format(rp_rs_bd))
            rand_no = secrets.choice(rp_rs_bd)
            rp_id = rand_no['ID']
            self.retrieve_route_plan_cust_assignment(rp_id)
            rp_cust_rs_bd = BuiltIn().get_variable_value("${rp_cust_rs_bd}")
            if rp_cust_rs_bd:
                print("rp_cust_rs_bd: {0}".format(rp_cust_rs_bd))
                rand_no = secrets.choice(rp_cust_rs_bd)
                cust_id = rand_no['CUST_ID']
                cust_id = {"ID": cust_id}
                cust.append(cust_id)

        cust_count = len(cust)
        payload = {
            "FROM_ROUTE_ID": from_route_id,
            "TO_ROUTE_ID": to_route_id,
            "FROM_DATE": start_date,
            "TO_DATE": end_date,
            "CUSTOMER_COUNT": cust_count,
            "CUSTOMERS": cust
        }

        route_coverage_id = BuiltIn().get_variable_value("$route_coverage_id")
        if route_coverage_id:
            payload.pop("FROM_ROUTE_ID")
            payload.pop("TO_ROUTE_ID")

        payload = json.dumps(payload)
        return payload

    def retrieve_all_route_plan(self, route_id):
        """ Function to retrieve all route plan """
        dist_id = "undefined"
        url = "{0}distributors/{1}/route/{2}/route-plan".format(END_POINT_URL, dist_id, route_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable("${rp_rs_bd}", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def retrieve_route_plan_cust_assignment(self, routeplan_id):
        """ Function to retrieve route plan customer assginemtn"""
        dist_id = "undefined"
        url = "{0}distributors/{1}/route-plan/{2}/routeplan-custassignment/details".format(END_POINT_URL, dist_id, routeplan_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable("${rp_cust_rs_bd}", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)


