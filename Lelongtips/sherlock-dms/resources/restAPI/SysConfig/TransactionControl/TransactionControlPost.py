from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import secrets
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.Common import Common

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL
METADATA_END_POINT_URL = PROTOCOL + "metadata" + APP_URL
scheduleModule = "schedule-transactioncontrol"
configureModule = "configure-transaction-control"


class TransactionControlPost(object):
    TRX_ID = "${transaction_id}"
    
    @keyword('user assigns the transaction control for all routes')
    def user_assigns_transaction_control(self):
        trans_id = BuiltIn().get_variable_value(self.TRX_ID)
        tran_cd = BuiltIn().get_variable_value("${transaction_code}")
        status_code = BuiltIn().set_test_variable(Common.STATUS_CODE)
        if status_code == '200':
            url = "{0}setting-routetransactioncontrol/{1}".format(END_POINT_URL, scheduleModule)
            print("url1: ", url)
            payload = self.payload_configure_transaction_control(trans_id, tran_cd, "")
            common = APIMethod.APIMethod()
            response = common.trigger_api_request("POST", url, payload)
            print(str(response.status_code))
            print("Schedule Response: ", response.text)
            BuiltIn().set_test_variable(Common.STATUS_CODE, str(response.status_code))
            BuiltIn().set_test_variable("${status_text}", response.text)
            BuiltIn().set_test_variable("${payload}", payload)

    @keyword('user creates the transaction control with ${status} data')
    def user_creates_transaction_control(self, status):
        assigned_text = BuiltIn().get_variable_value("${status_text}")
        assigned_response = BuiltIn().get_variable_value(Common.STATUS_CODE)
        trans_id = BuiltIn().get_variable_value(self.TRX_ID)
        tran_cd = BuiltIn().get_variable_value("${transaction_code}")
        payload = self.payload_configure_transaction_control(trans_id, tran_cd, status)
        print("payload: ", payload)
        if assigned_response == 200 or assigned_text == 'Transaction control deleted successfully':
            url = "{0}module-data/{1}".format(METADATA_END_POINT_URL, configureModule)
            print("url2: ", url)
            common = APIMethod.APIMethod()
            response = common.trigger_api_request("POST", url, payload)
            print(response.status_code)
            if response.status_code == 201:
                body_result = response.json()
                print("Transaction Result: ", body_result)
                trx_id = body_result['ID']
                txn_id = body_result['TXN_ID']['ID']
                opt_type = body_result['OPT_TYPE']
                BuiltIn().set_test_variable(self.TRX_ID, trx_id)
                BuiltIn().set_test_variable("${txn_id}", txn_id)
                BuiltIn().set_test_variable("${opt_type}", opt_type)
            BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    def payload_configure_transaction_control(self, trans_id, tran_cd, status):
        op_type = None
        if status == 'fixed':
            op_type = BuiltIn().get_variable_value("${type}")
            print("op_type: ", op_type)
        payload = {
            "ALLOW_IND": secrets.choice([True, False]),
            "HIT_IND": secrets.choice([True, False]),
            "MANDATORY_IND": secrets.choice([True, False]),
            "EDIT_IND": secrets.choice([True, False]),
            "CANCEL_IND": secrets.choice([True, False]),
            "GPS_IND": secrets.choice([True, False]),
            "PRINT_IND": secrets.choice([True, False]),
            "PRINT_COPY": secrets.choice(range(1, 3)),
            "MAX_PRINT_COPY": secrets.choice(range(6, 10)),
            "IS_PARENT": False,
            "OPT_TYPE": op_type,
            "TXN_ID": {
                "ID": trans_id,
                "TXN_CD": tran_cd
            }
        }
        details = BuiltIn().get_variable_value("${TransactionDetails}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Transaction Control Payload: ", payload)
        return payload
