from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.ReferenceData.SalesCalendar.SalesCalendarGet import SalesCalendarGet
import secrets
import calendar
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from faker import Faker
import datetime
FAKE = Faker()


NOW = datetime.datetime.now()

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class SalesCalendarPost(object):
    WEEKEND_DAY = "${weekend_day}"
    DATE_FORMAT = "%Y-%m-%d"
    DATE_TIME_FORMAT = "%Y-%m-%dT00:00:00.000Z"

    @keyword('user creates month with ${data_type} data')
    def user_creates_sales_calendar_month(self, data_type):
        url = "{0}profile-principals/HQ/sales-calendar/generateData/".format(END_POINT_URL)
        details = BuiltIn().get_variable_value("${weekend_details}")
        weekend_day = details["CALENDAR_WEEK_END_DAY"]
        BuiltIn().set_test_variable(self.WEEKEND_DAY, weekend_day)
        payload = self.payload_calendar_month_generate(weekend_day)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("Result: ", body_result)
            BuiltIn().set_test_variable("${response_body}", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def payload_calendar_month_generate(self, weekend_day):
        date = self.return_latest_start_and_end_date("date time format")
        payload = {
            "CALENDAR_NAME": ''.join(secrets.choice('A1B2CD3EF4GHI5JKLM6NOPQ7R8STUV9WXY0Z') for _ in range(50)),
            "CALENDAR_START_DATE": date[0],
            "CALENDAR_END_DATE": date[1],
            "CALENDAR_WEEK_END_DAY": weekend_day,
            "CALENDAR_MODE": "Auto"
        }
        details = BuiltIn().get_variable_value("${month_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Month Payload: ", payload)
        return payload

    @keyword('user creates sales calendar selecting auto mode with ${data_type} data')
    def user_creates_sales_calendar(self, data_type):
        url = "{0}profile-principals/HQ/sales-calendar/".format(END_POINT_URL)
        payload = self.payload_sales_calendar()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("Result: ", body_result)
            calendar_id = body_result['ID']
            BuiltIn().set_test_variable("${calendar_id}", calendar_id)
        else:
            print("ResultFail: ", response.status_code)
            print("ResultFailReason: ", response.text)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def return_latest_start_and_end_date(self, date_format):

        if date_format == "date":
            date_format = self.DATE_FORMAT
        else:
            date_format = self.DATE_TIME_FORMAT
        SalesCalendarGet().user_retrieves_all_calendar_data()
        all_calendar = BuiltIn().get_variable_value("${sales_calendar_body_result}")
        highest = 0
        for item in all_calendar:
            if highest == 0:
                highest = item['CALENDAR_END_DATE']
            else:
                if item['CALENDAR_END_DATE'] > highest:
                    highest = item['CALENDAR_END_DATE']
        highest = datetime.datetime.strptime(highest, self.DATE_FORMAT)
        start_date = str((highest + datetime.timedelta(days=1)).strftime(date_format))
        end_date_time = str((highest + datetime.timedelta(days=365)).strftime(date_format))
        end_date = end_date_time
        if "T" in end_date:
            end_date = end_date.split("T")
            end_date = end_date[0].split("-")
            last_day_of_month = calendar.monthrange(int(end_date[0]), int(end_date[1]))[1]
            end_date_time = end_date_time.replace("{0}T".format(end_date[2]), "{0}T".format(last_day_of_month))
        else:
            end_date = end_date.split("-")
            last_day_of_month = calendar.monthrange(int(end_date[0]), int(end_date[1]))[1]
            end_date_time = end_date_time.replace(end_date[2], str(last_day_of_month))
        return start_date, end_date_time

    def payload_sales_calendar(self):
        months = BuiltIn().get_variable_value("${response_body}")
        weekend_day = BuiltIn().get_variable_value(self.WEEKEND_DAY)
        date = self.return_latest_start_and_end_date('date')
        payload = {
            "CALENDAR_NAME": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(50)),
            "PRINCIPAL_ID": "HQ",
            "CALENDAR_START_DATE": date[0],
            "CALENDAR_END_DATE": date[1],
            "CALENDAR_WEEK_END_DAY": weekend_day,
            "CALENDAR_MODE": "Auto",
            "CALENDAR_YEAR": "2024",
            "MONTHS": months
        }
        details = BuiltIn().get_variable_value("${sales_calendar_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Sales Calendar Payload: ", payload)
        return payload

    @keyword('user creates sales calendar selecting manual mode with ${data_type} data')
    def user_creates_sales_calendar_manual(self, data_type):
        url = "{0}profile-principals/HQ/sales-calendar/".format(END_POINT_URL)
        details = BuiltIn().get_variable_value("${weekend_details}")
        weekend_day = details["CALENDAR_WEEK_END_DAY"]
        BuiltIn().set_test_variable(self.WEEKEND_DAY, weekend_day)
        payload = self.payload_sales_calendar_manual(weekend_day)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            calendar_id = body_result['ID']
            BuiltIn().set_test_variable("${calendar_id}", calendar_id)
        else:
            print("ResultFail: ", response.status_code)
            print("ResultFailReason: ", response.text)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def payload_sales_calendar_manual(self, weekend_day):
        start_date, end_date, first_month_end_dt, first_no_days, \
        sec_month_start_date, sec_no_days = self.date_calculation()
        payload = {
            "CALENDAR_NAME": ''.join(secrets.choice('ABCDEFGHIJKLMNOP') for _ in range(50)),
            "PRINCIPAL_ID": "HQ",
            "CALENDAR_START_DATE": str(start_date),
            "CALENDAR_END_DATE":  str(end_date),
            "CALENDAR_WEEK_END_DAY":  str(weekend_day),
            "CALENDAR_YEAR": "2024",
            "CALENDAR_MODE": "Manual",
            "MONTHS": [
                {
                    "CALENDAR_MONTH": 1,
                    "CALENDAR_MONTH_START_DATE":  str(start_date),
                    "CALENDAR_MONTH_END_DATE":  str(end_date),
                    "CALENDAR_MONTH_QUARTER": "Q1",
                    "CALENDAR_MONTH_HALF_YEARLY": "H1",
                    "CALENDAR_MONTH_NO_DAYS":  first_no_days,
                    "WEEKS": [
                        {
                            "CALENDAR_WEEK_NO": 1,
                            "CALENDAR_WEEK_START_DATE":  str(start_date),
                            "CALENDAR_WEEK_END_DATE":  str(end_date)
                        }
                    ]
                }
            ]
        }
        payload = json.dumps(payload)
        print("Sales Calendar Payload: ", payload)
        return payload

    def date_calculation(self):
        date = self.return_latest_start_and_end_date('date')
        start_date = date[0]
        st_year, st_month, start_day = start_date.split('-')
        start_day = datetime.datetime.strptime(start_day, "%d")
        end_date = date[1]
        first_month_end_dt = str((start_day + datetime.timedelta(days=2)).strftime(self.DATE_FORMAT))
        first_no_days = ( datetime.datetime.strptime(end_date, self.DATE_FORMAT) -
                          datetime.datetime.strptime(start_date, self.DATE_FORMAT)).days
        first_no_days = int(first_no_days) + 1
        sec_month_start_date = str((start_day + datetime.timedelta(days=3)).strftime(self.DATE_FORMAT))
        return start_date, end_date, first_month_end_dt, first_no_days, sec_month_start_date, 4
