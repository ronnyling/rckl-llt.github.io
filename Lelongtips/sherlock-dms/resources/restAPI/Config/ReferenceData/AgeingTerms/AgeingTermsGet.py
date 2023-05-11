from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class AgeingTermsGet(object):

    def user_retrieves_all_ageing_terms(self):
        url = "{0}aging-term".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_ageing_term(self):
        res_bd_term_id = BuiltIn().get_variable_value("${res_bd_term_id}")
        url = "{0}aging-term/{1}".format(END_POINT_URL, res_bd_term_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            BuiltIn().set_test_variable("${res_bd_term_id}", response.json()['ID'])
            BuiltIn().set_test_variable("${res_bd_term_cd}", response.json()['AGING_CD'])
            BuiltIn().set_test_variable("${res_bd_term_sd}", response.json()['AGING_START'])
            BuiltIn().set_test_variable("${res_bd_term_ed}", response.json()['AGING_END'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)
