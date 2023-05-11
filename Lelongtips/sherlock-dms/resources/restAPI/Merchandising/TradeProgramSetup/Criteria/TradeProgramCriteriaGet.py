import secrets

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class TradeProgramCriteriaGet(object):

    @keyword('user retrieves all trade program criterias')
    def user_retrieves_all_trade_program_criterias(self):
        url = "{0}trade-program-criteria".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${tpc_ls}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves program criteria details')
    def user_retrieves_trade_program_criteria_details(self):
        tpc_id = BuiltIn().get_variable_value("${tpc_id}")
        if not tpc_id:
            self.user_retrieves_all_trade_program_criterias()
            tpc_ls = BuiltIn().get_variable_value("${tpc_ls}")
            rand_tpc = secrets.choice(tpc_ls)
            tpc_id = rand_tpc['ID']
        url = "{0}trade-program-criteria/{1}".format(END_POINT_URL, tpc_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${tpc_details}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
