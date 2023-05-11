import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "perf-mgt" + APP_URL


class SFADashboardSetupDelete(object):

    @keyword('user deletes the created dashboard with ${type} id')
    def user_deletes_the_created_data(self, type):
        if type == "valid":
            res_bd_dashboard_id = BuiltIn().get_variable_value("${res_bd_dashboard_id}")
        else:
            res_bd_dashboard_id = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45))
        url = "{0}advance-kpi/{1}".format(END_POINT_URL, res_bd_dashboard_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

