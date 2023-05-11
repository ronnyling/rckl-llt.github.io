from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class RouteTrxNumberGet(object):
    """ Functions to retrieve route transaction number """

    def user_retrieves_all_route_transaction_number(self):
        """ Function to retrieve all route transaction number """
        route_id = BuiltIn().get_variable_value("${route_id}")
        url = "{0}route/{1}/transactionnumber-route".format(END_POINT_URL, route_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_route_transaction_number_by_id(self):
        """ Function to retrieve route transaction number by using id """
        route_id = BuiltIn().get_variable_value("${route_id}")
        res_bd_route_trxno_id = BuiltIn().get_variable_value("${res_bd_route_trxno_id}")
        url = "{0}route/{1}/transactionnumber-route/{2}".format(END_POINT_URL, route_id, res_bd_route_trxno_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_route_trxno_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)
