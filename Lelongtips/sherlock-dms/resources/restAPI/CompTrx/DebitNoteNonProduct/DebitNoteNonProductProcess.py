from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.CompTrx.DebitNoteNonProduct import DebitNoteNonProductPost
from resources.restAPI.CompTrx.DebitNoteNonProduct import DebitNoteNonProductGet

END_POINT_URL = PROTOCOL + "debit-note-sup" + APP_URL


class DebitNoteNonProductProcess(object):

    @keyword('user confirms debit note non product')
    def user_confirms_debit_note_non_product(self):
        sdnnp_id = BuiltIn().get_variable_value("${sdnnp_id}")
        url = "{0}supplier-dn-np-header/{1}".format(END_POINT_URL, sdnnp_id)
        DebitNoteNonProductGet.DebitNoteNonProductGet().get_dn_svc_dtl_id(sdnnp_id)
        dn_payload = DebitNoteNonProductPost.DebitNoteNonProductPost().dn_payload("SAVE AND CONFIRM")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, dn_payload)
        if response.status_code == 200:
            tax_url = "{0}supplier-dn-np-header/{1}/dn-tax".format(END_POINT_URL, sdnnp_id)
            dn_tax_payload = DebitNoteNonProductPost.DebitNoteNonProductPost().dn_tax_payload()
            response = common.trigger_api_request("PUT", tax_url, dn_tax_payload)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
