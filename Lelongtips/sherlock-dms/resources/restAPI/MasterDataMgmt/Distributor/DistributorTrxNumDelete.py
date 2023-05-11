from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "profile-dist" + APP_URL


class DistributorTrxNumDelete(object):
    """ Functions to delete distributor transaction number """

    def user_deletes_distributor_transaction_number(self):
        """ Function to delete warehouse using given id """
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        res_bd_dist_trxno_id = BuiltIn().get_variable_value("${res_bd_dist_trxno_id}")
        url = "{0}distributors/{1}/transactionnumber/{2}".format(END_POINT_URL, distributor_id, res_bd_dist_trxno_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
