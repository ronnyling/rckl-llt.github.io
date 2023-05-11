from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class SalesPersonGet(object):

    def user_gets_route_salesperson_info(self):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/route-salesperson".format(END_POINT_URL, dist_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${sp_ls}", body_result)
        print(response.json())
        return response.status_code


    def user_gets_route_salesperson_info_by_id(self):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        salesperson_id = BuiltIn().get_variable_value("${res_bd_salesperson_id}")
        url = "{0}distributors/{1}/route-salesperson/{2}".format(END_POINT_URL, dist_id, salesperson_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.json())
        return response.status_code

