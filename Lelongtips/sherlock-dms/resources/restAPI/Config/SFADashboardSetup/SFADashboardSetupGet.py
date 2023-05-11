import secrets
from resources.restAPI.Common.TokenAccess import TokenAccess
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Config.SFADashboardSetup import SFADashboardSetupDelete
END_POINT_URL = PROTOCOL + "perf-mgt" + APP_URL

class SFADashboardSetupGet(object):

    @keyword('user retrieves all dashboard data')
    def user_retrieves_all_dashboard(self):
        url = "{0}advance-kpi".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            respond_len = len(response.json())
            for i in range(respond_len):
                if response.json()[i]['DASHBOARD']['DASHBOARD_NAME'] == 'Delivery Dashboard':
                    delivery_dashboard = True
                    delivery_dashboard_id = response.json()[i]['ID']
                    break
                else:
                    delivery_dashboard = False
                    delivery_dashboard_id = ''
            BuiltIn().set_test_variable("${delivery_dashboard}", delivery_dashboard)
            BuiltIn().set_test_variable("${res_bd_dashboard_id}", delivery_dashboard_id)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user gets dashboard by using ${type} id')
    def user_gets_dashboard_by_id(self, type):
        if type=="valid":
            res_bd_dashboard_id = BuiltIn().get_variable_value("${res_bd_dashboard_id}")
        else:
            res_bd_dashboard_id = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45))
        url = "{0}advance-kpi/{1}".format(END_POINT_URL, res_bd_dashboard_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_dashboard_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword('user validates is there any delivery dashboard')
    def user_validate_delivery_dashboard(self):
        TokenAccess().user_retrieves_token_access_as("distadm")
        self.user_retrieves_all_dashboard()
        status = BuiltIn().get_variable_value("${delivery_dashboard}")
        if status == True:
            SFADashboardSetupDelete.SFADashboardSetupDelete().user_deletes_the_created_data("valid")




