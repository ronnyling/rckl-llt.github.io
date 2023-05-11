from resources.restAPI.CustTrx.DebitNoteNonProduct import DebitNoteNonProductPost
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from setup.hanaDB import HanaDB


END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class DebitNoteNonProductPut(object):

    @keyword('user updates debit note non prod using ${data_type} data')
    def user_updates_debit_note_non_prod(self, data_type):
        res_bd_debit_note_np_id = BuiltIn().get_variable_value("${res_bd_debit_note_np_id}")
        url = "{0}debitnote-nonprd/{1}".format(END_POINT_URL, res_bd_debit_note_np_id)
        payload = DebitNoteNonProductPost.DebitNoteNonProductPost().payload_debit_note_np("updates")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print("Status Code : " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.text)
        if response.status_code != 200:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            res_bd_debit_note_np_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_debit_note_np_id}", res_bd_debit_note_np_id)
            # res_bd_debit_note_np_id = str(res_bd_debit_note_np_id).replace(":", "").replace("-", "")
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM TXN_DBNPRD WHERE TXN_ID = '{0}'"
            #                                                           .format(res_bd_debit_note_np_id), 1)
            # HanaDB.HanaDB().disconnect_from_database()
            print(body_result)
