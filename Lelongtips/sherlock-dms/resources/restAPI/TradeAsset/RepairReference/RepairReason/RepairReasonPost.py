import json
import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class RepairReasonPost(object):
    @keyword("user posts to repair reason")
    def user_posts_to_repair_reason(self):
        url = "{0}trade-asset/repair-reason".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_repair_reason_payload()
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            br = response.json()
            BuiltIn().set_test_variable("${rr_details}", br)
            BuiltIn().set_test_variable("${rr_id}", br['ID'])
        return str(response.status_code), response.json()

    def gen_repair_reason_payload(self):
        payload = {
            "REP_RSN_CD": 'RR' + ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5)),
            "REP_RSN_DESC": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        }
        return payload
