from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class DebitNoteProductGet(object):
    """ Functions to retrieve debit note """

    def user_retrieves_all_debit_note(self):
        """ Function to retrieve all debit note """
        url = "{0}debitnote".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total of Debit Note Products retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_debit_note_by_id(self):
        """ Function to retrieve debit note by id"""
        res_bd_debit_note_id = BuiltIn().get_variable_value("${res_bd_debit_note_id}")
        print(res_bd_debit_note_id)
        url = "{0}debitnote/{1}".format(END_POINT_URL, res_bd_debit_note_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            assert body_result['PRIME_FLAG'] == 'PRIME' or body_result['PRIME_FLAG'] == 'NON_PRIME', \
                                                        "Prime flag not showing correctly in respond"
            assert body_result['ID'] == res_bd_debit_note_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)
