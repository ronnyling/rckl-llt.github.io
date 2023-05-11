import json
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class PreventiveMaintenancePut(object):
    @keyword("user puts to preventive maintenance")
    def user_puts_to_preventive_maintenance(self):
        pm_id = BuiltIn().get_variable_value("${pm_id}")
        url = "{0}trade-asset/preventive-maintenance/{1}".format(END_POINT_URL, pm_id)
        common = APIMethod.APIMethod()
        payload = self.gen_preventive_maintenance_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code), response.json()

    def gen_preventive_maintenance_payload(self):
        pm_details = BuiltIn().get_variable_value("${pm_details}")
        payload = {}
        payload.update((k, v) for k, v in pm_details.items())
        return payload
