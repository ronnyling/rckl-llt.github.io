import json
import secrets
import datetime

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL

END_POINT_URL = PROTOCOL + "dynamic-survey" + APP_URL


class SurveySetupPost(object):

    @keyword("user add survey with ${data_type} data")
    def user_add_survey_using_data(self, data_type):
        url = "{0}dynamic-survey".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.payload(data_type)
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload)
        response.status_code == 201
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            res_bd_survey_id = response.json()['ID']
            BuiltIn().set_test_variable("${res_bd_survey_id}", res_bd_survey_id)

    def payload(self, data_type):
        details = BuiltIn().get_variable_value("${survey_details}")
        if data_type == 'fixed':
            survey_desc = details['SURVEY_DESC']
            survey_title = details['SURVEY_TITLE']
            survey_date = details['SURVEY_START_DATE']
        else:
            survey_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            survey_title = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
            survey_date = datetime.datetime.now() + datetime.timedelta(days=1)
            survey_date = survey_date.strftime('%Y-%m-%d')
        payload = {
            "ROW_HEIGHT": 1,
            "START_DATE": survey_date,
            "STATUS": "A",
            "SURVEY_DESC": survey_desc,
            "SURVEY_OBJECTIVE": "S",
            "SURVEY_TITLE": survey_title,
            "SURVEY_TYPE": "F"
        }
        print("PAYLOAD IS: ", payload)
        BuiltIn().set_test_variable("${survey_setup_payload}", payload)
        return payload
