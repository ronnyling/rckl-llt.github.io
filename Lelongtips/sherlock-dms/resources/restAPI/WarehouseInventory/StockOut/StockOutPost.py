import secrets
import time
from datetime import datetime

from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

from resources.restAPI.MasterDataMgmt.ProductSector.ProductSectorGet import ProductSectorGet
from resources.restAPI.MasterDataMgmt.Supplier.SupplierGet import SupplierGet
from resources.restAPI.WarehouseInventory.StockOut.StockOutGet import StockOutGet
from resources.restAPI.WarehouseInventory.WarehouseTransfer.WarehouseTransferPost import WarehouseTransferPost

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL

class StockOutPost(object):
    @keyword("user post to ${operation} stock out ${with_without} stock movement for ${whs_type}")
    def user_post_to_stock_out(self, operation, with_without, whs_type):
        url = "{0}inventory-stock-out".format(INVT_END_POINT_URL)
        if with_without == "with":
            stock_movement = True
        elif with_without == "without":
            stock_movement = False
        payload = self.gen_stk_out(operation, stock_movement, whs_type)
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${stk_out_payload}", payload)
            BuiltIn().set_test_variable("${stk_out_id}", response.json()['stockOutId'])
        print(response.status_code)
        return response.status_code

    def gen_stk_out(self, operation, stock_movement, whs_type):
        StockOutGet().user_retrieves_rand_stock_out_type()
        rand_stkout_type_id = BuiltIn().get_variable_value("${rand_stkout_type_id}")
        StockOutGet().user_retrieves_rand_reason_for_stock_out_type()
        rand_stkout_rsn_id = BuiltIn().get_variable_value("${rand_stkout_rsn_id}")
        SupplierGet().user_retrieves_rand_supplier_for_dist()
        rand_supp_id = BuiltIn().get_variable_value("${rand_supp_id}")
        StockOutGet().user_retrieves_rand_stock_out_return_type()
        rand_stkout_return_type_id = BuiltIn().get_variable_value("${rand_stkout_return_type_id}")
        now = datetime.today().strftime("%Y-%m-%d")

        retrieve_success = None
        tries = 0
        while tries < 20 and retrieve_success is None:
            ProductSectorGet().user_retrieve_hq_product_for_dist()
            retrieve_success = BuiltIn().get_variable_value("${retrieve_success}")
            time.sleep(1)

        hq_prd_for_dist_ls = BuiltIn().get_variable_value("${hq_prd_for_dist_ls}")
        batch_bin_details, batch_details, bin_details = WarehouseTransferPost().prepare_wh(hq_prd_for_dist_ls, whs_type, None)
        prd_id = batch_bin_details['PRD_ID']
        cost_price = batch_bin_details['COST']['minCOST']
        qty = secrets.choice(range(1, 3))
        uom_index = [i for i, d in enumerate(batch_bin_details['UOMS']) if 1 in d.values()][0]
        uom_details = batch_bin_details['UOMS'][uom_index]
        conv_factor = uom_details['CONV_FACTOR_SML']
        payload = {
            "STOCK_OUT_DATE": now,
            "WAREHOUSE": batch_bin_details['WHS_ID'],
            "TYPE": rand_stkout_type_id,
            "REASON": rand_stkout_rsn_id,
            "SUPPLIER": rand_supp_id,
            "RETURN_TYPE": rand_stkout_return_type_id,
            "CLAIMABLE": secrets.choice([True, False]),
            "PRIME_FLAG": "PRIME",
            "STOCK_MOVEMENT_TYPE": stock_movement,
            "DEL_DATE_TO_SUPPLIER": now,
            "PRODUCT_DETAILS": [
                {
                    "PRODUCT_ID": prd_id,
                    "NET_AMT": str(cost_price * qty * conv_factor),
                    "COST_PRICE": cost_price,
                    "EXPIRY_DATE": batch_bin_details["EXPIRY_DATE"] if batch_bin_details["EXPIRY_DATE"] is not None else "",
                    "UOMS": [
                        {
                            "UOM_ID": uom_details["UOM_ID"],
                            "QUANTITY": str(qty)
                        }
                    ]
                }
            ]
        }
        if operation == "save":
            payload["STATUS"] = "O"
        elif operation == "confirm":
            payload["STATUS"] = "C"

        if batch_details is not None:
            payload['PRODUCT_DETAILS'][0]['BATCH_ID'] = batch_details['BATCH_ID']
        if bin_details is not None:
            payload['PRODUCT_DETAILS'][0]['BIN_ID'] = bin_details['BIN_ID']
        if batch_bin_details is not None:
            payload['PRODUCT_DETAILS'][0]["EXPIRY_DATE"] = batch_bin_details["EXPIRY_DATE"]
        return payload
