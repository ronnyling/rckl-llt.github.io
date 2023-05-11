import json
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ServiceRequestPut(object):
    @keyword("user puts to service request")
    def user_puts_to_service_request(self):
        asr_id = BuiltIn().get_variable_value("${asr_id}")
        url = "{0}trade-asset/asset-service-request/{1}".format(END_POINT_URL, asr_id)
        common = APIMethod.APIMethod()
        payload = self.gen_service_request_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code), response.json()

    def gen_service_request_payload(self):
        amm_details = BuiltIn().get_variable_value("${asr_details}")
        payload = {}
        payload.update((k, v) for k, v in amm_details.items())
        return payload
