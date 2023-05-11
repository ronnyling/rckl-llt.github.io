
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class TradeProgramDelete(object):
    @keyword('user delete trade program details')
    def user_deletes_trade_program_details(self):
        tp_id = BuiltIn().get_variable_value("${tp_id}")
        url = "{0}trade-program/{1}".format(END_POINT_URL, tp_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user delete objective of criteria for trade program details')
    def user_delete_objective_criteria_trade_program_details(self):
        tp_id = BuiltIn().get_variable_value("${tp_id}")
        criteria_id = BuiltIn().get_variable_value("${criteria_id}")
        objective_id = BuiltIn().get_variable_value("${objective_id}")

        url = "{0}trade-program/{1}/criteria/{2}/objective/{3}".format(END_POINT_URL, tp_id, criteria_id, objective_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
