from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import secrets

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class AuditDelete(object):

    @keyword('user deletes created audit setup')
    def user_deletes_created_audit_setup(self):
        audit_id = BuiltIn().get_variable_value("${audit_id}")
        url = "{0}merc-audit/{1}".format(END_POINT_URL, audit_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
