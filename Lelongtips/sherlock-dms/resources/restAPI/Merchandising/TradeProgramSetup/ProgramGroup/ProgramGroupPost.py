import json
import secrets

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.Merchandising.TradeProgramSetup.ProgramGroup.ProgramGroupGet import ProgramGroupGet

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ProgramGroupPost(object):
    @keyword('user post to program group')
    def user_post_to_program_group(self):
        url = "{0}trade-program-group".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_tpg_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload)
        print("payload = " + str(payload))
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${tpg_br}", body_result)
            BuiltIn().set_test_variable("${tpg_id}", body_result['ID'])
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def gen_tpg_payload(self):
        ProgramGroupGet().user_retrieves_trade_program_details()
        tpg_details = BuiltIn().get_variable_value("${tpg_details}")

        payload = {
            "ALLOW_OVERLAP_IND": True,
            "PG_CD": "TP" + ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8)),
            "PG_DESC": "desc" + ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "TP_RECORDS": [
                {
                    "TP_ID": tpg_details['ID']
                }
            ]
        }
        return payload
