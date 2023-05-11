""" Python File related to HHT DynamicSurvey API """
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.Common import Common
import json

APP_URL_1_0 = '-svc-qa.cfapps.jp10.hana.ondemand.com/api/v1.0/'
DYNAMIC_SURVEY_END_POINT_URL = PROTOCOL + "dynamic-survey"
MOBILE_END_POINT_URL = PROTOCOL + "mobile-comm-general"

class DynamicSurveyGet:
    """ Functions related to HHT DynamicSurvey GET/SYNC Request """

    @keyword("user retrieves Dynamic Survey Header using ${user_file}")
    def get_dynamic_survey(self, user_file):
        url = "{0}comm/dynamic-survey".format(DYNAMIC_SURVEY_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Dynamic Survey Customer using ${user_file}")
    def get_dynamic_survey_customer(self, user_file):
        url = "{0}comm/dynamic-survey-cust".format(DYNAMIC_SURVEY_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Dynamic Survey Question Score using ${user_file}")
    def get_dynamic_survey_question_score(self, user_file):
        url = "{0}comm/dynamic-survey-question-score".format(DYNAMIC_SURVEY_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Dynamic Survey Subject using ${user_file}")
    def get_dynamic_survey_subject(self, user_file):
        url = "{0}comm/dynamic-survey-subject".format(DYNAMIC_SURVEY_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Dynamic Survey Answer Option using ${user_file}")
    def get_dynamic_survey_answer_option(self, user_file):
        url = "{0}comm/dynamic-survey-answer-option".format(DYNAMIC_SURVEY_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Dynamic Survey Question using ${user_file}")
    def get_dynamic_survey_question(self, user_file):
        url = "{0}comm/dynamic-survey-question".format(DYNAMIC_SURVEY_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Dynamic Survey History using ${user_file}")
    def get_dynamic_survey_history(self, user_file):
        url = "{0}comm/dynamic-survey-history".format(DYNAMIC_SURVEY_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Dynamic Survey JSON File")
    def get_dynamic_survey_json_file(self):
        url = "{0}comm/attachment/dynamic-survey".format(DYNAMIC_SURVEY_END_POINT_URL + APP_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)
