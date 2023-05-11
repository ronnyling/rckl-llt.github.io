import json
import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.PerformanceMgmt.Incentives.IncentiveProgram.IncentiveProgramGet import IncentiveProgramGet
from resources.restAPI.PerformanceMgmt.Incentives.IncentiveSetup.IncentiveSetupPost import IncentiveSetupPost
from resources.restAPI.PerformanceMgmt.Incentives.IncentiveSetup.IncentiveSetupPut import IncentiveSetupPut

END_POINT_URL = PROTOCOL + "performance" + APP_URL


class IncentiveProgramPost(object):
    @keyword('user posts for incentive program')
    def user_posts_for_incentive_program(self):
        url = "{0}incentive-programs".format(END_POINT_URL)
        payload = self.gen_inc_program_payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, json.dumps(payload))
        print("payload = ", str(json.dumps(payload)))
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable('${inc_program_br}', body_result)
            BuiltIn().set_test_variable('${inc_program_id}', body_result['ID'])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def gen_inc_program_payload(self):
        IncentiveProgramGet().user_retrieve_confirmed_incentive_setup_for_route()
        cfm_inc_setup_ls = BuiltIn().get_variable_value('${cfm_inc_setup_ls}')
        tries = 0
        while tries < 3 and len(cfm_inc_setup_ls) < 1:
            IncentiveSetupPost().user_posts_for_incentive_setup()
            IncentiveSetupPost().user_posts_to_incentive_setup_details_slabs()
            IncentiveSetupPut().user_puts_for_incentive_setup("confirm")
            IncentiveProgramGet().user_retrieve_confirmed_incentive_setup_for_route()
            cfm_inc_setup_ls = BuiltIn().get_variable_value('${cfm_inc_setup_ls}')
            tries += 1
        valid_inc = [inc for inc in cfm_inc_setup_ls if inc['INC_MTH_FROM'] != "00"]
        rand_inc = secrets.choice(valid_inc)
        inc_details = rand_inc

        payload = {
            "INC_PROGRAM_CD": "INCPROG" + ''.join(secrets.choice('0123456789ABCDEF') for _ in range(13)),
            "INC_PROGRAM_FOR": "R",
            "INC_PROGRAM_DESC": ''.join(secrets.choice('0123456789ABCDEF') for _ in range(10)),
            "INC_PROGRAM_YEAR": inc_details['INC_YEAR'],
            "INC_PROGRAM_MTH_FROM": inc_details['INC_MTH_FROM'],
            "INC_PROGRAM_MTH_TO": inc_details['INC_MTH_TO'],
            "DIST_ID": inc_details['DIST_ID'],
            "STATUS": "A",
            "INCENTIVES": [
                {
                    "INC_ID": inc_details['INC_ID']
                }
            ]
        }
        return payload
