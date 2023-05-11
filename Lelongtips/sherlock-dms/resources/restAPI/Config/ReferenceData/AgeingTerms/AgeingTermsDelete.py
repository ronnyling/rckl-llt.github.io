from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, APIAssertion
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class AgeingTermsDelete(object):

    def user_deletes_created_ageing_terms(self):
        res_bd_term_id = BuiltIn().get_variable_value("${res_bd_term_id}")
        url = "{0}aging-term/{1}".format(END_POINT_URL, res_bd_term_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
