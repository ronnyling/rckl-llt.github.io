import json
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class AssetConditionPut(object):
    @keyword("user puts to asset condition")
    def user_puts_to_asset_condition(self):
        ac_id = BuiltIn().get_variable_value("${ac_id}")
        url = "{0}trade-asset/asset-condition/{1}".format(END_POINT_URL, ac_id)
        common = APIMethod.APIMethod()
        payload = self.gen_asset_condition_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code), response.json()

    def gen_asset_condition_payload(self):
        ac_details = BuiltIn().get_variable_value("${ac_details}")
        payload = {}
        payload.update((k, v) for k, v in ac_details.items())
        return payload
