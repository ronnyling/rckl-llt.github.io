import secrets
import time
from datetime import datetime

from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

from resources.restAPI.Config.ReferenceData.ReasonType.ReasonGet import ReasonGet
from resources.restAPI.MasterDataMgmt.ProductSector.ProductSectorGet import ProductSectorGet
from resources.restAPI.WarehouseInventory.StockAdjustment.StockAdjustmentGet import StockAdjustmentGet
from resources.restAPI.WarehouseInventory.StockReceipt.StockReceiptGet import StockReceiptGet
from resources.restAPI.WarehouseInventory.StockReceipt.StockReceiptPost import StockReceiptPost

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL


class StockAdjustmentPost(object):

    @keyword("user post to save stock adjustment")
    def user_post_to_stock_adjustment(self):

        url = "{0}inventory-stock-adjustment".format(INVT_END_POINT_URL)
        payload = self.gen_stock_adjustment_payload()
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${stock_adjustment_id}", response.json()['adjustmentId'])
            BuiltIn().set_test_variable("${stock_adjustment_payload}", payload)
        print(response.status_code)
        return response.status_code

    def gen_stock_adjustment_payload(self):
        whs_ids = None
        batch_bin_details = None

        StockReceiptGet().user_retrieves_all_whs_available_for_dist()
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
            StockReceiptPost().user_retrieves_batch_list_bulk(whs_ids, prd_ids)
            batch_list_bulk = BuiltIn().get_variable_value("${batch_list_bulk}")
            for batch_bin in batch_list_bulk:
                if len(batch_bin['BATCH']) > 0 and batch_bin['WHS_ID'] in valid_whs_ids:
                    batch_bin_details = batch_bin
                    break
            if batch_bin_details is not None:
                break
        print("batch details = " + str(batch_bin_details))

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

        StockAdjustmentGet().user_retrieves_all_stock_adjustment_types()
        stock_adjustment_type_ls = BuiltIn().get_variable_value("${stock_adjustment_type_ls}")
        rand_type = secrets.choice(stock_adjustment_type_ls)
        adj_type = rand_type['ID']

        BuiltIn().set_test_variable("${res_bd_reason_type_id}","D4269B2F:E4260E8F-AF60-414E-89BB-C10036E7136B")
        ReasonGet().user_retrieves_all_reasons()
        rand_reason = BuiltIn().get_variable_value("${rand_reason}")

        payload = {
            "STOCK_ADJUSTMENT_DATE": datetime.today().strftime("%Y-%m-%d"),
            "WAREHOUSE_ID": whs_id,
            "PRIME_FLAG": "PRIME",
            "REMARKS": "",
            "STATUS": "O",
            "PRODUCT_DETAILS": [
                {
                    "PRODUCT_ID": prd_id,
                    "STKADJ_TYPE": adj_type,
                    "REASON": rand_reason,
                    "BATCH_ID": batch_details['BATCH_ID'],
                    "BIN_ID": rand_bin_details_for_batch['BIN_ID'],
                    "EXPIRY_DATE": batch_details['EXP_DATE'],
                    "NET_AMT": str(cost_details['minCOST'] * qty),
                    "UOMS": [
                        {
                            "UOM_ID": rand_uom_details['UOM_ID'],
                            "QUANTITY": str(qty)
                        }
                    ]
                }
            ]
        }
        return payload
