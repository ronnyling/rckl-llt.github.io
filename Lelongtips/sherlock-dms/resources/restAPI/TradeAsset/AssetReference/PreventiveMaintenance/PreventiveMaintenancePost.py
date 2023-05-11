import json
import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class PreventiveMaintenancePost(object):
    @keyword("user posts to preventive maintenance")
    def user_posts_to_preventive_maintenance(self):
        url = "{0}trade-asset/preventive-maintenance".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_preventive_maintenance_payload()
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            br = response.json()
            BuiltIn().set_test_variable("${pm_details}", br)
            BuiltIn().set_test_variable("${pm_id}", br['ID'])
        return str(response.status_code), response.json()

    def gen_preventive_maintenance_payload(self):
        payload = {
            "PREVENTIVE_MAINTENANCE_CD": 'PM' + ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5)),
            "PREVENTIVE_MAINTENANCE_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        }
        return payload
