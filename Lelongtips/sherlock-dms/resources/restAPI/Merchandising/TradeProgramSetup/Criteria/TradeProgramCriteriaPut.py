import json

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class TradeProgramCriteriaPut(object):
    @keyword('user puts to trade program criteria details')
    def user_put_to_trade_program_criteria_details(self):
        tpc_id = BuiltIn().get_variable_value("${tpc_id}")
        url = "{0}trade-program-criteria/{1}".format(END_POINT_URL, tpc_id)
        common = APIMethod.APIMethod()
        payload = self.gen_tpc_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        print("payload = " + str(payload))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def gen_tpc_payload(self):
        tpc_br = BuiltIn().get_variable_value("${tpc_br}")
        payload = {}
        payload.update((k, v) for k, v in tpc_br.items())
        return payload
