import json
import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class SpecialActivityPost(object):
    @keyword("user posts to special activity")
    def user_posts_to_special_activity(self):
        url = "{0}trade-asset/special-activity".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_special_activity_payload()
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            br = response.json()
            BuiltIn().set_test_variable("${sa_details}", br)
            BuiltIn().set_test_variable("${sa_id}", br['ID'])
        return str(response.status_code), response.json()

    def gen_special_activity_payload(self):
        payload = {
            "SPECIAL_ACT_CD": 'SA' + ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5)),
            "SPECIAL_ACT_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        }
        return payload
