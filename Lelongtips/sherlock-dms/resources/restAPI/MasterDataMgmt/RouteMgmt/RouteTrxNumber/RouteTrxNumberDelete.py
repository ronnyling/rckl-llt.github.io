from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class RouteTrxNumberDelete(object):
    """ Functions to delete route transaction number """

    def user_deletes_route_transaction_number(self):
        """ Function to delete route trx number """
        route_id = BuiltIn().get_variable_value("${route_id}")
        res_bd_route_trxno_id = BuiltIn().get_variable_value("${res_bd_route_trxno_id}")
        url = "{0}route/{1}/transactionnumber-route/delete".format(END_POINT_URL, route_id)
        payload = self.payload_route_trans_del(res_bd_route_trxno_id)
        print("Payload is : ", payload)
        payload_dump = json.dumps(payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload_dump)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_route_trans_del(self, route_trx_num_id):
        """ distributor route transaction number payload content """
        payload = [
            route_trx_num_id
        ]
        return payload

