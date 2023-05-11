import json
import secrets

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class SparePartPost(object):
    @keyword("user posts to spare part")
    def user_posts_to_spare_part(self):
        url = "{0}trade-asset/spare-part".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_spare_part_payload()
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            br = response.json()
            BuiltIn().set_test_variable("${sp_details}", br)
            BuiltIn().set_test_variable("${sp_id}", br['ID'])
        return str(response.status_code), response.json()

    def gen_spare_part_payload(self):
        payload = {
            "SPARE_PART_CD": 'SP' + ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5)),
            "SPARE_PART_DESC": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "COST": secrets.randbelow(100),
            "REMARKS": "AUTOMATION"
        }
        return payload
