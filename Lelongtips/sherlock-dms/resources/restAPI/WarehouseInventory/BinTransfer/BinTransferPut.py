
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL

class BinTransferPut(object):

    @keyword("user puts to ${operation} bin transfer")
    def user_puts_bin_transfer(self, operation):
        bin_trsf_id = BuiltIn().get_variable_value("${bin_trsf_id}")
        bin_trsf_payload = BuiltIn().get_variable_value("${bin_trsf_payload}")

        url = "{0}inventory-bin-transfer/{1}".format(INVT_END_POINT_URL, bin_trsf_id)
        bin_trsf_payload = json.loads(bin_trsf_payload)
        if operation == "confirm":
            bin_trsf_payload['STATUS'] = 'C'
            bin_trsf_payload['POST_TYPE'] = 'save and confirm'
        elif operation == "save":
            bin_trsf_payload['STATUS'] = 'O'
            bin_trsf_payload['POST_TYPE'] = 'save'
        bin_trsf_payload['PRODUCT_DETAILS'][0]['EXISTING'] = "true"

        payload = json.dumps(bin_trsf_payload)
        print("payload = " + str(payload))
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code
