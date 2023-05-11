import json
import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Config.ReferenceData.AgeingTerms import AgeingTermsGet
END_POINT_URL = PROTOCOL + "setting" + APP_URL


class AgeingTermsPut(object):

    @keyword("user updates ageing terms with ${data_type} data")
    def user_updates_aging_term(self, data_type):
        AgeingTermsGet.AgeingTermsGet().user_retrieves_ageing_term()
        res_bd_term_id = BuiltIn().get_variable_value("${res_bd_term_id}")
        url = "{0}aging-term/{1}".format(END_POINT_URL, res_bd_term_id)
        payload = self.payload_term()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_term(self):
        term_id = BuiltIn().get_variable_value("${res_bd_term_id}")
        cd = BuiltIn().get_variable_value("${res_bd_term_cd}")
        start = BuiltIn().get_variable_value("${res_bd_term_sd}")
        end = BuiltIn().get_variable_value("${res_bd_term_ed}")
        payload = {
               "ID": term_id,
               "AGING_CD":cd,
               "AGING_START":start,
               "AGING_END":end,
               "AGING_DESC":''.join(secrets.choice('0123456789') for _ in range(5)),
            }
        details = BuiltIn().get_variable_value("${term_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print(payload)
        return payload






