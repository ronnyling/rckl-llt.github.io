from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "profile-dist" + APP_URL


class DistributorTrxNumGet(object):
    """ Functions to retrieve distributor transaction number """

    def user_retrieves_all_distributor_transaction_number(self):
        """ Function to retrieve all distributor transaction number """
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/transactionnumber".format(END_POINT_URL, distributor_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_distributor_transaction_number_by_id(self):
        """ Function to retrieve distributor transaction number by using id """
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        res_bd_dist_trxno_id = BuiltIn().get_variable_value("${res_bd_dist_trxno_id}")
        url = "{0}distributors/{1}/transactionnumber/{2}".format(END_POINT_URL, distributor_id, res_bd_dist_trxno_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_dist_trxno_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)
