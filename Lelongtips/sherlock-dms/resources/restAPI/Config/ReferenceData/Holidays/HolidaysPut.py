from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from datetime import datetime
from faker import Faker
FAKE = Faker()
import datetime
NOW = datetime.datetime.now()

END_POINT_URL = PROTOCOL + "setting" + APP_URL

class HolidaysPut(object):

    @keyword('user updates holiday calendar with created data')
    def user_puts_holiday_calendar_with_created_data(self):
        calendar_id = BuiltIn().get_variable_value("${calendar_id}")
        url = "{0}holiday-calendar/{1}".format(END_POINT_URL, calendar_id)
        payload = self.payload_holiday_calendar_put()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_holiday_calendar_put(self):
        greater_than_current_date = NOW + datetime.timedelta(days=45)
        calendar_name = BuiltIn().get_variable_value("${calendar_name}")
        calendar_name_change = calendar_name + "NEW"
        calendar_type = BuiltIn().get_variable_value("${calendar_type}")
        calendar_entity = BuiltIn().get_variable_value("${calendar_entity}")
        calendar_assignment = BuiltIn().get_variable_value("${calendar_assignment}")
        payload = {

            'HOLIDAY_TYPE': calendar_type,
            'ENTITY': calendar_entity,
            'HOLIDAY_DESC': calendar_name_change,
            'HOLIDAY_DATE': greater_than_current_date.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            'ASSIGNMENT_TYPE': calendar_assignment,

        }
        payload = json.dumps(payload)
        print("Holiday Calendar Payload: ", payload)
        return payload