import json
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "performance" + APP_URL


class IncentiveSetupPut(object):
    @keyword('user puts to ${operation} incentive setup')
    def user_puts_for_incentive_setup(self, operation):
        inc_setup_br = BuiltIn().get_variable_value('${inc_setup_br}')
        inc_setup_id = BuiltIn().get_variable_value('${inc_setup_id}')
        if operation == "save":
            inc_setup_br['STATUS'] = "O"
        elif operation == "confirm":
            inc_setup_br['STATUS'] = "C"

        url = "{0}incentives/{1}".format(END_POINT_URL, inc_setup_id)
        common = APIMethod.APIMethod()
        inc_setup_br = json.dumps(inc_setup_br)
        response = common.trigger_api_request("PUT", url, inc_setup_br)
        print("payload = ", str(inc_setup_br))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
