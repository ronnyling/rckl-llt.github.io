from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
END_POINT_URL = PROTOCOL + "product" + APP_URL


class ProductDelete:

    def user_deletes_product(self):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        prod_id = BuiltIn().get_variable_value("${prd_id}")
        url = "{0}distributors/{1}/product/{2}".format(END_POINT_URL, dist_id, prod_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code

    def user_deletes_created_product(self):
        prod_id = BuiltIn().get_variable_value("${prd_id}")
        url = "{0}/product/{1}".format(END_POINT_URL, prod_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code
