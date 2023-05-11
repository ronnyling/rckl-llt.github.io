import json
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class RepairFacilityPut(object):
    @keyword("user puts to repair facility")
    def user_puts_to_repair_facility(self):
        rf_id = BuiltIn().get_variable_value("${rf_id}")
        url = "{0}trade-asset/repair-facility/{1}".format(END_POINT_URL, rf_id)
        common = APIMethod.APIMethod()
        payload = self.gen_repair_facility_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code), response.json()

    def gen_repair_facility_payload(self):
        rf_details = BuiltIn().get_variable_value("${rf_details}")
        payload = {}
        payload.update((k, v) for k, v in rf_details.items())
        return payload
