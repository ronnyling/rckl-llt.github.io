from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import secrets
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from datetime import datetime
from faker import Faker
import datetime
FAKE = Faker()
NOW = datetime.datetime.now()
END_POINT_URL = PROTOCOL + "setting" + APP_URL


class HolidaysPost(object):
    days_to_add = 45

    @keyword('user creates holiday calendar with ${type} data')
    def user_creates_holiday_calendar(self, data_type):
        date = self.get_date(self.days_to_add)
        response = self.create_holiday(date)
        while response == 409:
            self.days_to_add += 1
            date = self.get_date(self.days_to_add)
            response = self.create_holiday(date)

    def get_date(self, day):
        greater_than_current_date = NOW + datetime.timedelta(days=day)
        date = greater_than_current_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        return date

    def create_holiday(self, date):
        url = "{0}holiday-calendar/".format(END_POINT_URL)
        payload = self.payload_holiday_calendar(date)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("Result: ", body_result)
            calendar_id = body_result['ID']
            calender_name = body_result['HOLIDAY_DESC']
            calender_type = body_result['HOLIDAY_TYPE']
            calender_date = body_result['HOLIDAY_DATE']
            calender_entity = body_result['ENTITY']
            calender_assignment = body_result['ASSIGNMENT_TYPE']
            BuiltIn().set_test_variable("${calendar_id}", calendar_id)
            BuiltIn().set_test_variable("${calendar_name}", calender_name)
            BuiltIn().set_test_variable("${calendar_type}", calender_type)
            BuiltIn().set_test_variable("${calendar_date}", calender_date)
            BuiltIn().set_test_variable("${calendar_entity}", calender_entity)
            BuiltIn().set_test_variable("${calendar_assignment}", calender_assignment)
        else:
            print("ResultFail: ", response.status_code)
            print("ResultFailReason: ", response.text)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code

    def payload_holiday_calendar(self, date):
        payload = {
            'HOLIDAY_TYPE': secrets.choice(['State', 'National']),
            'ENTITY': 'HQ',
            'HOLIDAY_DESC': ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            'HOLIDAY_DATE': date,
            'ASSIGNMENT_TYPE': "All",
        }
        details = BuiltIn().get_variable_value("${HC_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Holiday Calendar Payload: ", payload)
        return payload
