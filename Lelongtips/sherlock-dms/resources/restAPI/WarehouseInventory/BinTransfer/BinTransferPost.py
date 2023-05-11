import secrets
import time
from collections import Counter
from datetime import datetime

from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

from resources.restAPI.Config.ReferenceData.ReasonType.ReasonGet import ReasonGet
from resources.restAPI.MasterDataMgmt.Bin.BinGet import BinGet
from resources.restAPI.MasterDataMgmt.ProductSector.ProductSectorGet import ProductSectorGet
from resources.restAPI.WarehouseInventory.StockReceipt.StockReceiptGet import StockReceiptGet
from resources.restAPI.WarehouseInventory.StockReceipt.StockReceiptPost import StockReceiptPost

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL

class BinTransferPost(object):

    @keyword("user post to ${operation} bin transfer")
    def user_post_to_own_warehouse_transfer(self, operation):
        url = "{0}inventory-bin-transfer".format(INVT_END_POINT_URL)
        payload = self.gen_bin_trsf_payload()

        if operation == "confirm":
            payload['STATUS'] = 'C'
            payload['POST_TYPE'] = "save and confirm"
        elif operation == "save":
            payload['STATUS'] = 'O'
            payload['POST_TYPE'] = "save"

        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            BuiltIn().set_test_variable("${bin_trsf_id}", response.json()['binTransfer'])
            BuiltIn().set_test_variable("${bin_trsf_payload}", payload)
        print(response.status_code)
        return response.status_code

    def gen_bin_trsf_payload(self):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        BinGet().user_retrieves_all_bin()
        whs_bin_list = BuiltIn().get_variable_value("${whs_bin_list}")
        whs_id_dist = [i['WAREHOUSE_CODE']['ID'] for i in whs_bin_list if i['WAREHOUSE_CODE']['DIST_ID'] == dist_id]
        cnt = Counter(whs_id_dist)
        valid_whs_ids = [k for k, v in cnt.items() if v > 1]
        print("is this empty " + str(dist_id))

        StockReceiptGet().user_retrieves_all_whs_available_for_dist()
        retrieve_success = None
        tries = 0
        while tries < 20 and retrieve_success is None:
            ProductSectorGet().user_retrieve_hq_product_for_dist()
            retrieve_success = BuiltIn().get_variable_value("${retrieve_success}")
            time.sleep(1)
        hq_prd_for_dist_ls = BuiltIn().get_variable_value("${hq_prd_for_dist_ls}")
        prd_ids = [hq_prd_for_dist['PRD_ID'] for hq_prd_for_dist in hq_prd_for_dist_ls]
        StockReceiptPost().user_retrieves_batch_list_bulk(valid_whs_ids, prd_ids)
        batch_list_bulk = BuiltIn().get_variable_value("${batch_list_bulk}")
        assert len(batch_list_bulk) > 0, "No available whs found with multiple bins"
        bin_details = None
        batch_details = None
        batch_bin_details = None
        found_available_qty = False
        for batch_bin in batch_list_bulk:
            batches = batch_bin['BATCH']
            for batch in batches:
                bins = batch['BIN_ARR']
                if len(bins) > 1:
                    for bin in bins:
                        if int(float(bin['AVAILABLE_QTY'])) > 5:
                            bin_details = bin
                            batch_details = batch
                            batch_bin_details = batch_bin
                            found_available_qty = True
                            break
                if found_available_qty:
                    break
            if found_available_qty:
                break

        other_bins_id = [i['BIN_ID'] for i in batch_details['BIN_ARR'] if i['BIN_ID'] != bin_details['BIN_ID']]
        rand_dest_bin = secrets.choice(other_bins_id)
        rand_dest_bin_id = rand_dest_bin
        uom_index = [i for i, d in enumerate(batch_bin_details['UOMS']) if 1 in d.values()][0]
        uom_details = batch_bin_details['UOMS'][uom_index]
        whs_id = batch_bin_details['WHS_ID']

        BuiltIn().set_test_variable("${res_bd_reason_type_id}", "D4269B2F:55657639-E9B3-47E9-B975-32FEDFD9D89A")
        ReasonGet().user_retrieves_all_reasons()
        rand_reason = BuiltIn().get_variable_value("${rand_reason}")

        payload = {
            "LOOSE_PALLET_TRANSFER": "false",
            "BIN_TRANSFER_DATE": str(datetime.today().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"),
            "WAREHOUSE": whs_id,
            "REASON": rand_reason,
            "PRODUCT_DETAILS": [
                {
                    "PRODUCT_ID": batch_bin_details['PRD_ID'],
                    "BATCH_ID": batch_details['BATCH_ID'],
                    "EXPIRY_DATE": batch_details['EXP_DATE'],
                    "SOURCE_BIN": bin_details['BIN_ID'],
                    "DEST_BIN": rand_dest_bin_id,
                    "PRD_BATCH_UOM": [
                        {
                            "UOM_ID": uom_details['UOM_ID'],
                            "TRANSFER_QTY": "1",
                            "TRANSFER_QTY_SML": "1"
                        }
                    ]
                }
            ]
        }
        return payload
