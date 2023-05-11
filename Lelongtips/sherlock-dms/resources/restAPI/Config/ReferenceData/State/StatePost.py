import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, APIAssertion, TokenAccess
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class StatePost(object):
    """ Functions to create state record """

    @keyword('user creates state with ${data_type}')
    def user_creates_state_with(self, data_type):
        """ Functions to create state using fixed/random data"""
        url = "{0}module-data/address-state".format(END_POINT_URL)
        payload = self.payload_state()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            body_result['COUNTRY'] = BuiltIn().get_variable_value("${res_bd_country_id}")
            if body_result['_UNIQUES']:
                body_result.pop('_UNIQUES')
            BuiltIn().set_test_variable("${res_bd_state_payload}", body_result)
            res_bd_state_id = body_result['ID']
            state_cd = body_result['STATE_CD']
            BuiltIn().set_test_variable("${state}",body_result)
            BuiltIn().set_test_variable("${state_cd}", state_cd)
            BuiltIn().set_test_variable("${state_name}", body_result['STATE_NAME'])
            BuiltIn().set_test_variable("${res_bd_state_id}", res_bd_state_id)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_state(self):
        """ Functions for state payload content """
        country_id = BuiltIn().get_variable_value("${res_bd_country_id}")
        if country_id is None:
            country_id = None
        else:
            country_id = {
                "ID": country_id
            }
        payload = {
            "STATE_CD": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "STATE_NAME": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
            "COUNTRY": country_id
        }
        details = BuiltIn().get_variable_value("${state_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("State Payload: ", payload)
        return payload

    def user_creates_state_as_prerequisite(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("sysimp")
        self.user_creates_state_with("random")
        APIAssertion.APIAssertion().expected_return_status_code("201")

