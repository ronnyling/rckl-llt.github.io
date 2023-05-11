from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod, APIAssertion

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class SalesCalendarDelete(object):

    def user_deletes_sales_calendar_with_created_data(self):
        """ Function to delete sales calendar with valid data """
        calendar_id = BuiltIn().get_variable_value("${calendar_id}")
        url = "{0}profile-principals/HQ/sales-calendar/{1}".format(END_POINT_URL, calendar_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_deletes_created_sales_calendar_as_teardown(self):
        self.user_deletes_sales_calendar_with_created_data()
        APIAssertion.APIAssertion().expected_return_status_code("200")
