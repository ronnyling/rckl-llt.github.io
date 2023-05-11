import datetime
import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "performance" + APP_URL


class IncentiveProgramGet(object):
    @keyword('user retrieves incentive program listing')
    def user_retrieves_incentive_program_listing(self):
        url = "{0}incentive-programs".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable('${inc_program_ls}', body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves incentive program details')
    def user_retrieves_incentive_program_details(self):
        inc_program_id = BuiltIn().get_variable_value("${inc_program_id}")
        if inc_program_id is None:
            self.user_retrieves_incentive_program_listing()
            inc_program_ls = BuiltIn().get_variable_value('${inc_program_ls}')
            rand_inc = secrets.choice(inc_program_ls)
            inc_program_id = rand_inc['ID']
            BuiltIn().set_test_variable("${inc_program_id}", inc_program_id)
        url = "{0}incentive-programs/{1}".format(END_POINT_URL, inc_program_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable('${inc_program_details}', body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves incentive program details assignments')
    def user_retrieves_incentive_program_details_assignments(self):
        inc_program_id = BuiltIn().get_variable_value("${inc_program_id}")
        url = "{0}incentive-programs/{1}/assignments".format(END_POINT_URL, inc_program_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable('${inc_program_assignments_details}', body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieve_confirmed_incentive_setup_for_route(self):
        next_month = (datetime.datetime.today() + datetime.timedelta(days=31))
        url = "{0}incentives-kpi?inc_for=R&status=C&year={1}".format(END_POINT_URL, next_month.strftime('%Y'))
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable('${cfm_inc_setup_ls}', body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
