from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route.RouteGet import RouteGet
from resources.restAPI.MasterDataMgmt.Distributor.DistributorGet import DistributorGet
from resources.restAPI.MasterDataMgmt.Customer.CustomerGet import CustomerGet
import datetime

NOW = datetime.datetime.now()
END_POINT_URL = PROTOCOL + "profile-route" + APP_URL
CUST_END_POINT_URL = PROTOCOL + "profile-cust" + APP_URL
CUST_TRX_END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class MyStoresGet(object):

    @keyword("user retrieves all route plan customer assignment for ${route_cd}")
    def user_retrieves_all_route_plan_cust_assignment(self, route_cd):
        """ Function to retrieve all route plan customer assginment """
        route_id = RouteGet().user_gets_route_by_using_code(route_cd)
        url = "{0}route/{1}/routeplan-custassignment/all".format(END_POINT_URL, route_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword("user retrieves my stores customer list")
    def user_retrieves_my_stores_cust_list(self):
        """ Function to retrieve my stores customer list """
        visit_date = str((NOW + datetime.timedelta(days=0)).strftime("%Y-%m-%d"))
        url = "{0}telesales/visit-date/{1}/customer-list".format(CUST_TRX_END_POINT_URL, visit_date)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword("user retrieves contact for {cust}")
    def user_retrieves_my_stores_cust_contact(self, cust):
        """ Function to retrieve my stores customer contact """
        dist_id = DistributorGet().user_gets_distributor_by_using_code("DistEgg")
        CustomerGet().user_gets_cust_by_using_code(cust)
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        url = "{0}distributors/{1}/customer/{2}/customer-contact".format(CUST_TRX_END_POINT_URL, dist_id, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
