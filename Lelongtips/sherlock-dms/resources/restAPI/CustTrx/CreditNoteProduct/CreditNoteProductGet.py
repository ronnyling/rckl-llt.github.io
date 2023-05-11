import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "credit-note" + APP_URL


class CreditNoteProductGet(object):
    """ Functions to retrieve credit note """

    def user_retrieves_all_credit_note(self):
        """ Function to retrieve all credit note """
        url = "{0}cn-prd-header".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of Credit Note Products records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_cnp = secrets.choice(range(0, len(body_result)))
            else:
                rand_cnp = 0
            BuiltIn().set_test_variable("${rand_cn_selection}", body_result[rand_cnp]["ID"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_credit_note_by_id(self):
        """ Function to retrieve credit note by id"""
        res_bd_credit_note_id = BuiltIn().get_variable_value("${res_bd_credit_note_id}")
        print(res_bd_credit_note_id)
        url = "{0}cn-prd-header/{1}".format(END_POINT_URL, res_bd_credit_note_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            prime_status = body_result['PRIME_FLAG']
            assert prime_status == 'PRIME' or prime_status == 'NON_PRIME', "Prime flag not showing correctly in respond"
            assert res_bd_id == res_bd_credit_note_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_credit_note_product_by_id(self):
        """ Function to retrieve credit note product details by using id"""
        res_bd_credit_note_id = BuiltIn().get_variable_value("${res_bd_credit_note_id}")
        url = "{0}cn-prd-header/{1}/cn-prd-detail/".format(END_POINT_URL, res_bd_credit_note_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result[0]['TXN_ID']
            assert res_bd_id == res_bd_credit_note_id, "ID retrieved not matched"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
