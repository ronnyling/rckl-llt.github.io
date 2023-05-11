from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.restAPI.Common import TokenAccess
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route.RouteGet import RouteGet
from resources.restAPI.MasterDataMgmt.Distributor.DistributorGet import DistributorGet
from resources.restAPI.MasterDataMgmt.Customer.CustomerGet import CustomerGet
import datetime
import secrets
import json

max_duration = 60000
current_datetime = datetime.datetime.now()
CUST_TRX_END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL
call_status = ['P', 'U', 'C', 'M', 'P']
call_type = ['I', 'O']


class TelesalesCallPost(object):

    @keyword("user creates telesales call")
    def user_create_telesales_call(self):
        """ Function to create telesales call """
        url = "{0}telesales/transaction/telesales-call-details".format(CUST_TRX_END_POINT_URL)
        payload = self.payload()
        print("Payload before post: ", payload)
        print("URL before post: ", url)
        user_role = BuiltIn().get_variable_value("${user_role}")
        print("User_role before post = ", user_role)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${call_id}", body_result['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload(self):
        """ Function for telesales call payload content """
        call_details = BuiltIn().get_variable_value("${call_details}")
        user_role = BuiltIn().get_variable_value("${user_role}")
        print("User_role = ", user_role)
        TokenAccess.TokenAccess().user_retrieves_token_access_as('hqadm')
        dist_id = DistributorGet().user_gets_distributor_by_using_code(call_details['DIST_CD'])
        route_id = RouteGet().user_gets_route_by_using_code(call_details['ROUTE_CD'])
        CustomerGet().user_gets_cust_by_using_code(call_details['CUST_CD'])
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        TokenAccess.TokenAccess().user_retrieves_token_access_as(user_role)
        time_spent = secrets.randbelow(max_duration)
        call_in = str(current_datetime - datetime.timedelta(milliseconds=time_spent))
        call_out = str(current_datetime)

        payload = {
            "DIST_ID": dist_id,
            "ROUTE_ID": route_id,
            "CUST_ID": cust_id,
            "CALL_IN": call_in,
            "CALL_OUT": call_out,
            "TIME_SPENT": time_spent,
            "REASON_ID": "",
            "CALLBACK_DT": "",
            "CALL_STATUS": secrets.choice(call_status),
            "CALL_TYPE": secrets.choice(call_type)
        }

        payload = json.dumps(payload)
        return payload
