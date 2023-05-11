import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class LocalityPut(object):
    """ Functions to edit locality record """

    @keyword('user edits locality with ${data_type}')
    def user_edits_locality_with(self, data_type):
        """ Functions to create edit using fixed/random data"""
        city_id = BuiltIn().get_variable_value("${res_bd_locality_id}")
        id_type = BuiltIn().get_variable_value("${ID_TYPE}")
        if id_type:
            city_id = id_type
        url = "{0}module-data/address-city/{1}".format(END_POINT_URL, city_id)
        payload = self.payload_locality(data_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_locality(self, data_type):
        """ Functions for locality payload content """
        state_id = BuiltIn().get_variable_value("${res_bd_state_id}")
        if state_id is None:
            state_id = None
        else:
            state_id = {
                "ID": state_id
            }
        payload = {
            "CITY_CD": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "CITY_NAME": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
            "STATE": state_id
        }
        details = BuiltIn().get_variable_value("${locality_update_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Locality Payload: ", payload)
        return payload
