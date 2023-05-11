import json
import secrets

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class TradeProgramObjectivePost(object):

    @keyword('user post to trade program objective')
    def user_post_to_trade_program_objective(self):
        url = "{0}trade-program-objective".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_tpo_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload)
        print("payload = " + str(payload))
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${tpo_br}", body_result)
            BuiltIn().set_test_variable("${tpo_id}", body_result['ID'])
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def gen_tpo_payload(self):
        payload = {
            "OBJECTIVE_STATUS": "Active",
            "OBJECTIVE_CODE": "TPO" + ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5)),
            "OBJECTIVE_DESCRIPTION": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "OBJECTIVE_TYPE": "Y"
        }
        return payload
