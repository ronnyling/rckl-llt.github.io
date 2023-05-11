import json
import secrets

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class TradeProgramCriteriaPost(object):

    @keyword('user post to trade program criteria')
    def user_post_to_trade_program(self):
        url = "{0}trade-program-criteria".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_tp_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload)
        print("payload = " + str(payload))
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${tpc_br}", body_result)
            BuiltIn().set_test_variable("${tpc_id}", body_result['ID'])
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def gen_tp_payload(self):
        payload = {
            "CRITERIA_STATUS": "Active",
            "CRITERIA_CODE": "TPC" + ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5)),
            "CRITERIA_DESCRIPTION": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        }
        return payload
