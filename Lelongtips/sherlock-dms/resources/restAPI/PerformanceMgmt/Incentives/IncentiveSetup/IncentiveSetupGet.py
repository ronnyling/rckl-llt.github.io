import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "performance" + APP_URL

class IncentiveSetupGet(object):

    @keyword('user retrieves incentive setup listing')
    def user_retrieves_incentive_setup_listing(self):
        url = "{0}incentives".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable('${inc_setup_ls}', body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves incentive setup details')
    def user_retrieves_incentive_setup_details(self):
        inc_setup_id = BuiltIn().get_variable_value("${inc_setup_id}")
        if inc_setup_id is None:
            self.user_retrieves_incentive_setup_listing()
            inc_setup_ls = BuiltIn().get_variable_value('${inc_setup_ls}')
            rand_inc = secrets.choice(inc_setup_ls)
            inc_setup_id = rand_inc['ID']
            BuiltIn().set_test_variable("${inc_setup_id}", inc_setup_id)
        url = "{0}incentives/{1}".format(END_POINT_URL, inc_setup_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable('${inc_setup_details}', body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves incentive setup details slabs')
    def user_retrieves_incentive_setup_details_slabs(self):
        inc_setup_id = BuiltIn().get_variable_value("${inc_setup_id}")
        url = "{0}incentives/{1}/slabs".format(END_POINT_URL, inc_setup_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable('${inc_setup_slab_details}', body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_kpi_config(self):
        url = "{0}incentives/kpi/config".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable('${inc_kpi_ls}', body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)