from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Merchandising.ActivitySetup.Audit import AuditPost
import json

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class AuditPut(object):

    @keyword('user updates audit setup with ${data} data')
    def user_updates_audit_setup(self, data):
        payload = AuditPost.AuditPost().payload()
        url = "{0}merchandising/merc-general-info".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("Body Result: ", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
