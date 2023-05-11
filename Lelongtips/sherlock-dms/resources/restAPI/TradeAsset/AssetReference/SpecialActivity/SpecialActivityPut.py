import json
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class SpecialActivityPut(object):
    @keyword("user puts to special activity")
    def user_puts_to_special_activity(self):
        sa_id = BuiltIn().get_variable_value("${sa_id}")
        url = "{0}trade-asset/special-activity/{1}".format(END_POINT_URL, sa_id)
        common = APIMethod.APIMethod()
        payload = self.gen_special_activity_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code), response.json()

    def gen_special_activity_payload(self):
        sa_details = BuiltIn().get_variable_value("${sa_details}")
        payload = {}
        payload.update((k, v) for k, v in sa_details.items())
        return payload
