from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

METADATA_END_POINT_URL = PROTOCOL + "metadata" + APP_URL
module = "transaction-list"


class TransactionListGet(object):

    @keyword('user retrieves the transaction id for ${trx_control} and code for ${op_type}')
    def user_retrieves_transaction_id(self, trx_control, op_type):
        url = "{0}module-data/{1}".format(METADATA_END_POINT_URL, module)
        BuiltIn().set_test_variable("${trx_control}", trx_control)
        BuiltIn().set_test_variable("${op_type}", op_type)
        print("URL: ", url)
        print("op_type: ", op_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        code_op_type = self.user_retrieves_code_op_type(op_type)
        print("type: ", code_op_type)
        BuiltIn().set_test_variable("${type}", code_op_type)
        if response.status_code == 200:
            body_result = response.json()
            print("Result: ", body_result)
            for x in body_result:
                trx_desc = x['TXN_DESC']
                if trx_desc == trx_control:
                    trx_id = x['ID']
                    trx_cd = x['TXN_CD']
                    break
            BuiltIn().set_test_variable("${transaction_id}", trx_id)
            BuiltIn().set_test_variable("${transaction_code}", trx_cd)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_transaction_list(self):
        url = "{0}module-data/{1}".format(METADATA_END_POINT_URL, module)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        body_result = response.json()
        retrieved_data = []
        for x in body_result:
            soc_details = BuiltIn().get_variable_value("${SOCDetails}")
            deleted_list = BuiltIn().get_variable_value("${DeletedList}")
            if soc_details and x['TXN_CD'] in soc_details.keys():
                print("TXN code for SOC checking: ", x['TXN_CD'])
                txn_cd = x['TXN_CD']
                if x['SOC_IND'] is None:
                    x['SOC_IND'] = False
                assert x['SOC_IND'] == soc_details[txn_cd], "SOC_IND storing incorrectly"
            if deleted_list:
                print("TXN code which is deleted: ", x['TXN_CD'])
                assert x['TXN_CD'] not in deleted_list, "{0} - Transaction is not being deleted".format(x['TXN_CD'])
            retrieved_data.append(x['TXN_CD'])
        active_list = BuiltIn().get_variable_value("${ActiveList}")
        if active_list:
            for data in active_list:
                assert data in retrieved_data, "Active list missing in transaction control"
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_code_op_type(self, op_type):
        if op_type == "Van Sales":
            return "V"
        elif op_type == "Pre-Sales":
            return "O"
        elif op_type == "Delivery Rep":
            return "L"
        elif op_type == "Merchandiser":
            return "M"
