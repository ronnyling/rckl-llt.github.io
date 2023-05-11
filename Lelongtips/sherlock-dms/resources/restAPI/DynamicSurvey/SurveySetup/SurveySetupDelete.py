from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL

END_POINT_URL = PROTOCOL + "dynamic-survey" + APP_URL


class SurveySetupDelete(object):
    SURVEY_ID = "${res_bd_survey_id}"

    def user_deletes_created_survey_setup(self):
        survey_id = BuiltIn().get_variable_value(self.SURVEY_ID)
        url = "{0}dynamic-survey/{1}".format(END_POINT_URL, survey_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        assert response.status_code == 204, "Survey setup not deleted"
