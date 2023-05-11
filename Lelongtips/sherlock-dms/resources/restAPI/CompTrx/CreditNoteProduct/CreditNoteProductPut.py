from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.CompTrx.CreditNoteProduct import CreditNoteProductPost
import json

END_POINT_URL = PROTOCOL + "credit-note" + APP_URL


class CreditNoteProductPut(object):

    @keyword('user updates created credit note product using ${data} data')
    def user_updates_credit_note_product(self, data):
        scnp_id = BuiltIn().get_variable_value("${scnp_id}")
        url = "{0}supplier-cn-prd-header/{1}".format(END_POINT_URL, scnp_id)
        payload = CreditNoteProductPost.CreditNoteProductPost().payload("edit", "SAVE")
        common = APIMethod.APIMethod()
        print('Payload is : ', payload)
        response = common.trigger_api_request("PUT", url, json.dumps(payload))
        if response.status_code == 200:
            body_result = response.json()
            """No payload return, only "Success" message return. No ID to retrieve"""
            print("Returned responses:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
