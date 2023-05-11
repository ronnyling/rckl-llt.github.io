import secrets

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL

class TradeProgramGet(object):

    @keyword('user retrieves all trade programs')
    def user_retrieves_all_trade_programs(self):
        url = "{0}trade-program".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${tp_ls}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves trade program details')
    def user_retrieves_trade_program_details(self):
        tpg_id = BuiltIn().get_variable_value("${tp_id}")
        if not tpg_id:
            self.user_retrieves_all_trade_programs()
            tpg_ls = BuiltIn().get_variable_value("${tp_ls}")
            rand_tp = secrets.choice(tpg_ls)
            tpg_id = rand_tp['ID']
        url = "{0}trade-program/{1}".format(END_POINT_URL, tpg_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${tp_details}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_all_criterias_for_trade_program(self):
        url = "{0}trade-program-criteria".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${tp_criteria_ls}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves criteria for trade program details')
    def user_retrieves_criteria_program_group_details(self):
        tp_id = BuiltIn().get_variable_value("${tp_id}")
        if not tp_id:
            self.user_retrieves_all_trade_programs()
            tp_ls = BuiltIn().set_test_variable("${tp_ls}")
            rand_tp = secrets.choice(tp_ls)
            tp_id = rand_tp['ID']
        url = "{0}trade-program/{1}/criteria".format(END_POINT_URL, tp_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${criteria_tp_details}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves objective of criteria for trade program details')
    def user_retrieves_objective_criteria_trade_program_details(self):
        tp_id = BuiltIn().get_variable_value("${tp_id}")
        criteria_id = BuiltIn().get_variable_value("${criteria_id}")

        url = "{0}trade-program/{1}/criteria/{2}/objective".format(END_POINT_URL, tp_id, criteria_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${ojective_criteria_tp_details}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_all_criterias(self):
        url = "{0}trade-program-criteria".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${criteria_ls}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_all_objectives(self):
        url = "{0}trade-program-objective".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${objective_ls}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
