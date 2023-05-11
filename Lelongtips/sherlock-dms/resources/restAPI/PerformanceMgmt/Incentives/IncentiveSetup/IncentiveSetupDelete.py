from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "performance" + APP_URL


class IncentiveSetupDelete(object):
    @keyword('user deletes incentive setup details')
    def user_deletes_incentive_setup(self):
        inc_setup_id = BuiltIn().get_variable_value("${inc_setup_id}")
        url = "{0}incentives/{1}".format(END_POINT_URL, inc_setup_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
