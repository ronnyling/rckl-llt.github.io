from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import secrets

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class ClaimTypeDelete(object):

    @keyword('user deletes claim type with ${data}')
    def user_deletes_claim_type_with(self, data):
        if data == "created data":
            claim_type_id = BuiltIn().get_variable_value("${claim_type_id}")
        else:
            claim_type_id = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45))
        url = "{0}claim-type/{1}".format(END_POINT_URL, claim_type_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
