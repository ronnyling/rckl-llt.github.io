import secrets

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, APIAssertion, TokenAccess
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class CountryPost(object):
    """ Functions to create country """

    @keyword('user creates country with ${data_type}')
    def user_creates_country_with(self, data_type):
        """ Function to create country with random/fixed data """
        url = "{0}module-data/address-country".format(END_POINT_URL)
        payload = self.payload_country()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            if body_result['_UNIQUES']:
                body_result.pop('_UNIQUES')
            BuiltIn().set_test_variable("${res_bd_country_payload}", body_result)
            country_name = body_result['COUNTRY_NAME']
            BuiltIn().set_test_variable("${country_name}", country_name)
            res_bd_country_id = body_result['ID']
            BuiltIn().set_test_variable("${country}", body_result)
            country_cd = body_result['COUNTRY_CD']
            BuiltIn().set_test_variable("${country_cd}", country_cd)
            BuiltIn().set_test_variable("${res_bd_country_id}", res_bd_country_id)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_country(self):
        """ Function for country payload content """
        payload = {
            "COUNTRY_CD": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "COUNTRY_NAME": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20))
        }
        details = BuiltIn().get_variable_value("${country_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Country Payload: ", payload)
        return payload

    def user_creates_country_as_prerequisite(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("sysimp")
        self.user_creates_country_with("random")
        APIAssertion.APIAssertion().expected_return_status_code("201")
