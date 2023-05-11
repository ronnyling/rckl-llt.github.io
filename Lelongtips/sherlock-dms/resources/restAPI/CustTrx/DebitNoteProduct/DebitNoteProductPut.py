from resources.restAPI.CustTrx.DebitNoteProduct import DebitNoteProductPost
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from setup.hanaDB import HanaDB


END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class DebitNoteProductPut(object):

    @keyword('user updates debit note with ${data_type} data')
    def user_updates_debit_note(self, data_type):
        res_bd_debit_note_id = BuiltIn().get_variable_value("${res_bd_debit_note_id}")
        url = "{0}debitnote/{1}".format(END_POINT_URL, res_bd_debit_note_id)
        payload = DebitNoteProductPost.DebitNoteProductPost().payload_debit_note("updates")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print("PUT Status code for debit_note_product is " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.text)
        if response.status_code != 200:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            res_bd_debit_note_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_debit_note_id}", res_bd_debit_note_id)
            # res_bd_debit_note_id = str(res_bd_debit_note_id).replace(":", "").replace("-", "")
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM TXN_DBNPRD WHERE TXN_ID = '{0}'"
            #                                                           .format(res_bd_debit_note_id), 1)
            # HanaDB.HanaDB().disconnect_from_database()
            print(body_result)
