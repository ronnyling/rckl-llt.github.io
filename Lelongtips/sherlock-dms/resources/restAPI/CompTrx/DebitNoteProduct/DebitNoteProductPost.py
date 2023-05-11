from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.CompTrx.DebitNoteProduct import DebitNoteProductGet
from resources.restAPI.MasterDataMgmt.Supplier import SupplierGet
from resources.restAPI.Config.ReferenceData.ReasonType import ReasonTypeGet

import json
import secrets
import datetime

END_POINT_URL = PROTOCOL + "debit-note-sup" + APP_URL
PRD_SEC_END_POINT_URL = PROTOCOL + "product-sector" + APP_URL


class DebitNoteProductPost(object):

    @keyword('user ${action} debit note product using ${data} data')
    def user_creates_debit_note_product(self, action, data):
        url = "{0}supplier-dn-prd".format(END_POINT_URL)
        if action == "creates":
            payload = self.payload("add", "SAVE")
        else:
            payload = self.payload("add", "SAVE AND CONFIRM")
        common = APIMethod.APIMethod()
        print('DN Payload: ', payload)
        response = common.trigger_api_request("POST", url, json.dumps(payload))
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${sdnp_id}", body_result['ID'])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def payload(self, mode, post_type):
        dnp_details = BuiltIn().get_variable_value("${dnp_details}")
        current_date = datetime.datetime.now()
        dn_date = str(current_date.strftime("%Y-%m-%d"))
        due_date = str(current_date.strftime("%Y-%m-%d"))
        supplier_id = SupplierGet.SupplierGet().user_retrieves_supplier_by_code(dnp_details['SUPPLIER'])
        ReasonTypeGet.ReasonTypeGet().user_gets_reason_by_using_code(dnp_details['REASON'], "SDNP")
        reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        prd_details = self.get_product_details(dnp_details['PRD_CD'])
        qty = dnp_details['QUANTITY']
        price = dnp_details['PRICE']
        ttl_price = str(int(qty)*int(price))
        if post_type == "SAVE AND CONFIRM":
            status = "C"
        else:
            status = "O"

        payload = {
            "POST_TYPE": post_type,
            "STATUS": status,
            "DEBIT_NOTE_NO": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "DEBIT_NOTE_DT": dn_date,
            "DUE_DT": due_date,
            "REF_DOC_TYPE": "I",
            "SUPPLIER_ID": supplier_id,
            "REASON_ID": reason_id,
            "REMARK": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "PRD_DISC_TTL": "0",
            "GROSS_TTL": ttl_price,
            "TAX_TTL": "0",
            "NET_TTL": ttl_price,
            "ADJ_AMT": "0",
            "NET_TTL_TAX": ttl_price,
            "CUST_DISC_PERC": "0",
            "CUST_DISC_AMT": "0",
            "PRIME_FLAG": "PRIME",
            "PRODUCTS": [
                {
                    "PRD_ID": prd_details['ID'],
                    "PRD_CD": prd_details['PRD_CD'],
                    "PRD_DESC": prd_details['PRD_DESC'],
                    "MODE": mode,
                    "GROSS_AMT": ttl_price,
                    "PRD_LISTPRC": price,
                    "NET_AMT": ttl_price,
                    "NET_AMT_TAX": ttl_price,
                    "PRD_INDEX": 0,
                    "UOM_ID": prd_details['UOMS'][0]['UOM_ID'],
                    "UOM_DESC": prd_details['UOMS'][0]['DESCRIPTION'],
                    "PRD_QTY": int(qty),
                    "DISC_AMT": "0",
                    "TAX_AMT": "0",
                    "prdTaxSummary": [],
                    "UOM_LISTPRC": price
                }
            ]
        }
        if mode == "edit":
            sdnp_details = DebitNoteProductGet.DebitNoteProductGet().user_retrieves_comp_debit_note_product_by_id()
            txn_no = sdnp_details['DEBIT_NOTE_NO']
            payload.update({"DEBIT_NOTE_NO": txn_no})
        return payload

    def get_product_details(self, prd_cd):
        prd_list = self.get_all_product_for_dist()
        for prd in prd_list:
            if prd['PRD_CD'] == prd_cd:
                prd_details = prd
                break
        return prd_details

    def get_all_product_for_dist(self):
        url = "{0}all-product-for-dist".format(PRD_SEC_END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve product"
        body_result = response.json()
        return body_result
