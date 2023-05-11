import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "dynamic-survey" + APP_URL


class SurveySetupGet(object):

    @keyword('user retrieves all dynamic survey result')
    def user_retrieves_all_dynamic_survey_result(self):
        url = "{0}dynamic-survey-results".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_survey = secrets.choice(range(0, len(body_result)))
            else:
                rand_survey = 0
            BuiltIn().set_test_variable("${res_bd_survey_result_id}", body_result[rand_survey]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves dynamic survey result details')
    def user_gets_survey_result_details(self):
        res_bd_survey_id = BuiltIn().get_variable_value("${res_bd_survey_result_id}")
        url = "{0}dynamic-survey-results/{1}".format(END_POINT_URL, res_bd_survey_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_survey_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)