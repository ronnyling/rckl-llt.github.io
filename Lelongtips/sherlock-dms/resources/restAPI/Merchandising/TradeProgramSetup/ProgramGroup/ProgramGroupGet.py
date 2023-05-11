import secrets

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL

class ProgramGroupGet(object):

    @keyword('user retrieves all program groups')
    def user_retrieves_all_program_groups(self):
        url = "{0}trade-program-group".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${tpg_ls}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves program group details')
    def user_retrieves_trade_program_details(self):
        tpg_id = BuiltIn().get_variable_value("${tpg_id}")
        if not tpg_id:
            self.user_retrieves_all_program_groups()
            tpg_ls = BuiltIn().get_variable_value("${tpg_ls}")
            rand_tp = secrets.choice(tpg_ls)
            tpg_id = rand_tp['ID']
        url = "{0}trade-program-group/{1}".format(END_POINT_URL, tpg_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${tpg_details}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
