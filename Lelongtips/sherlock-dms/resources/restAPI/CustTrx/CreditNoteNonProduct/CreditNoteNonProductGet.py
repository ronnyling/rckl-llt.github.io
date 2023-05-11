from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import secrets

END_POINT_URL = PROTOCOL + "credit-note" + APP_URL


class CreditNoteNonProductGet(object):
    """ Functions to retrieve credit note """

    def user_retrieves_all_credit_note_non_product(self):
        """ Function to retrieve all credit note """
        url = "{0}cn-header".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of Credit Note Non product records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_cnnp = secrets.choice(range(0, len(body_result)))
            else:
                rand_cnnp = 0
            BuiltIn().set_test_variable("${rand_cn_selection}", body_result[rand_cnnp]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_credit_note_non_product_by_id(self):
        res_bd_cn_np_id = BuiltIn().get_variable_value("${rand_cn_selection}")
        url = "{0}cn-header/{1}".format(END_POINT_URL, res_bd_cn_np_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            prime_status = body_result['PRIME_FLAG']
            assert prime_status == 'PRIME' or prime_status == 'NON_PRIME', "Prime flag not showing correctly in respond"
            assert res_bd_id == res_bd_cn_np_id, "ID retrieved not matched"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
