from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.CompTrx.CreditNoteNonProduct import CreditNoteNonProductPost

import json

END_POINT_URL = PROTOCOL + "credit-note" + APP_URL


class CreditNoteNonProductProcess(object):

    @keyword('user confirms credit note non product')
    def user_confirms_credit_note_non_product(self):
        scnnp_id = BuiltIn().get_variable_value("${scnnp_id}")
        url = "{0}supplier-cn-np/{1}".format(END_POINT_URL, scnnp_id)
        payload = CreditNoteNonProductPost.CreditNoteNonProductPost().payload("SAVE AND CONFIRM")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, json.dumps(payload))
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)