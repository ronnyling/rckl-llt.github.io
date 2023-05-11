import secrets

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod


CUST_END_POINT_URL = PROTOCOL + "profile-cust" + APP_URL

class CustomerOptionGet(object):

    def user_retrieves_cust_option(self):
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        dist_id = BuiltIn().get_variable_value("${dist_id}")
        url = "{0}distributors/{1}/customer/{2}/customer-option".format(CUST_END_POINT_URL, dist_id, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve cust option"
        if response.status_code == 200:
            rand = secrets.choice(response.json())
            body_result = response.json()
            BuiltIn().set_test_variable("${cust_option_id}", rand['ID'])
        body_result = response.json()
        return body_result[0]

    def user_retrieves_cust_option_details(self):
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        cust_option_id = BuiltIn().get_variable_value("${cust_option_id}")
        url = "{0}distributors/1/customer/{1}/customer-option/{2}".format(CUST_END_POINT_URL, cust_id, cust_option_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve cust option"
        if response.status_code == 200:
            BuiltIn().set_test_variable("${cust_option_details}", response.json())
        return response.status_code