import json
import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class AssetConditionPost(object):
    @keyword("user posts to asset condition")
    def user_posts_to_asset_condition(self):
        url = "{0}trade-asset/asset-condition".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_asset_condition_payload()
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            br = response.json()
            BuiltIn().set_test_variable("${ac_details}", br)
            BuiltIn().set_test_variable("${ac_id}", br['ID'])
        return str(response.status_code), response.json()

    def gen_asset_condition_payload(self):
        payload = {
            "ASSET_COND_CD": 'AC' + ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5)),
            "ASSET_COND_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        }
        return payload
