import json
import secrets
import datetime

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL

END_POINT_URL = PROTOCOL + "dynamic-survey" + APP_URL


class SurveySetupPut(object):
    SURVEY_ID = "${res_bd_survey_id}"

    @keyword("user updates created survey setup with ${data_type} data")
    def user_update_survey_using_data(self, data_type):
        survey_id = BuiltIn().get_variable_value(self.SURVEY_ID)
        url = "{0}dynamic-survey/{1}".format(END_POINT_URL, survey_id)
        common = APIMethod.APIMethod()
        payload = self.payload_update(data_type)
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        response.status_code == 201
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_update(self, data_type):
        survey_id = BuiltIn().get_variable_value(self.SURVEY_ID)
        payload = BuiltIn().get_variable_value("${survey_setup_payload}")
        new_payload = {"ID": survey_id}
        payload.update(new_payload)
        if data_type == 'fixed':
            details = BuiltIn().get_variable_value("${survey_update_details}")
        else:
            survey_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            survey_title = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
            details = {
                "SURVEY_DESC": survey_desc,
                "SURVEY_TITLE": survey_title
            }
        payload.update((k, v) for k, v in details.items())
        print("PAYLOAD UPDATE IS: ", payload)
        return payload
