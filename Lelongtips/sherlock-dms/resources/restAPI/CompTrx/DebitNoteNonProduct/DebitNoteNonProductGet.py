from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "debit-note-sup" + APP_URL


class DebitNoteNonProductGet(object):

    @keyword('user retrieves debit note non product')
    def user_retrieves_debit_note_non_product(self):
        url = "{0}supplier-dn-np-header".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def get_dn_svc_dtl_id(self, dnnp_id):
        url = "{0}supplier-dn-np-header/{1}/dn-detail".format(END_POINT_URL, dnnp_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        body_result = response.json()
        svc_dtl_id = body_result[0]['ID']
        BuiltIn().set_test_variable("${svc_dtl_id}", svc_dtl_id)
