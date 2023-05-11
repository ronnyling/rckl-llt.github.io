import json
import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class AgeingTermsPost(object):

    @keyword("user creates ageing terms with ${data_type} data")
    def user_creates_ageing_terms_using_data(self, data_type):
        url = "{0}aging-term".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.payload_term()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            res_bd_term_id = response.json()['ID']
            res_bd_term_cd = response.json()['AGING_CD']
            BuiltIn().set_test_variable("${res_bd_term_id}", res_bd_term_id)
            BuiltIn().set_test_variable("${res_bd_term_cd}", res_bd_term_cd)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_term(self):
        start = secrets.choice(range(30, 100))
        end = start+10
        payload = {
               "AGING_START": str(start),
               "AGING_END": str(end),
               "AGING_DESC":''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
        }
        details = BuiltIn().get_variable_value("${term_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print(payload)
        return payload
