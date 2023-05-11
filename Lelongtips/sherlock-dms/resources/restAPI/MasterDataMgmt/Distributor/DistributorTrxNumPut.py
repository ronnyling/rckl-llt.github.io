from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.MasterDataMgmt.Distributor import DistributorTrxNumPost
from robot.api.deco import keyword
from setup.hanaDB import HanaDB
import json

END_POINT_URL = PROTOCOL + "profile-dist" + APP_URL


class DistributorTrxNumPut(object):
    """ Functions for updating distributor transaction number """

    @keyword('user updates distributor transaction number with ${data_type} data')
    def user_updates_distributor_trans_num_with_data(self, data_type):
        """ Functions to update distributor transaction number with random/given data """
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        res_bd_dist_trxno_id = BuiltIn().get_variable_value("${res_bd_dist_trxno_id}")
        url = "{0}distributors/{1}/transactionnumber/{2}".format(END_POINT_URL, distributor_id, res_bd_dist_trxno_id)
        payload = DistributorTrxNumPost.DistributorTrxNumPost().payload_dist_trans("update random")
        payload = json.dumps(payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            res_bd_dist_trxno_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_dist_trxno_id}", res_bd_dist_trxno_id)
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().user_validates_database_data("transactionnumber", body_result)
            # HanaDB.HanaDB().disconnect_from_database()
        BuiltIn().set_test_variable("${status_code}", response.status_code)
