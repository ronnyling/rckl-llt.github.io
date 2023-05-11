from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class ClaimTypePut(object):

    @keyword("user updates claim type with ${payload}")
    def update_claim_type(self, payload=None, status=None, claim_type_cd=None, claim_type_type=None):
        claim_type_id = BuiltIn().get_variable_value("${claim_type_id}")
        url = "{0}claim-type/{1}".format(END_POINT_URL, claim_type_id)

        newdict = BuiltIn().get_variable_value("&{payload}")    # * note PUT requires VERSION to be integer, but POST doesnt
        print(newdict)
        update_id = {'ID': claim_type_id}

        newdict = json.loads(payload)
        newdict.update(update_id)

        print("Payload for update ", newdict)
        payload = json.dumps(newdict)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code
