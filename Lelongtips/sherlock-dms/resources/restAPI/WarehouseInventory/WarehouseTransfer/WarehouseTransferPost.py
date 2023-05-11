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
from resources.restAPI.WarehouseInventory.StockAudit.StockAuditGet import StockAuditGet
from resources.restAPI.WarehouseInventory.StockReceipt.StockReceiptGet import StockReceiptGet
from resources.restAPI.WarehouseInventory.StockReceipt.StockReceiptPost import StockReceiptPost

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL

class WarehouseTransferPost(object):

    @keyword("user post to ${operation} ${tsfr_type} warehouse transfer from ${source_whs_type} to ${dest_whs_type}")
    def user_post_to_own_warehouse_transfer(self, operation, tsfr_type, source_whs_type, dest_whs_type):
        url = "{0}inventory-warehouse-transfer".format(INVT_END_POINT_URL)
        payload = self.gen_whs_trsf_payload(tsfr_type, source_whs_type, dest_whs_type)

        if operation == "confirm":
            payload['STATUS'] = 'C'
        elif operation == "save":
            payload['STATUS'] = 'O'
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${whs_trsf_id}", response.json()['wareHouseTransfer'])
            BuiltIn().set_test_variable("${whs_trsf_payload}", payload)
        print(response.status_code)
        return response.status_code

    def gen_whs_trsf_payload(self, tsfr_type, source_whs_type, dest_whs_type):
        src_batch_bin_details = None
        dist_src_dest = BuiltIn().get_variable_value("${dist_src_dest}")
        source_dist_id = dist_src_dest['src_distributor_id']

        if tsfr_type == "own":
            dest_dist_id = source_dist_id
        else:
            dest_dist_id = dist_src_dest['dest_distributor_id']

        StockReceiptGet().user_retrieves_all_whs_available_for_dist()
        StockReceiptGet().user_retrieves_all_supplier_available_for_dist()
        retrieve_success = None
        tries = 0
        while tries < 20 and retrieve_success is None:
            ProductSectorGet().user_retrieve_hq_product_for_dist()
            retrieve_success = BuiltIn().get_variable_value("${retrieve_success}")
            time.sleep(1)
        hq_prd_for_dist_ls = BuiltIn().get_variable_value("${hq_prd_for_dist_ls}")

        if tsfr_type == "own":
            src_batch_bin_details, src_batch_details, src_bin_details = self.prepare_wh(hq_prd_for_dist_ls, source_whs_type, None)
            dest_batch_bin_details, dest_batch_details, dest_bin_details = self.prepare_wh(hq_prd_for_dist_ls, dest_whs_type, src_batch_bin_details['PRD_ID'])
        elif tsfr_type == "other":
            src_batch_bin_details, src_batch_details, src_bin_details = self.prepare_wh(hq_prd_for_dist_ls, source_whs_type, None)
            dest_batch_bin_details, dest_batch_details, dest_bin_details = self.prepare_wh(hq_prd_for_dist_ls, dest_whs_type, src_batch_bin_details['PRD_ID'])

        prd_id = src_batch_bin_details['PRD_ID']
        src_whs_id = src_batch_bin_details['WHS_ID']
        dest_whs_id = dest_batch_bin_details['WHS_ID']

        BuiltIn().set_test_variable("${res_bd_reason_type_id}", "D4269B2F:D569455D-606D-4F5B-9AC4-443E1E2E6225")
        ReasonGet().user_retrieves_all_reasons()
        rand_reason = BuiltIn().get_variable_value("${rand_reason}")

        src_cost_price = src_batch_bin_details['COST']['minCOST']
        qty = secrets.choice(range(1, 3))
        uom_index = [i for i, d in enumerate(src_batch_bin_details['UOMS']) if 1 in d.values()][0]
        uom_details = src_batch_bin_details['UOMS'][uom_index]
        conv_factor = uom_details['CONV_FACTOR_SML']

        payload = {
            "WH_TRANSFER_TYPE": "B97D1268:6C14457A-F46E-4751-9FF2-3191EE621E0F",
            "TRANSFER_DATE": datetime.today().strftime("%Y-%m-%d"),
            "SOURCE_WH": src_whs_id,
            "REASON": rand_reason,
            "DEST_WH": dest_whs_id,
            "DEST_DIST": dest_dist_id if dest_dist_id is not None else "",
            "SOURCE_DIST": source_dist_id if source_dist_id is not None else "",
            "PO_REF": None,
            "REMARKS": "",
            "STATUS": "O",
            "PRIME_FLAG": "PRIME",
            "PRODUCT_DETAILS": [
                {
                    "PRODUCT_ID": prd_id,
                    "NET_AMT": str(src_cost_price * qty * conv_factor),
                    "COST_PRICE": str(src_cost_price),
                    "UOMS": [
                        {
                            "UOM_ID": uom_details["UOM_ID"],
                            "QUANTITY": str(qty)
                        }
                    ]
                }
            ]
        }

        if source_whs_type == "fully-managed" or source_whs_type == "damaged fully-managed":
            payload["PRODUCT_DETAILS"][0]['EXPIRY_DATE_SOURCE'] = src_batch_bin_details["EXPIRY_DATE"]
            payload["PRODUCT_DETAILS"][0]["BIN_ID"] = src_bin_details['BIN_ID']
            payload["PRODUCT_DETAILS"][0]["BATCH_ID"] = src_batch_details['BATCH_ID']

        if source_whs_type == "semi-managed" :
            payload["PRODUCT_DETAILS"][0]['EXPIRY_DATE_SOURCE'] = src_batch_bin_details["EXPIRY_DATE"]
            payload["PRODUCT_DETAILS"][0]["BATCH_ID"] = ''.join(filter(str.isdigit, src_batch_bin_details["EXPIRY_DATE"]))

        if dest_whs_type == "semi-managed":
            payload["PRODUCT_DETAILS"][0]['EXPIRY_DATE_DEST'] = dest_batch_bin_details["EXPIRY_DATE"]

        if dest_whs_type == "fully-managed" or dest_whs_type == "damaged fully-managed":
            payload["PRODUCT_DETAILS"][0]['DESTINATION_BATCH_CD'] = dest_batch_details["BATCH_CD"]
            payload["PRODUCT_DETAILS"][0]['EXPIRY_DATE_DEST'] = dest_batch_bin_details["EXPIRY_DATE"]
            payload["PRODUCT_DETAILS"][0]['DESTINATION_BIN_ID'] = dest_bin_details["BIN_ID"]
        return payload

    def prepare_wh(self, hq_prd_for_dist_ls, curr_whs_type, prd_id):
        valid_whs_ls = None
        found_available_qty = False
        batch_bin_details = None
        batch_details = None
        bin_details = None

        if curr_whs_type == "unmanaged":
            unmanage_extension = \
                "?filter={%22DIST_ID%22%3A{%22$eq%22%3A%223CAF4BF6%3AF0A6331B-3CFD-4DB4-9792-A27221CC2250%22}%2C%22WHS_BATCH_TRACE%22%3A{%22$eq%22%3Afalse}%2C%22WHS_EXP_MAND%22%3A{%22$eq%22%3Afalse}}"
            BuiltIn().set_test_variable("${whs_filter}", unmanage_extension)
            StockReceiptGet().user_retrieves_all_whs_available_for_dist()
            valid_whs_ls = BuiltIn().get_variable_value("${whs_for_dist_ls}")
        elif curr_whs_type == "semi-managed":
            semi_manage_extension = \
                "?filter={%22DIST_ID%22%3A{%22$eq%22%3A%223CAF4BF6%3AF0A6331B-3CFD-4DB4-9792-A27221CC2250%22}%2C%22WHS_BATCH_TRACE%22%3A{%22$eq%22%3Afalse}%2C%22WHS_EXP_MAND%22%3A{%22$eq%22%3Atrue}%2C%22IS_VARIANCE%22%3A{%22$eq%22%3Afalse}}"
            BuiltIn().set_test_variable("${whs_filter}", semi_manage_extension)
            StockReceiptGet().user_retrieves_all_whs_available_for_dist()
            valid_whs_ls = BuiltIn().get_variable_value("${whs_for_dist_ls}")
        elif curr_whs_type == "fully-managed":
            fully_manage_extension = \
                "?filter={%22DIST_ID%22%3A{%22$eq%22%3A%223CAF4BF6%3AF0A6331B-3CFD-4DB4-9792-A27221CC2250%22}%2C%22WHS_BATCH_TRACE%22%3A{%22$eq%22%3Atrue}%2C%22WHS_EXP_MAND%22%3A{%22$eq%22%3Atrue}%2C%22IS_VARIANCE%22%3A{%22$eq%22%3Afalse}}"
            BuiltIn().set_test_variable("${whs_filter}", fully_manage_extension)
            StockReceiptGet().user_retrieves_all_whs_available_for_dist()
            valid_whs_ls = BuiltIn().get_variable_value("${whs_for_dist_ls}")
        elif curr_whs_type == "damaged fully-managed":
            fully_manage_extension = \
                "?filter=%7B%0A%20%20%20%20%22DIST_ID%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22%24eq%22%3A%20%223CAF4BF6%3AF0A6331B-3CFD-4DB4-9792-A27221CC2250%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22WHS_BATCH_TRACE%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22%24eq%22%3A%20true%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22WHS_EXP_MAND%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22%24eq%22%3A%20true%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22IS_VARIANCE%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22%24eq%22%3A%20false%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22WHS_IS_DAMAGE%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22%24eq%22%3A%20true%0A%20%20%20%20%7D%0A%7D"
            curr_whs_type = "fully-managed"
            BuiltIn().set_test_variable("${whs_filter}", fully_manage_extension)
            StockReceiptGet().user_retrieves_all_whs_available_for_dist()
            valid_whs_ls = BuiltIn().get_variable_value("${whs_for_dist_ls}")

        StockAuditGet().user_retrieves_stock_audit_listing()
        stk_audit_ls = BuiltIn().get_variable_value("${stk_audit_ls}")
        invalid_whs_codes = [whs['WHS_CODE'] for whs in stk_audit_ls if whs['STATUS'] == "Open" \
                             or whs['STATUS'] == "Confirmed"]
        valid_whs_ids = [whs['ID'] for whs in valid_whs_ls if whs['WHS_CD'] not in invalid_whs_codes]
        prd_ids = [hq_prd_for_dist['PRD_ID'] for hq_prd_for_dist in hq_prd_for_dist_ls]
        StockReceiptPost().user_retrieves_batch_list_bulk(valid_whs_ids, prd_ids)
        batch_list_bulk = BuiltIn().get_variable_value("${batch_list_bulk}")
        if len(batch_list_bulk) > 0:
            for batch_bin in batch_list_bulk:
                if curr_whs_type == "unmanaged":
                    avail_qty = batch_bin['AVAILABLE_QTY']
                    if int(float(avail_qty)) > 5 or prd_id is not None:
                        batch_bin_details = batch_bin
                        found_available_qty = True
                        break

                if curr_whs_type == "semi-managed":
                    exp_dates = batch_bin['EXP_DATE_LIST']
                    for exp_date in exp_dates:
                        if int(float(exp_date['TOTAL_AVAILABLE_QTY'])) > 5 or prd_id is not None:
                            batch_bin_details = batch_bin
                            batch_details = exp_date
                            found_available_qty = True
                            break

                if curr_whs_type == "fully-managed":
                    batches = batch_bin['BATCH']
                    try:
                        for batch in batches:
                            bins = batch['BIN_ARR']
                            for bin in bins:
                                if int(float(bin['AVAILABLE_QTY'])) > 5 or prd_id is not None:
                                    bin_details = bin
                                    batch_details = batch
                                    batch_bin_details = batch_bin
                                    found_available_qty = True
                                    break
                            if found_available_qty:
                                break
                    except Exception:
                        if int(float(batches['AVAILABLE_QTY'])) > 5 or prd_id is not None:
                            batch_bin_details = batch_bin
                            found_available_qty = True
                            break
                if found_available_qty:
                    break
        else:
            print("No batch list found, please setup")
        assert found_available_qty, "Please prepare data first, " + curr_whs_type + " not setup properly"
        print("batch details = " + str(batch_bin_details))
        return batch_bin_details, batch_details, bin_details
