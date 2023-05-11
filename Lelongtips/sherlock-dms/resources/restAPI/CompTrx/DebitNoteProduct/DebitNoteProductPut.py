from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.CompTrx.DebitNoteProduct import DebitNoteProductPost
import json

END_POINT_URL = PROTOCOL + "debit-note-sup" + APP_URL


class DebitNoteProductPut(object):

    @keyword('user updates created debit note product using ${data} data')
    def user_updates_debit_note_product(self, data):
        sdnp_id = BuiltIn().get_variable_value("${sdnp_id}")
        url = "{0}supplier-dn-prd-header/{1}".format(END_POINT_URL, sdnp_id)
        payload = DebitNoteProductPost.DebitNoteProductPost().payload("edit", "SAVE")
        payload['PRODUCT_DETAILS'] = payload.pop('PRODUCTS')
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, json.dumps(payload))
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${sdnp_id}", body_result['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)
