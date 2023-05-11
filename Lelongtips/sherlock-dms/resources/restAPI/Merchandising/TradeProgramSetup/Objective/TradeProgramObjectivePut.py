import json

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class TradeProgramObjectivePut(object):
    @keyword('user puts to trade program objective details')
    def user_put_to_trade_program_objective_details(self):
        tpo_id = BuiltIn().get_variable_value("${tpo_id}")
        url = "{0}trade-program-objective/{1}".format(END_POINT_URL, tpo_id)
        common = APIMethod.APIMethod()
        payload = self.gen_tpo_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        print("payload = " + str(payload))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def gen_tpo_payload(self):
        tpo_br = BuiltIn().get_variable_value("${tpo_br}")
        payload = {}
        payload.update((k, v) for k, v in tpo_br.items())
        return payload
