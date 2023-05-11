import json

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route import RoutePost
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route.RouteGet import RouteGet

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class RoutePut(object):
    ROUTE_ID = "${res_bd_route_id}"
    ROUTE_DETAILS = "${route_details}"
    """ Functions to update route record """

    @keyword('When user updates route with ${data_type} data')
    def user_updates_route_with(self, data_type):
        """ Function to update route by using random/given data """
        res_bd_route_id = BuiltIn().get_variable_value(self.ROUTE_ID)
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        # user_role = BuiltIn().get_variable_value("${user_role}")
        # print("User_role: ", user_role)
        url = "{0}distributors/{1}/route/{2}".format(END_POINT_URL, distributor_id, res_bd_route_id)
        res_bd_route = BuiltIn().get_variable_value("${res_bd_route}")
        route_details = BuiltIn().get_variable_value(self.ROUTE_DETAILS)
        if route_details is not None:
            route_details["ROUTE_CD"] = res_bd_route['ROUTE_CD']
            route_details["OP_TYPE"] = res_bd_route['OP_TYPE']
            route_details["ID"] = res_bd_route_id
        else:
            route_details = {
                "ROUTE_CD": res_bd_route['ROUTE_CD'],
                "OP_TYPE": res_bd_route['OP_TYPE'],
                "ID" : res_bd_route_id
            }
        BuiltIn().set_test_variable("${route_details}", route_details)
        payload = RoutePost.RoutePost().payload_route("update")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            res_bd_route_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_route_id}", res_bd_route_id)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_puts_route_transaction_control_setting(self):
        RouteGet().user_retrieve_route_transaction_control_setting()
        txn_ctrl_route = BuiltIn().get_variable_value("${txn_ctrl_route}")

        route_id = BuiltIn().get_variable_value("${res_bd_route_id}")
        url = "{0}setting-routetransactioncontrol/route/{1}".format(END_POINT_URL, route_id)
        common = APIMethod.APIMethod()

        payload = self.gen_tc_payload(txn_ctrl_route)
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("response body = " + str(body_result))
            BuiltIn().set_test_variable("${txn_ctrl_route}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def gen_tc_payload(self, txn_ctrl_route):
        payload = txn_ctrl_route
        return payload