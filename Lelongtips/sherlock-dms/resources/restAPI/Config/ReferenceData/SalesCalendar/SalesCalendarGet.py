from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class SalesCalendarGet(object):

    def user_retrieves_all_calendar_data(self):
        url = "{0}profile-principals/HQ/sales-calendar".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            print("response body ", body_result)
            BuiltIn().set_test_variable("${sales_calendar_body_result}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)


    def user_gets_calendar_by_using_id(self):
        calendar_id = BuiltIn().get_variable_value("${calendar_id}")
        url = "{0}profile-principals/HQ/sales-calendar/{1}".format(END_POINT_URL, calendar_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_cal_id = body_result['ID']
            first_mon_id = body_result['MONTHS'][0]['ID']
            first_week_id = body_result['MONTHS'][0]['WEEKS'][0]['ID']
            assert res_cal_id == calendar_id, "ID retrieved not matched"
            print("response body ", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        BuiltIn().set_test_variable("${first_mon_id}", first_mon_id)
        BuiltIn().set_test_variable("${first_week_id}", first_week_id)