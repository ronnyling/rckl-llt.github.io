from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import secrets
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class StatePut(object):
    """ Functions to create state record """
    @keyword('user edits state with ${data_type}')
    def user_edits_state_with(self, data_type):
        """ Functions to create state using given/random data"""
        state_id = BuiltIn().get_variable_value("${res_bd_state_id}")
        id_type = BuiltIn().get_variable_value("${ID_TYPE}")
        if id_type:
            state_id = id_type
        url = "{0}module-data/address-state/{1}".format(END_POINT_URL, state_id)
        payload = self.payload_state(data_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_state(self, data_type):
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
        details = BuiltIn().get_variable_value("${state_update_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("State Payload: ", payload)
        return payload
