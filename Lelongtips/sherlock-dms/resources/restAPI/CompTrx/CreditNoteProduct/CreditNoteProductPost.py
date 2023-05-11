from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

from resources.restAPI.CompTrx.CreditNoteProduct import CreditNoteProductGet
from resources.restAPI.MasterDataMgmt.Supplier import SupplierGet
from resources.restAPI.Config.ReferenceData.ReasonType import ReasonTypeGet
from resources.restAPI.MasterDataMgmt.Warehouse import WarehouseGet
import json
import secrets
import datetime

END_POINT_URL = PROTOCOL + "credit-note" + APP_URL
PRD_SEC_END_POINT_URL = PROTOCOL + "product-sector" + APP_URL


class CreditNoteProductPost(object):

    @keyword('user ${action} credit note product using ${data} data')
    def user_creates_credit_note_product(self, action, data):
        url = "{0}supplier-cn-prd".format(END_POINT_URL)
        if action == "creates":
            payload = self.payload("add", "SAVE")
        else:
            payload = self.payload("add", "SAVE AND CONFIRM")
        common = APIMethod.APIMethod()
        print('CN Payload: ', payload)
        response = common.trigger_api_request("POST", url, json.dumps(payload))
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${scnp_id}", body_result['CNSupProdId'])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def payload(self, mode, post_type):
        cnp_details = BuiltIn().get_variable_value("${cnp_details}")
        current_date = datetime.datetime.now()
        cn_date = str(current_date.strftime("%Y-%m-%d"))
        supplier_id = SupplierGet.SupplierGet().user_retrieves_supplier_by_code(cnp_details['SUPPLIER'])
        ReasonTypeGet.ReasonTypeGet().user_gets_reason_by_using_code(cnp_details['REASON'], "SCNP")
        reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        prd_details = self.get_product_details(cnp_details['PRD_CD'])
        warehouse = cnp_details['WHS']
        wh_id = WarehouseGet.WarehouseGet().user_retrieves_warehouse_by_using_code(warehouse)
        qty = cnp_details['QUANTITY']
        price = cnp_details['PRICE']
        ttl_price = str(int(qty)*int(price))
        if post_type == "SAVE AND CONFIRM":
            status = "C"
        else:
            status = "O"

        payload = {
            "POST_TYPE": post_type,
            "STATUS": status,
            "CREDIT_NOTE_NO": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "CREDIT_NOTE_DT": cn_date,
            "SUPPLIER_ID": supplier_id,
            "REASON_ID": reason_id,
            "REMARK": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "PRD_DISC_TTL": "0",
            "GROSS_TTL": ttl_price,
            "TAX_TTL": "0",
            "NET_TTL": ttl_price,
            "ADJ_AMT": "0",
            "NET_TTL_TAX": ttl_price,
            "TAXABLE_AMT": "0",
            "NONTAXABLE_AMT": "0",
            "CUST_DISC_PERC": "0",
            "CUST_DISC_AMT": "0",
            "INV_DISC_TTL": "0",
            "PRIME_FLAG": "PRIME",
            "STOCK_MOVEMENT": False,
            "WHS_ID": wh_id,
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
            scnp_details = CreditNoteProductGet.CreditNoteProductGet().user_retrieves_comp_credit_note_product_by_id()
            txn_no = scnp_details['CREDIT_NOTE_NO']
            payload.update({"CREDIT_NOTE_NO": txn_no})
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
