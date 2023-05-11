import secrets
from datetime import datetime

from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

from resources.restAPI.MasterDataMgmt.Product.ProductUomGet import ProductUomGet
from resources.restAPI.WarehouseInventory.StockAudit.StockAuditGet import StockAuditGet
from resources.restAPI.WarehouseInventory.StockReceipt.StockReceiptGet import StockReceiptGet
from resources.restAPI.WarehouseInventory.StockReceipt.StockReceiptPost import StockReceiptPost
from resources.restAPI.WarehouseInventory.WarehouseTransfer.WarehouseTransferGet import WarehouseTransferGet

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL

class StockAuditPut(object):
    @keyword("user puts to ${operation} stock audit")
    def user_puts_to_stock_audit(self, operation):
        stk_audit_id = BuiltIn().get_variable_value("${stk_audit_id}")

        url = "{0}inventory-stock-audit/{1}".format(INVT_END_POINT_URL, stk_audit_id)
        payload = self.gen_stk_audit_payload(operation, stk_audit_id)
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code

    def gen_stk_audit_payload(self, operation, stk_audit_id):
        bin_whs = None
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        BuiltIn().set_test_variable("${stk_audit_id}", stk_audit_id)
        StockAuditGet().user_retrieves_stock_audit_details()
        stk_audit_payload = json.loads(BuiltIn().get_variable_value("${stk_audit_payload}"))
        payload = stk_audit_payload
        whs_id = payload['WAREHOUSE']
        WarehouseTransferGet().user_retrieves_warehouse_product_list(distributor_id, whs_id)
        whs_prd_ls = BuiltIn().get_variable_value("${whs_prd_ls}")
        rand_prd = secrets.choice(whs_prd_ls)
        rand_prd_details = rand_prd
        StockReceiptPost().user_retrieves_batch_list_bulk([whs_id], [rand_prd_details['ID']])
        batch_list_bulk = BuiltIn().get_variable_value("${batch_list_bulk}")
        BuiltIn().set_test_variable("${prd_id}", rand_prd_details['ID'])
        ProductUomGet().user_retrieves_previous_prd_uom()
        uoms = BuiltIn().get_variable_value("${prd_uom_ls}")
        uom_details = next((uom for uom in uoms if uom['CONV_FACTOR_SML'] == 1))

        whs_type = BuiltIn().get_variable_value("${whs_type}")
        if whs_type == "fully-managed":
            StockReceiptGet().user_retrieves_all_bin_for_whs(whs_id)
            bins_for_whs = BuiltIn().get_variable_value("${bins_for_whs}")
            rand_bin = secrets.choice(bins_for_whs)
            bin_whs = rand_bin


        batch_details = None
        batch_found = False
        if len(batch_list_bulk) > 0:
            for batch in batch_list_bulk[0]['BATCH']:
                if len(batch['BIN_ARR']) > 0:
                    for bin in batch['BIN_ARR']:
                        if bin['BIN_ID'] == bin_whs['ID']:
                            batch_details = batch
                            batch_found = True
                            break
                if batch_found:
                    break

        payload['PRODUCT_DETAILS'] = [
            {
                "PRODUCT_ID": rand_prd_details['ID'],
                "PRODUCT_CD": rand_prd_details['PRD_CD'],
                "PRODUCT_DESC": rand_prd_details['PRD_DESC'],
                "BATCH_ID": batch_details['BATCH_ID'],
                "BATCH_DESC": batch_details['BATCH_CD'],
                "BIN_ID": bin_whs['ID'] if bin_whs is not None else None,
                "BIN_DESC": bin_whs['BIN_DESC'] if bin_whs is not None else None,
                "UOMS": [
                    {
                        "UOM_ID": uom_details['ID'],
                        "QUANTITY": 100 if int(float(rand_prd_details['AVAILABLE_QTY'])) < 5 else int(float(rand_prd_details['AVAILABLE_QTY'])) + 5
                    }
                ]
            }
        ]
        payload['STOCK_AUDIT_DATE'] = datetime.today().strftime("%Y-%m-%d")
        if operation == "save":
            payload['STATUS'] = "O"
        elif operation == "confirm":
            payload['STATUS'] = "C"
        return payload
