import json
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class AssetMovementPut(object):
    @keyword("user puts to asset movement")
    def user_puts_to_asset_movement(self):
        amm_id = BuiltIn().get_variable_value("${amm_id}")
        url = "{0}trade-asset/asset-movement/{1}".format(END_POINT_URL, amm_id)
        common = APIMethod.APIMethod()
        payload = self.gen_asset_movement_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code), response.json()

    def gen_asset_movement_payload(self):
        amm_details = BuiltIn().get_variable_value("${amm_details}")
        payload = {}
        payload.update((k, v) for k, v in amm_details.items())
        return payload
