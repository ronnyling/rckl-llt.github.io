import secrets

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class CountryPut(object):
    """ Functions to create country """

    @keyword('user edits country with ${data_type} by using ${id_type} id')
    def user_edits_country_with(self, data_type, id_type):
        """ Function to create country with random/given data """
        res_bd_country_id = BuiltIn().get_variable_value("${res_bd_country_id}")
        if id_type == "valid":
            url = "{0}module-data/address-country/{1}".format(END_POINT_URL, res_bd_country_id)
        else:
            url = "{0}module-data/address-country/83fj9dx9sdj".format(END_POINT_URL)
        payload = self.payload_country(data_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_country(self, data_type):
        """ Function for country payload content """
        payload = {
            "COUNTRY_CD": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "COUNTRY_NAME": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20))
        }
        details = BuiltIn().get_variable_value("${country_update_details}")
        print("{0}".format(data_type))
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Country Payload: ", payload)
        return payload
