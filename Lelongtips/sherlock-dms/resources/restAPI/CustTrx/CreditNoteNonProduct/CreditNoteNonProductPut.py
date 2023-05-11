import json
from resources.restAPI.CustTrx.CreditNoteNonProduct import CreditNoteNonProductPost
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY

END_POINT_URL = PROTOCOL + "credit-note" + APP_URL


class CreditNoteNonProductPut(object):

    @keyword('user updates credit note non product with ${data_type} data')
    def user_updates_cn_np(self, data_type):
        url = "{0}credit-note-np".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = CreditNoteNonProductPost.CreditNoteNonProductPost().payload_combine(data_type)
        payload['TXN_HEADER']['ID'] = BuiltIn().get_variable_value("${cn_np_id}")
        payload = json.dumps(payload)
        print("UPDATED PAYLOAD: ", payload)
        response = common.trigger_api_request("POST", url, payload)
        print("Updated Status Code for Credit Note Non Product is " + str(response.status_code))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)