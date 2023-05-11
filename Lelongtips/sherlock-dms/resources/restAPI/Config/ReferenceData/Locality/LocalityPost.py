import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, APIAssertion, TokenAccess
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class LocalityPost(object):
    """ Function to create locality with random/fixed data """

    @keyword('user creates locality with ${data_type}')
    def user_creates_locality_with(self, data_type):
        """ Function to create locality with random/fixed data """
        url = "{0}module-data/address-city".format(END_POINT_URL)
        payload = self.payload_locality()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            body_result['STATE'] = BuiltIn().get_variable_value("${res_bd_state_id}")
            BuiltIn().set_test_variable("${res_bd_locality_payload}", body_result)
            res_bd_locality_id = body_result['ID']
            locality_cd = body_result['CITY_CD']
            BuiltIn().set_test_variable("${res_bd_locality_id}", res_bd_locality_id)
            BuiltIn().set_test_variable("${locality_cd}", locality_cd)
            BuiltIn().set_test_variable("${locality}",body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_locality(self):
        """ Function for locality payload content """
        state_id = BuiltIn().get_variable_value("${res_bd_state_id}")
        if state_id is None:
            state_id = None
        else:
            state_id = {
                "ID": state_id
            }
        payload = {
            "CITY_CD": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(4)),
            "CITY_NAME": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
            "STATE": state_id
        }
        details = BuiltIn().get_variable_value("${locality_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("locality Payload: ", payload)
        return payload

    def user_creates_locality_as_prerequisite(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("sysimp")
        self.user_creates_locality_with("random")
        APIAssertion.APIAssertion().expected_return_status_code("201")