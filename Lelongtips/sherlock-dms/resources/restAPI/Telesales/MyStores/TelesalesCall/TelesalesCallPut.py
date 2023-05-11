from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import TokenAccess
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route.RouteGet import RouteGet
from resources.restAPI.MasterDataMgmt.Distributor.DistributorGet import DistributorGet
from resources.restAPI.MasterDataMgmt.Customer.CustomerGet import CustomerGet
import json
END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class TelesalesCallPut(object):
    @keyword('user updates telesales call with ${data_type} data')
    def user_updates_telesales_call(self, data_type):
        details = BuiltIn().get_variable_value("${call_details}")
        call_id = BuiltIn().get_variable_value("${call_id}")
        url = "{0}telesales/transaction/telesales-call-update".format(END_POINT_URL)
        TokenAccess.TokenAccess().user_retrieves_token_access_as('hqadm')
        dist_id = DistributorGet().user_gets_distributor_by_using_code(details['DIST_CD'])
        route_id = RouteGet().user_gets_route_by_using_code(details['ROUTE_CD'])
        CustomerGet().user_gets_cust_by_using_code(details['CUST_CD'])
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        end_call = {
            "DIST_ID": dist_id,
            "ROUTE_ID": route_id,
            "CUST_ID": cust_id,
            "ID": call_id,
            "CALL_OUT": details['CALL_OUT'],
            "TIME_SPENT": details['TIME_SPENT'],
            "CALLBACK_DT": details['CALLBACK_DT'],
            "CALL_STATUS": details['CALL_STATUS'],
            "REASON_ID": ""
        }
        payload = json.dumps(end_call)
        print("payload ", payload)
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code


