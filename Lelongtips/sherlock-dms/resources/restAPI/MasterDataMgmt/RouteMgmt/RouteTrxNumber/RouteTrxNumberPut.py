from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.MasterDataMgmt.RouteMgmt.RouteTrxNumber import RouteTrxNumberPost
from robot.api.deco import keyword
from setup.hanaDB import HanaDB
import json

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class RouteTrxNumberPut(object):
    """ Functions for updating route transaction number """

    @keyword('user updates route transaction number with ${data_type} data')
    def user_updates_route_trans_num_with_data(self, data_type):
        """ Functions to update route transaction number with random/given data """
        route_id = BuiltIn().get_variable_value("${route_id}")
        res_bd_route_trxno_id = BuiltIn().get_variable_value("${res_bd_route_trxno_id}")
        url = "{0}route/{1}/transactionnumber-route/{2}".format(END_POINT_URL, route_id, res_bd_route_trxno_id)
        payload = RouteTrxNumberPost.RouteTrxNumberPost().payload_route_trans("update random")
        print("Payload is : ", payload)
        payload = json.dumps(payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            res_bd_route_trxno_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_route_trxno_id}", res_bd_route_trxno_id)
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().user_validates_database_data("transactionnumber-route", body_result)
            # HanaDB.HanaDB().disconnect_from_database()
        BuiltIn().set_test_variable("${status_code}", response.status_code)
