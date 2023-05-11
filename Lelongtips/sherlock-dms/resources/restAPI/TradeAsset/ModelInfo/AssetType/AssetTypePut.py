import json
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class AssetTypePut(object):
    @keyword("user puts to trade asset type")
    def user_puts_to_asset_type(self):
        tat_id = BuiltIn().get_variable_value("${tat_id}")
        url = "{0}trade-asset/trade-asset-type/{1}".format(END_POINT_URL, tat_id)
        common = APIMethod.APIMethod()
        payload = self.gen_tat_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        print("payload = " + str(payload))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code), response.json()

    def gen_tat_payload(self):
        tat_details = BuiltIn().get_variable_value("${tat_details}")
        payload = {}
        payload.update((k, v) for k, v in tat_details.items())
        return payload
