from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.CustTrx.SalesInvoice import SalesInvoiceGet
import secrets
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class DebitNoteNonProductGet(object):

    def user_retrieves_all_debit_note_non_product(self):
        url = "{0}debitnote-nonprd".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of Debit Note Non Product records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_dnnp = secrets.choice(range(0, len(body_result)))
            else:
                rand_dnnp = 0
            BuiltIn().set_test_variable("${rand_dn_selection}", body_result[rand_dnnp]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves debit note non product by ${type} id')
    def user_retrieves_debit_note_non_product_by_id(self, type):
        if type=="valid":
            res_bd_dn_np_id = BuiltIn().get_variable_value("${res_bd_debit_note_np_id}")
        else :
            res_bd_dn_np_id = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45))
        url = "{0}debitnote-nonprd/{1}".format(END_POINT_URL, res_bd_dn_np_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            prime_status = body_result['PRIME_FLAG']
            assert prime_status == 'PRIME' or prime_status == 'NON_PRIME', "Prime flag doesnt match"
            assert res_bd_id == res_bd_dn_np_id, "ID retrieved not matched"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
