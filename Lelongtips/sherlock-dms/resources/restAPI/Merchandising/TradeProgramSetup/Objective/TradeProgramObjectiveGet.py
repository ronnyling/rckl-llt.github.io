import secrets

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class TradeProgramObjectiveGet(object):

    @keyword('user retrieves all trade program objectives')
    def user_retrieves_all_trade_program_objectives(self):
        url = "{0}trade-program-objective".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${tpo_ls}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves program objective details')
    def user_retrieves_trade_program_objective_details(self):
        tpo_id = BuiltIn().get_variable_value("${tpo_id}")
        if not tpo_id:
            self.user_retrieves_all_trade_program_objectives()
            tpo_ls = BuiltIn().get_variable_value("${tpo_ls}")
            rand_tpc = secrets.choice(tpo_ls)
            tpo_id = rand_tpc['ID']
        url = "{0}trade-program-objective/{1}".format(END_POINT_URL, tpo_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${tpo_details}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
