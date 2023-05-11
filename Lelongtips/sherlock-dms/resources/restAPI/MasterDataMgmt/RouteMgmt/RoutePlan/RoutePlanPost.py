import json
import datetime
import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.Distributor.DistributorGet import DistributorGet
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route.RouteGet import RouteGet

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL
current_date = datetime.datetime.now()
start_date = str((current_date + datetime.timedelta(days=2)).strftime("%Y-%m-%d"))
end_date = str((current_date + datetime.timedelta(days=3)).strftime("%Y-%m-%d"))
hq_op_type = ['H', 'Q', 'A']
dist_op_type = ['V', 'O', 'M', 'T']
hq_dist_id = "3CAF4BF6:8C7572E0-F133-4341-9B42-8C5D32CC6352"


class RoutePlanPost(object):
    """ Functions to create route plan """

    @keyword('When ${user_role} creates route plan with ${type} data')
    def user_creates_route_plan_with(self, user_role, type):
        """ Function to create route plan with random/fixed data"""
        if user_role == "hqadm":
            dist_id = hq_dist_id
        else:
            dist_id = DistributorGet().user_gets_distributor_by_using_code("DistEgg")

        BuiltIn().set_test_variable("${dist_id}", dist_id)
        payload = self.payload(dist_id)
        route_id = BuiltIn().get_variable_value("${route_id}")
        url = "{0}distributors/{1}/route/{2}/route-plan".format(END_POINT_URL, dist_id, route_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print("payload : " + str(payload))
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${route_plan_id}", body_result['ID'])
            BuiltIn().set_test_variable("${route_id}", body_result['ROUTE_ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload(self, dist_id):
        """ Function for route plan payload """
        route_id = BuiltIn().get_variable_value("${route_id}")
        if route_id is None:
            if dist_id == hq_dist_id:
                dist_id = None
                rand_op_type = secrets.choice(hq_op_type)
            else:
                rand_op_type = secrets.choice(dist_op_type)
            route_details = RouteGet().user_retrieves_route_with_slsperson_by_dist_id_and_op_type(dist_id, rand_op_type)
            BuiltIn().set_test_variable("${route_id}", route_details['ID'])
        dist_details = BuiltIn().get_variable_value("${dist_details}")
        if dist_details is None:
            dist_details = DistributorGet().user_retrieves_random_distributor()
            BuiltIn().set_test_variable("${dist_id}", dist_details['ID'])
            BuiltIn().set_test_variable("${dist_details}", dist_details)

        payload = {
            "RP_TYPE": "NF",
            # "RP_VISIT_DAY": [],
            "RP_WEEK": [],
            # "RP_MONTH": [],
            "RP_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "RP_FREQUENCY": None,
            "RP_STARTDATE": start_date,
            "RP_ENDDATE": end_date,
            "DIST_ID_RP": dist_details
        }

        payload2 = {
            "RP_TYPE": "F",
            "RP_VISIT_DAY": [
                "RP_DAY_MON",
                "RP_DAY_TUE",
                "RP_DAY_WED",
                "RP_DAY_THU",
                "RP_DAY_FRI",
                "RP_DAY_SAT",
                "RP_DAY_SUN"
            ],
            "RP_WEEK": [],
            "RP_MONTH": [],
            "RP_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "RP_FREQUENCY": "F01",
            "RP_STARTDATE": start_date,
            "RP_ENDDATE": end_date
        }
        payload = payload2
        route_plan_id = BuiltIn().get_variable_value("${route_plan_id}")
        if route_plan_id:
            payload['ID'] = route_plan_id
        payload = json.dumps(payload)
        return payload

    def user_triggers_routeplan_generator(self):
        route_id = BuiltIn().get_variable_value("${res_bd_route_id}")
        url = "{0}schedule-routeplan-generator".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_rpgen_payload(route_id)
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("response body = " + str(body_result))
            BuiltIn().set_test_variable("${rp_schedule}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def gen_rpgen_payload(self, route_id):
        payload = {}
        payload['DIST_CD'] = 'DistEgg'
        payload['ROUTE_ID'] = route_id
        return payload

    @keyword('user creates route plan')
    def user_creates_route_plan_with(self):
        RouteGet().user_gets_all_route_data()
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        dist_id = BuiltIn().get_variable_value("${dist_id}")
        route_rs_body = BuiltIn().get_variable_value("${route_rs_body}")
        route_sp_id = None
        for route in route_rs_body:
            if route['DIST_ID'] == distributor_id:
                BuiltIn().set_test_variable("${res_bd_route_id}", route['ID'])
                RouteGet().user_gets_route_by_using_id()
                route_details = BuiltIn().get_variable_value("${route_details}")
                if route_details['SALES_PERSON'] is not None:
                    route_sp_id = route_details['ID']
                    break
        payload = self.gen_rp_payload()
        print("my record here " + str(distributor_id) + str(route_sp_id) + str(dist_id))
        url = "{0}distributors/{1}/route/{2}/route-plan".format(END_POINT_URL, distributor_id, route_sp_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print("payload : " + str(payload))
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${route_plan_id}", body_result['ID'])
            BuiltIn().set_test_variable("${route_id}", body_result['ROUTE_ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def gen_rp_payload(self):
        payload = {
            "RP_TYPE": "F",
            "RP_VISIT_DAY": [
                "RP_DAY_MON",
                "RP_DAY_TUE",
                "RP_DAY_WED",
                "RP_DAY_THU",
                "RP_DAY_FRI",
                "RP_DAY_SAT",
                "RP_DAY_SUN"
            ],
            "RP_WEEK": [],
            "RP_MONTH": [],
            "RP_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "RP_FREQUENCY": "F01",
            "RP_STARTDATE": start_date,
            "RP_ENDDATE": end_date
        }
        payload = json.dumps(payload)
        return payload