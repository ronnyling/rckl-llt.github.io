import json
import secrets
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod, TokenAccess
from robot.libraries.BuiltIn import BuiltIn
from setup.hanaDB import HanaDB
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY

DN_HEADER = "${dn_np_header_details}"
END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class DebitNoteNonProductPost(object):

    @keyword('user creates debit note non prod using ${data_type} data')
    def user_creates_debit_note_non_prod(self, data_type):
        url = "{0}debitnote-nonprd".format(END_POINT_URL)
        payload = self.payload_debit_note_np("creates")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print("Status Code : " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.text)
        if response.status_code != 201:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            res_bd_debit_note_np_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_debit_note_np_id}", res_bd_debit_note_np_id)
            # res_bd_debit_note_np_id = str(res_bd_debit_note_np_id).replace(":", "").replace("-", "")
            # HanaDB.HanaDB().connect_database_to_environment()
            # result_body = HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM TXN_DBN WHERE ID = '{0}'"
            #                                                             .format(res_bd_debit_note_np_id), 1)
            # HanaDB.HanaDB().disconnect_from_database()
            # assert result_body, "Record not found in database"
            print(body_result)

    def payload_debit_note_np(self, action):
        route_id = BuiltIn().get_variable_value("${route_id}")
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        header_details = BuiltIn().get_variable_value("${dn_np_header_details}")
        if header_details is not None :
            prime_flag = header_details['PRIME_FLAG']
        else :
            prime_flag = secrets.choice(["PRIME", "NON_PRIME"])
        rand_value = (secrets.randbelow(9999))
        print ("rand val" , rand_value)
        remark = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
        refno =  ''.join(secrets.choice('0123456789AB') for _ in range(10))
        TokenAccess.TokenAccess().get_token_by_role('distadm')
        today_dt = COMMON_KEY.get_local_time()
        payload = {
            "DIST_ID": dist_id,
            "CUST_ID": cust_id,
            "TXN_DT": today_dt,
            "PRIME_FLAG": prime_flag,
            "ROUTE_ID": route_id,
            "INVTERM_ID": "E6FC108E:68ABCE14-43B6-4E23-B6D3-D346E4A3D7D3",
            "REF_DOC_TYPE": None,
            "REF_DOC_NO": None,
            "REF_DOC_ID": None,
            "BILLTO_ID": "B7BA0A51:2F92C435-C156-41E2-8337-9425FFA3C6A4",
            "REASON_ID": reason_id,
            "GROSS_TTL": rand_value,
            "TAX_TTL": 0,
            "NET_TTL": rand_value,
            "NET_TTL_TAX": rand_value,
            "ADJ_AMT": 0,
            "TAXABLE_AMT": 0,
            "NONTAXABLE_AMT": rand_value,
            "REF_DOC_ORI_NET_TTL": 0,
            "RP_ID": None,
            "DUE_DT": today_dt,
            "CUST_TAX_IND": False,
            "ITEMS": [
                {
                    "ITEM_INDEX": 1,
                    "SAC_ID": None,
                    "REMARK": remark,
                    "REF_NO": refno,
                    "AMT": rand_value,
                    "TAX_AMT": 0,
                    "NET_AMT_TAX": rand_value,
                    "TAXES": [

                    ]
                }
            ],
            "PRD_RELATED": False,
            "STATUS": "D"
        }
        if action == 'updates':
            payload.update({"VERSION": 1})
        payload = json.dumps(payload)
        print("Payload is {0}".format(payload))
        return payload

