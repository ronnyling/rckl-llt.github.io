from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class TradeProgramObjectiveDelete(object):
    @keyword('user delete trade program objective details')
    def user_deletes_trade_program_objective_details(self):
        tpo_id = BuiltIn().get_variable_value("${tpo_id}")
        url = "{0}trade-program-objective/{1}".format(END_POINT_URL, tpo_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
