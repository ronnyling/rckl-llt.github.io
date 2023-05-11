from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Config.SFADashboardSetup import SFADashboardSetupPost
MODIFIED_DATE = ""
CREATED_DATE = ""
END_POINT_URL = PROTOCOL + "perf-mgt" + APP_URL


class SFADashboardSetupPut(object):

    @keyword('user edits dashboard with ${data_type} data using ${id_type} id')
    def user_edits_dashboard_with(self, data_type, id_type):
        res_bd_dashboard_id = BuiltIn().get_variable_value("${res_bd_dashboard_id}")
        if id_type == "valid":
            url = "{0}advance-kpi/{1}".format(END_POINT_URL, res_bd_dashboard_id)
        else:
            url = "{0}advance-kpi".format(END_POINT_URL)
        payload = SFADashboardSetupPost.SFADashboardSetupPost().payload_dashboard("edit")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

