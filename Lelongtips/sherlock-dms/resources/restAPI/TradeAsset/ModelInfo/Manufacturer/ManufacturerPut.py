import json
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ManufacturerPut(object):
    @keyword("user puts to manufacturer")
    def user_puts_to_manufacturer(self):
        manu_id = BuiltIn().get_variable_value("${manu_id}")
        url = "{0}trade-asset/asset-manufacturer/{1}".format(END_POINT_URL, manu_id)
        common = APIMethod.APIMethod()
        payload = self.gen_manu_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print("payload = " + str(payload))
        return str(response.status_code), response.json()

    def gen_manu_payload(self):
        manu_details = BuiltIn().get_variable_value("${manu_details}")
        payload = {}
        payload.update((k, v) for k, v in manu_details.items())
        return payload
