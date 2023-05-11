import datetime
import json
import secrets
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL
END_POINT_URL_DYNAMIC_HIER = PROTOCOL + "dynamic-hierarchy" + APP_URL
END_POINT_URL_PROFILE_DIST = PROTOCOL + "profile-dist" + APP_URL



class RouteGet(object):
    """ Functions to retrieve route record """
    DIST_ID = "${distributor_id}"
    CUST_ID = "${cust_id}"

    def user_gets_all_route_data(self):
        """ Function to retrieve all route record """
        distributor_id = BuiltIn().get_variable_value(self.DIST_ID)
        url = "{0}distributors/{1}/route".format(END_POINT_URL, distributor_id)
        print("route url: ", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable("${route_rs_body}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_random_route(self):
        self.user_gets_all_route_data()
        route_list = BuiltIn().get_variable_value("${route_rs_body}")
        rand_no = secrets.choice(route_list)
        rand_route = rand_no
        BuiltIn().set_test_variable("${route_id}", rand_route['ID'])
        return rand_route

    def user_retrieves_route_with_slsperson_by_dist_id_and_op_type(self, exp_dist_id, exp_op_type):
        self.user_gets_all_route_data()
        route_list = BuiltIn().get_variable_value("${route_rs_body}")
        route = {}
        print("Before loop, dist id  op type = " + str(exp_dist_id) + " " + str(exp_op_type) )
        for x in route_list:
            print("Route X = ", x)
            dist_id = x['DIST_ID']
            op_type = x['OP_TYPE']
            print("expected_dist_id = ", exp_dist_id)
            print("exp_op_type = ", exp_op_type)
            if dist_id == exp_dist_id and op_type == exp_op_type and x['SALES_PERSON'] is not None:
                route = x
                print("Selected route = ", route)
                break
        assert route is None, "No suitable records found"
        BuiltIn().set_test_variable("${route_id}", route['ID'])
        return route

    def user_gets_route_by_using_id(self):
        """ Function to retrieve route by using given id """
        res_bd_route_id = BuiltIn().get_variable_value("${res_bd_route_id}")
        distributor_id = BuiltIn().get_variable_value(self.DIST_ID)
        url = "{0}distributors/{1}/route/{2}".format(END_POINT_URL, distributor_id, res_bd_route_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            BuiltIn().set_test_variable("${route_details}", response.json())
            assert res_bd_id == res_bd_route_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword("user gets route by using code '${route_cd}'")
    def user_gets_route_by_using_code(self, route_cd):
        """ Functions to retrieve route id by using route code """
        dist_id = BuiltIn().get_variable_value(self.DIST_ID)
        filter_route = {"ROUTE_CD": {"$eq": route_cd}}
        filter_route = json.dumps(filter_route)
        str(filter_route).encode(encoding='UTF-8', errors='strict')
        url = "{0}distributors/{1}/route?filter={2}".format(END_POINT_URL, dist_id, filter_route)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve Route"
        body_result = response.json()
        route_id = body_result[0]['ID']
        BuiltIn().set_test_variable("${route_rs_bd}", body_result[0])
        BuiltIn().set_test_variable("${route_id}", route_id)
        BuiltIn().set_test_variable("${route_cd}", route_cd)
        return route_id

    @keyword("user gets route plan by using code '${rp_cd}'")
    def user_gets_route_plan_by_using_code(self, rp_cd):
        """ Functions to retrieve route plan id by using route plan code """
        route_id = BuiltIn().get_variable_value('${route_id}')
        dist_id = BuiltIn().get_variable_value(self.DIST_ID)
        filter_rp = {"RP_CD":{"$eq":rp_cd}}
        filter_rp = json.dumps(filter_rp)
        str(filter_rp).encode(encoding='UTF-8', errors='strict')
        url = "{0}distributors/{1}/route/{2}/route-plan?filter={3}".format(END_POINT_URL, dist_id, route_id, filter_rp)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve Route Plan "
        body_result = response.json()
        rp_id = body_result[0]['ID']
        BuiltIn().set_test_variable("${rp_id}", rp_id)
        BuiltIn().set_test_variable("${rp_cd}", rp_cd)

    def get_route_list_by_operation_type(self, op_type):
        """ Functions to retrieve route id by using route operation type """
        #route_id = BuiltIn().get_variable_value('${route_id}')
        #dist_id = BuiltIn().get_variable_value(self.DIST_ID)
        dist_id = "undefined"
        filter_op = {"OP_TYPE": {"$eq": op_type}}
        filter_op = json.dumps(filter_op)
        str(filter_op).encode(encoding='UTF-8', errors='strict')
        url = "{0}distributors/{1}/route?filter={2}".format(END_POINT_URL, dist_id, filter_op)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve Route"
        body_result = response.json()
        BuiltIn().set_test_variable("${route_br}", body_result)
        route_id = body_result[0]['ID']
        BuiltIn().set_test_variable("${route_id}", route_id)

    @keyword("user validated supervisor route will not be retrieved")
    def check_supervisor_route_is_exist(self):
        route_rs_body = BuiltIn().get_variable_value("${route_rs_body}")
        flag = False
        for item in route_rs_body:
            if item['OP_TYPE'] == 'S':
                flag = True
        assert flag is False, "Supervisor Route is found!!!"

    def user_gets_route_with_open_items(self):
        cust_id = BuiltIn().get_variable_value(self.CUST_ID)
        url = "{0}customer/{1}/all-cust-route-opn?includeOpenItems=true".format(END_POINT_URL, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve Route"
        body_result = response.json()
        return len(body_result)

    def user_retrieve_nodes_to_assign(self):
        url = "{0}route/nodes-to-assign".format(END_POINT_URL_DYNAMIC_HIER)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("response body = " + str(body_result))
            BuiltIn().set_test_variable("${nodes_to_assign}",body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieve_nodes(self):
        route_id = BuiltIn().get_variable_value("${res_bd_route_id}")
        url = "{0}route/{1}/nodes".format(END_POINT_URL_DYNAMIC_HIER, route_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("response body = " + str(body_result))
            BuiltIn().set_test_variable("${route_nodes}",body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieve_route_transaction_control_setting(self):
        route_id = BuiltIn().get_variable_value("${res_bd_route_id}")
        url = "{0}setting-routetransactioncontrol/route/{1}".format(END_POINT_URL, route_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("response body = " + str(body_result))
            BuiltIn().set_test_variable("${txn_ctrl_route}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieve_route_calender_view(self):
        year = datetime.datetime.today().year
        month = datetime.datetime.today().month
        route_id = BuiltIn().get_variable_value("${res_bd_route_id}")
        url = "{0}route/{1}/calendar-view/{2}/{3}".format(END_POINT_URL, route_id, year, month)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("response body = " + str(body_result))
            BuiltIn().set_test_variable("${cal_view}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieve_distributor_geotree(self):
        url = "{0}distributor-geotree".format(END_POINT_URL_PROFILE_DIST)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("response body = " + str(body_result))
            BuiltIn().set_test_variable("${geotree_dist}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieve_customers_assigned_to_routeplan(self):
        route_id = BuiltIn().get_variable_value("${res_bd_route_id}")
        distributor_id = BuiltIn().get_variable_value(self.DIST_ID)
        url = "{0}distributors/{1}/route/{2}/routecust".format(END_POINT_URL, distributor_id, route_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("response body = " + str(body_result))
            BuiltIn().set_test_variable("${route_cust}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
