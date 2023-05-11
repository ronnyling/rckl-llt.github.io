from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from faker import Faker
FAKE = Faker()
import datetime
NOW = datetime.datetime.now()

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class HolidaysDelete(object):

    @keyword('user deletes holiday calendar with created data')
    def user_deletes_holiday_calendar_with_created_data(self):
        calendar_id = BuiltIn().get_variable_value("${calendar_id}")
        url = "{0}holiday-calendar/{1}".format(END_POINT_URL, calendar_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)