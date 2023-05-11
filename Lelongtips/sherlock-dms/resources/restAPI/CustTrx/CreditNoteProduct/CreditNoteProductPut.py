import json
from resources.restAPI.Common import APIMethod, TokenAccess
from resources.restAPI import PROTOCOL, APP_URL
import urllib3
from resources.restAPI.CustTrx.CreditNoteProduct import CreditNoteProductPost
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
urllib3.disable_warnings()

END_POINT_URL = PROTOCOL+"credit-note"+APP_URL


class CreditNoteProductPut(object):

    @keyword("user edits credit note with ${data_type} data")
    def user_edits_credit_note_with_data(self, data_type):
        url = "{0}credit-note-prd".format(END_POINT_URL)
        payload = CreditNoteProductPost.CreditNoteProductPost().payload_credit_note(data_type)
        header_details = BuiltIn().get_variable_value("${cn_update_header_details}")
        cn_id = BuiltIn().get_variable_value("${res_bd_credit_note_id}")
        if header_details is not None:
            header_details.update({"ID": cn_id})
        else:
            header_details = {"ID": cn_id}
        body_details = BuiltIn().get_variable_value("${cn_update_body_details}")
        payload['TXN_HEADER'].update((k, v) for k, v in header_details.items())
        if body_details:
            payload['TXN_PRODUCT'][0].update((k, v) for k, v in body_details.items())
        payload = json.dumps(payload)
        print("CN Updated Payload: ", payload)
        user = BuiltIn().get_variable_value("${user_role}")
        TokenAccess.TokenAccess().get_token_by_role(user)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print("Update Status code for credit_note_product is " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.text)
        if response.status_code != 200:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            print(body_result)

