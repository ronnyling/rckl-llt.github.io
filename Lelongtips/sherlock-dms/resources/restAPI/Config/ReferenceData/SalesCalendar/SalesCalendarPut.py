from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import secrets
import json
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Config.ReferenceData.SalesCalendar import SalesCalendarPost
import datetime
from robot.api.deco import keyword
FAKE = Faker()



NOW = datetime.datetime.now()

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class SalesCalendarPut(object):
    @keyword('user updates sales calendar with ${data_type} data')
    def user_updates_sales_calendar_manual(self, data_type):
        calendar_id = BuiltIn().get_variable_value("${calendar_id}")
        url = "{0}profile-principals/HQ/sales-calendar/{1}".format(END_POINT_URL, calendar_id)
        details = BuiltIn().get_variable_value("${weekend_details}")
        weekend_day = details["CALENDAR_WEEK_END_DAY"]
        payload = self.payload_sales_calendar_update(weekend_day)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("Result: ", body_result)
            calendar_name = body_result['CALENDAR_NAME']
            BuiltIn().set_test_variable("${calendar_name}", calendar_name)
        else:
            print("ResultFail: ", response.status_code)
            print("ResultFailReason: ", response.text)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_sales_calendar_update(self, weekend_day):
        first_mon_id = BuiltIn().get_variable_value("${first_mon_id}")
        first_week_id = BuiltIn().get_variable_value("${first_week_id}")
        dates = SalesCalendarPost.SalesCalendarPost().date_calculation()
        start_date = dates[0]
        end_date = dates[1]
        first_no_days = dates[3]

        payload = {
            "CALENDAR_NAME": ''.join(secrets.choice('ABCDEFGHIJKLMNOP') for _ in range(50)),
            "PRINCIPAL_ID": "HQ",
            "CALENDAR_START_DATE": start_date,
            "CALENDAR_END_DATE": end_date,
            "CALENDAR_WEEK_END_DAY": weekend_day,
            "CALENDAR_MODE": "Manual",
            "MONTHS": [
                {
                    "CALENDAR_MONTH": 1,
                    "ID": first_mon_id,
                    "IS_DELETED": False,
                    "CALENDAR_MONTH_START_DATE": start_date,
                    "CALENDAR_MONTH_END_DATE": end_date,
                    "CALENDAR_MONTH_QUARTER": "Q1",
                    "CALENDAR_MONTH_HALF_YEARLY": secrets.choice(["H1"]),
                    "CALENDAR_MONTH_NO_DAYS": first_no_days,
                    "WEEKS": [
                        {
                            "CALENDAR_WEEK_NO": 1,
                            "ID": first_week_id,
                            "IS_DELETED": False,
                            "CALENDAR_WEEK_START_DATE": start_date,
                            "CALENDAR_WEEK_END_DATE": end_date
                        }
                    ]
                }
            ]
        }
        details = BuiltIn().get_variable_value("${update_month_quarter}")
        if details:
            payload["MONTHS"][0].update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Sales Calendar Updated Payload: ", payload)
        return payload
