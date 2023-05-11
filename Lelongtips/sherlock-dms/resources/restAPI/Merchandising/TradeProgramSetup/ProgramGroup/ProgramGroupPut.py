import json

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.Merchandising.TradeProgramSetup.ProgramGroup.ProgramGroupPost import ProgramGroupPost

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ProgramGroupPut(object):
    @keyword('user puts to program group details')
    def user_put_to_program_group_details(self):
        tpg_id = BuiltIn().get_variable_value("${tpg_id}")
        url = "{0}trade-program-group/{1}".format(END_POINT_URL, tpg_id)
        common = APIMethod.APIMethod()
        payload = self.gen_tpg_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        print("payload = " + str(payload))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def gen_tpg_payload(self):
        tpg_br = BuiltIn().get_variable_value("${tpg_br}")
        if tpg_br is None:
            ProgramGroupPost().user_post_to_program_group
            tpg_br = BuiltIn().get_variable_value("${tpg_br}")

        payload = {}
        payload.update((k, v) for k, v in tpg_br.items())
        payload['TP_COUNT'] = len(payload['TP_RECORDS'])
        delete_assignment = BuiltIn().get_variable_value("${delete_assignment}")
        if delete_assignment:
            payload['TP_RECORDS'] = []
            BuiltIn().set_test_variable("${delete_assignment}", False)
        return payload
