import secrets
import time
from datetime import datetime

from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

from resources.restAPI.MasterDataMgmt.ProductSector.ProductSectorGet import ProductSectorGet
from resources.restAPI.WarehouseInventory.StockReceipt.StockReceiptGet import StockReceiptGet

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL


class StockReceiptPost(object):

    @keyword("user post to ${mode} stock receipt")
    def user_post_to_stock_receipt(self, mode):
        post_type = None
        if mode == "save":
            post_type = "save"
        elif mode == "confirm":
            post_type = "save and confirm"

        url = "{0}inventory-stock-receipt".format(INVT_END_POINT_URL)
        payload = self.gen_stock_receipt_payload(post_type)
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            BuiltIn().set_test_variable("${stock_receipt_id}", response.json()['STOCK_RECEIPT_ID'])
            BuiltIn().set_test_variable("${stock_receipt_payload}", payload)
        print(response.status_code)
        return response.status_code

    def gen_stock_receipt_payload(self, post_type):
        whs_ids = None
        batch_bin_details = None

        StockReceiptGet().user_retrieves_all_whs_available_for_dist()
        StockReceiptGet().user_retrieves_all_supplier_available_for_dist()
        retrieve_success = None
        tries = 0
        while tries < 20 and retrieve_success is None:
            ProductSectorGet().user_retrieve_hq_product_for_dist()
            retrieve_success = BuiltIn().get_variable_value("${retrieve_success}")
            time.sleep(1)
        hq_prd_for_dist_ls = BuiltIn().get_variable_value("${hq_prd_for_dist_ls}")

        valid_whs_filter = "?filter=%20%7B%22DIST_ID%22%3A%7B%22%24eq%22%3A%223CAF4BF6%3AF0A6331B-3CFD-4DB4-9792-A27221CC2250%22%7D%7D"
        BuiltIn().set_test_variable("${whs_filter}", valid_whs_filter)
        StockReceiptGet().user_retrieves_all_whs_available_for_dist()
        valid_whs_ls = BuiltIn().get_variable_value("${whs_for_dist_ls}")

        valid_whs_ids = [whs['ID'] for whs in valid_whs_ls]
        for hq_prd_for_dist in hq_prd_for_dist_ls:
            prd_ids = [hq_prd_for_dist['PRD_ID']]
            self.user_retrieves_batch_list_bulk(whs_ids, prd_ids)
            batch_list_bulk = BuiltIn().get_variable_value("${batch_list_bulk}")
            for batch_bin in batch_list_bulk:
                if len(batch_bin['BATCH']) > 0 and batch_bin['WHS_ID'] in valid_whs_ids:
                    batch_bin_details = batch_bin
                    break
            if batch_bin_details is not None:
                break

        supplier_for_dist_ls = BuiltIn().get_variable_value("${supplier_for_dist_ls}")
        rand = secrets.choice(supplier_for_dist_ls)
        rand_supp_id = rand['ID']

        prd_id = batch_bin_details['PRD_ID']
        whs_id = batch_bin_details['WHS_ID']
        uom_details = batch_bin_details['UOMS']
        cost_details = batch_bin_details['COST']
        rand_batch = secrets.choice(batch_bin_details['BATCH'])

        batch_details = rand_batch
        rand_bin = secrets.choice(batch_details['BIN_ARR'])
        rand_bin_details_for_batch = rand_bin

        rand_uom = secrets.choice(uom_details)
        rand_uom_details = rand_uom
        qty = secrets.choice(range(1, 3))
        payload = {
            "STOCK_RECEIPT_DATE": datetime.today().strftime("%Y-%m-%d"),
            "PRIME_FLAG": "PRIME",
            "WAREHOUSE": whs_id,
            "REMARKS": "",
            "SUPPLIER_NAME_ADDRESS": rand_supp_id,
            "INVOICE_NO": "",
            "INVOICE_DATE": "",
            "DELIVERY_ORDER_NO": "DON".join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(3)),
            "DELIVERY_ORDER_DATE": "",
            "POST_TYPE": post_type,
            "STATUS": "O",
            "PRODUCT_DETAILS": [
                {
                    "PRODUCT_ID": prd_id,
                    "BATCH_CODE": batch_details['BATCH_CD'],
                    "EXISTING": False,
                    "EXS_BATCH": True,
                    "EXPIRY_DATE": batch_details['EXP_DATE'],
                    "MRP": str(cost_details['minMRP']),
                    "COST_PRICE": str(cost_details['minCOST']),
                    "NET_AMT": str(cost_details['minCOST'] * qty),
                    "PRD_BATCH_UOM": [
                        {
                            "UOM_ID": rand_uom_details['UOM_ID'],
                            "RECEIVD_QTY": str(qty),
                            "RECEIVD_QTY_SML": str(qty)
                        }
                    ],
                    "BIN_ALLOCATION": [
                        {
                            "BIN_ID": rand_bin_details_for_batch['BIN_ID'],
                            "UOM": [
                                {
                                    "UOM_ID": rand_uom_details['UOM_ID'],
                                    "BIN_QTY": qty,
                                    "BIN_QTY_SML": qty
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        return payload

    def user_retrieves_batch_list_bulk(self, whs_ids, prd_ids):
        url = "{0}batch-list-bulk".format(INVT_END_POINT_URL)
        payload = self.gen_batch_list_bulk_payload(whs_ids, prd_ids)
        payload = json.dumps(payload)
        print("payload is " + payload)
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${batch_list_bulk}", response.json())
        print(response.status_code)
        return response.status_code

    def gen_batch_list_bulk_payload(self, whs_ids, prd_ids):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        payload = {
            "DistId": dist_id if dist_id is not None else "3CAF4BF6:F0A6331B-3CFD-4DB4-9792-A27221CC2250",
            "ProductIds": prd_ids
        }
        if whs_ids is not None:
            payload["WarehouseIds"] = whs_ids
        return payload


