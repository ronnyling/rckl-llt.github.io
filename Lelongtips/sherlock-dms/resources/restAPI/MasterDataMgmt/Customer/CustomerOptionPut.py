import json

from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL

CUST_END_POINT_URL = PROTOCOL + "profile-cust" + APP_URL


class CustomerOptionPut(object):

    def user_puts_cust_option_details(self):
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        cust_option_id = BuiltIn().get_variable_value("${cust_option_id}")
        cust_option_details = BuiltIn().get_variable_value("${cust_option_details}")
        url = "{0}distributors/1/customer/{1}/customer-option/{2}".format(CUST_END_POINT_URL, cust_id, cust_option_id)
        payload = json.dumps(cust_option_details)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        assert response.status_code == 200, "Unable to retrieve cust option"
        return response.status_code