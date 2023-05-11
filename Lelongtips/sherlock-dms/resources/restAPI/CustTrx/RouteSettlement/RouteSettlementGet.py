from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from resources.Common import Common
import json
import secrets

from resources.restAPI.MasterDataMgmt.RouteMgmt.Route.RouteGet import RouteGet
END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL

class RouteSettlementGet:
    @keyword('user retrieves all route settlement')
    def user_retrieves_all_route_settlement(self):
        url = "{0}route-settlement".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        BuiltIn().set_test_variable("${route_settlement_list}", response.json())
        return str(response.status_code), response.json()

    def user_retrieves_random_route_settlement_details_by_id(self):
        self.user_retrieves_all_route_settlement()
        rs_list = BuiltIn().get_variable_value("${route_settlement_list}")
        rand_int = secrets.choice(rs_list)
        rand_rs_id = rand_int['ID']
        url = "{0}route-settlement/{1}".format(END_POINT_URL, rand_rs_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code), response.json()

    def user_retrieves_transactions_for_route_settlement(self):
        RouteGet().user_gets_all_route_data()
        route_ls = BuiltIn().get_variable_value("${route_rs_body}")

        all_route_hht_vs = (
            route for route in route_ls
            if route['HHT_USRFLG'] == "Yes" and route['STATUS'] == "Active" and route['OP_TYPE'] == "V"
        )
        rand_route = next(all_route_hht_vs, None)
        rand_route_id = rand_route['ID']
        BuiltIn().set_test_variable("${route_id}", rand_route_id)
        BuiltIn().set_test_variable("${route_cd}", rand_route['ROUTE_CD'])
        BuiltIn().set_test_variable("${route_name}", rand_route['ROUTE_NAME'])

        params = 'datetimeTo=2099-01-01&primeFlag=PRIME'
        url = "{0}route-settlement/{1}/transactions?{2}".format(END_POINT_URL, rand_route_id, params)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code), response.json()

    def last_record_route(self, route_id):
        self.user_retrieves_transactions_for_route_settlement()
        params = "primeFlag=PRIME"
        url = "{0}route-settlement/lastRecord/{1}?{2}".format(END_POINT_URL, route_id, params)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${last_rec_details}", response.json())
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.json()
