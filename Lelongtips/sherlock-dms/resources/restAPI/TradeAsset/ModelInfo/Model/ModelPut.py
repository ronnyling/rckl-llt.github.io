import json
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ModelPut(object):
    @keyword("user puts to model")
    def user_puts_to_model(self):
        model_id = BuiltIn().get_variable_value("${model_id}")
        url = "{0}trade-asset/asset-model/{1}".format(END_POINT_URL, model_id)
        common = APIMethod.APIMethod()
        payload = self.gen_model_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code), response.json()

    def gen_model_payload(self):
        model_details = BuiltIn().get_variable_value("${model_details}")
        payload = {}
        payload.update((k, v) for k, v in model_details.items())
        return payload
