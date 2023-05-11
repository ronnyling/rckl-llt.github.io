import secrets

from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
import json


CUST_END_POINT_URL = PROTOCOL + "profile-cust" + APP_URL


class CustomerShipToGet(object):

    def user_retrieves_cust_default_ship_to_address(self, cust):
        filter_ship_to = {"DEFAULT_SHIPTO": {"$eq": "true"}}
        filter_ship_to = json.dumps(filter_ship_to)
        str(filter_ship_to).encode(encoding='UTF-8', errors='strict')
        url = "{0}distributors/1/customer/{1}/cust-shipto?filter={2}".format(CUST_END_POINT_URL, cust, filter_ship_to)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve default customer ship to address"
        body_result = response.json()
        return body_result[0]

    def user_retrieves_random_ship_to(self):
        extension = '?filter={%22FIELDS%22:[%22ID%22,%22MODIFIED_DATE%22,%22SHIPTO_CD%22,%22SHIPTO_DESC%22,%22CONT_PERSON%22,%22CONT_NO%22,%22DEFAULT_SHIPTO%22],%22FILTER%22:[]}&silent=null'
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        url = "{0}distributors/1/customer/{1}/cust-shipto{2}".format(CUST_END_POINT_URL, cust_id, extension)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200 or response.status_code == 204, "Unable to retrieve default customer ship to address"
        if response.status_code == 200:
            rand = secrets.choice(response.json())
            BuiltIn().set_test_variable("${shipto_id}", rand['ID'])
        return response.status_code

    def user_retrieves_ship_to_details(self):
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        shipto_id = BuiltIn().get_variable_value("${shipto_id}")
        url = "{0}distributors/1/customer/{1}/cust-shipto/{2}".format(CUST_END_POINT_URL, cust_id, shipto_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${shipto_details}", response.json())
        return response.status_code
