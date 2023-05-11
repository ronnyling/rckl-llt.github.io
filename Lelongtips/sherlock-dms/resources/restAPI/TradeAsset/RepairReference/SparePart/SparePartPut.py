import json
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class SparePartPut(object):
    @keyword("user puts to spare part")
    def user_puts_to_spare_part(self):
        sp_id = BuiltIn().get_variable_value("${sp_id}")
        url = "{0}trade-asset/spare-part/{1}".format(END_POINT_URL, sp_id)
        common = APIMethod.APIMethod()
        payload = self.gen_spare_part_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code), response.json()

    def gen_spare_part_payload(self):
        sp_details = BuiltIn().get_variable_value("${sp_details}")
        payload = {}
        payload.update((k, v) for k, v in sp_details.items())
        return payload
