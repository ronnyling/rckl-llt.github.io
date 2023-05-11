import json
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.PerformanceMgmt.Incentives.IncentiveProgram.IncentiveProgramGet import IncentiveProgramGet

END_POINT_URL = PROTOCOL + "performance" + APP_URL


class IncentiveProgramPut(object):
    @keyword('user puts to ${operation} incentive program')
    def user_puts_for_incentive_setup(self, operation):
        inc_program_id = BuiltIn().get_variable_value('${inc_program_id}')
        IncentiveProgramGet().user_retrieves_incentive_program_details()
        payload = BuiltIn().get_variable_value('${inc_program_details}')
        url = "{0}incentive-programs/{1}".format(END_POINT_URL, inc_program_id)
        common = APIMethod.APIMethod()
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        print("payload = ", str(payload))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
