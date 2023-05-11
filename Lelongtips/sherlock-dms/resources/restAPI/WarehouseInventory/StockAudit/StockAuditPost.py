import secrets

from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

from resources.restAPI.WarehouseInventory.StockAudit.StockAuditGet import StockAuditGet
from resources.restAPI.WarehouseInventory.StockReceipt.StockReceiptGet import StockReceiptGet
from resources.restAPI.WarehouseInventory.WarehouseTransfer.WarehouseTransferGet import WarehouseTransferGet

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL
TYPE_FM = "fully-managed"
TYPE_SM = "semi-managed"
TYPE_UM = "unmanaged"

class StockAuditPost(object):
    @keyword("user post to save stock audit by ${stk_audit_type}")
    def user_post_to_stock_audit(self, stk_audit_type):
        stk_audit_excl_prd_ls = BuiltIn().get_variable_value("${stk_audit_excl_prd_ls}")
        if stk_audit_excl_prd_ls is None:
            self.user_post_to_exclude_product_in_stock_audit(stk_audit_type)
            stk_audit_excl_prd_ls = BuiltIn().get_variable_value("${stk_audit_excl_prd_ls}")
            stk_audit_excl_payload = BuiltIn().get_variable_value("${stk_audit_excl_payload}")
        else:
            stk_audit_excl_payload = BuiltIn().get_variable_value("${stk_audit_excl_payload}")
        url = "{0}inventory-stock-audit".format(INVT_END_POINT_URL)
        payload = self.gen_stk_audit(stk_audit_excl_payload, stk_audit_excl_prd_ls)
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${stk_audit_payload}", payload)
            BuiltIn().set_test_variable("${stk_audit_id}", response.json()['stockAuditId'])
        print(response.status_code)
        return response.status_code

    def gen_stk_audit(self, stk_audit_excl_payload, stk_audit_excl_prd_ls):
        stk_audit_excl_payload['REMARKS'] = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15))
        stk_audit_excl_payload['STATUS'] = 'O'


        excl_prds = [prd['PRD_ID'] for prd in stk_audit_excl_prd_ls]
        all_prds = stk_audit_excl_payload['SELECTED_IDS']
        valid_prds = [prd for prd in all_prds if prd not in excl_prds]
        stk_audit_excl_payload['SELECTED_IDS'] = valid_prds
        payload = stk_audit_excl_payload
        return payload

    @keyword("user post to retrieve excluded product for stock audit by ${audit_type}")
    def user_post_to_exclude_product_in_stock_audit(self, audit_type):
        url = "{0}inventory-stock-audit/exclude-product".format(INVT_END_POINT_URL)
        payload = self.gen_stk_audit_excl_payload(audit_type)
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${stk_audit_excl_prd_ls}", response.json())
            BuiltIn().set_test_variable("${stk_audit_excl_payload}", json.loads(payload))
        print(response.status_code)
        return response.status_code

    def gen_stk_audit_excl_payload(self, audit_type):
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        StockAuditGet().user_retrieves_audit_type_id_by_audit_type(audit_type)
        stk_audit_type_id = BuiltIn().get_variable_value("${stk_audit_type_id}")

        whs_type = None
        if audit_type == "product":
            whs_filter = None
            whs_type = secrets.choice([TYPE_UM, TYPE_SM, TYPE_FM])
            match whs_type:
                case "unmanaged":
                    whs_filter = "?filter={%22DIST_ID%22%3A{%22$eq%22%3A%223CAF4BF6%3AF0A6331B-3CFD-4DB4-9792-A27221CC2250%22}%2C%22WHS_BATCH_TRACE%22%3A{%22$eq%22%3Afalse}%2C%22WHS_EXP_MAND%22%3A{%22$eq%22%3Afalse}}"
                case "semi-managed":
                    whs_filter = "?filter={%22DIST_ID%22%3A{%22$eq%22%3A%223CAF4BF6%3AF0A6331B-3CFD-4DB4-9792-A27221CC2250%22}%2C%22WHS_BATCH_TRACE%22%3A{%22$eq%22%3Afalse}%2C%22WHS_EXP_MAND%22%3A{%22$eq%22%3Atrue}%2C%22IS_VARIANCE%22%3A{%22$eq%22%3Afalse}}"
                case "fully-managed":
                    whs_filter = "?filter={%22DIST_ID%22%3A{%22$eq%22%3A%223CAF4BF6%3AF0A6331B-3CFD-4DB4-9792-A27221CC2250%22}%2C%22WHS_BATCH_TRACE%22%3A{%22$eq%22%3Atrue}%2C%22WHS_EXP_MAND%22%3A{%22$eq%22%3Atrue}%2C%22IS_VARIANCE%22%3A{%22$eq%22%3Afalse}}"
            BuiltIn().set_test_variable("${whs_filter}", whs_filter)
        elif audit_type == "bin":
            whs_type = secrets.choice([TYPE_FM])
            whs_filter = "?filter={%22DIST_ID%22%3A{%22$eq%22%3A%223CAF4BF6%3AF0A6331B-3CFD-4DB4-9792-A27221CC2250%22}%2C%22WHS_BATCH_TRACE%22%3A{%22$eq%22%3Atrue}%2C%22WHS_EXP_MAND%22%3A{%22$eq%22%3Atrue}%2C%22IS_VARIANCE%22%3A{%22$eq%22%3Afalse}}"
            BuiltIn().set_test_variable("${whs_filter}", whs_filter)

        BuiltIn().set_test_variable("${whs_type}", whs_type)
        StockReceiptGet().user_retrieves_all_whs_available_for_dist()
        whs_all = BuiltIn().get_variable_value("${whs_for_dist_ls}")
        StockAuditGet().user_retrieves_stock_audit_listing()
        stk_audit_ls = BuiltIn().get_variable_value("${stk_audit_ls}")
        invalid_whs_codes = [whs['WHS_CODE'] for whs in stk_audit_ls if whs['STATUS'] == "Open"]

        whs_bins = []
        prd_ls = []
        ids = []
        if audit_type == "bin":
            for whs in whs_all:
                WarehouseTransferGet().user_retrieves_warehouse_product_list(distributor_id, whs['ID'])
                whs_prd_ls = BuiltIn().get_variable_value("${whs_prd_ls}")
                if len(whs_prd_ls) > 0:
                    StockReceiptGet().user_retrieves_all_bin_for_whs(whs['ID'])
                    bins_for_whs = BuiltIn().get_variable_value("${bins_for_whs}")
                    if len(bins_for_whs) > 0 and whs['WHS_CD'] not in invalid_whs_codes:
                        rand_whs_id = whs['ID']
                        whs_bins = bins_for_whs
                        break
            ids = [whs_bin['ID'] for whs_bin in whs_bins]
            is_prd = False

        elif audit_type == "product":
            for whs in whs_all:
                WarehouseTransferGet().user_retrieves_warehouse_product_list(distributor_id, whs['ID'])
                whs_prd_ls = BuiltIn().get_variable_value("${whs_prd_ls}")
                if whs_prd_ls is not None and whs['WHS_CD'] not in invalid_whs_codes:
                    rand_whs_id = whs['ID']
                    prd_ls = whs_prd_ls
                    break
            ids = [prd['ID'] for prd in prd_ls]
            is_prd = True

        payload = {
            "PRIME_FLAG": "PRIME",
            "WAREHOUSE": rand_whs_id,
            "AUDIT_TYPE": stk_audit_type_id,
            "SELECTED_IDS": ids,
            "IS_PRODUCT_ID": is_prd
        }
        return payload
