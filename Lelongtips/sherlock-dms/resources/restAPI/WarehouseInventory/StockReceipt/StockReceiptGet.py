import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL
CDTBL_END_POINT_URL = PROTOCOL + "codetable" + APP_URL
MTDT_END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class StockReceiptGet(object):

    def user_retrieves_stock_receipt_listing(self):
        url = "{0}inventory-stock-receipt".format(INVT_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${stock_receipt_ls}", response.json())
        return response.status_code

    def user_retrieves_bin_batch_details_for_stock_receipt(self):
        stock_receipt_details = BuiltIn().get_variable_value("${stock_receipt_details}")
        print("stock receipt details = ", str(stock_receipt_details))
        prd_id = BuiltIn().get_variable_value("${prd_id}")
        if prd_id is None:
            product_id_first = stock_receipt_details['PRODUCT_DETAILS'][0]['PRODUCT_ID']
        whs_id = BuiltIn().get_variable_value("${whs_id}")
        if whs_id is None:
            whs_id_first = stock_receipt_details['WAREHOUSE']
        url = "{0}batch-bin-list/{1}/{2}".format(INVT_END_POINT_URL, product_id_first, whs_id_first)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("batch_bin_ls", response.json())
        print(response.status_code)
        return response.status_code

    def user_retrieves_stock_receipt_details(self):
        stock_receipt_id = BuiltIn().get_variable_value("${stock_receipt_id}")
        if stock_receipt_id is None:
            self.user_retrieves_stock_receipt_listing()
            stock_receipt_ls = BuiltIn().get_variable_value("${stock_receipt_ls}")
            rand = secrets.choice(stock_receipt_ls)
            rand_stock_receipt_id = rand['TXN_ID']
            stock_receipt_id = rand_stock_receipt_id
            BuiltIn().set_test_variable("${stock_receipt_id}", rand_stock_receipt_id)
        url = "{0}inventory-stock-receipt/{1}".format(INVT_END_POINT_URL, stock_receipt_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${stock_receipt_details}", response.json())
        print(response.status_code)
        return response.status_code

    def user_retrieves_all_inventory_status_from_codetable(self):
        url = "{0}codetable/INVENTORY_STATUS".format(CDTBL_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code

    def user_retrieves_all_whs_available_for_dist(self):
        default_filter = "?filter=%20{%22DIST_ID%22:{%22$eq%22:%223CAF4BF6:F0A6331B-3CFD-4DB4-9792-A27221CC2250%22}}"
        whs_filter = BuiltIn().get_variable_value("${whs_filter}")
        if whs_filter is not None:
            extension = whs_filter
        else:
            extension = default_filter
        url = "{0}module-data/warehouse{1}".format(MTDT_END_POINT_URL, extension)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${whs_for_dist_ls}", response.json())
        print(response.status_code)
        return response.status_code

    def user_retrieves_all_supplier_available_for_dist(self):
        extension = "?filter={%22FIELDS%22:[%22ID%22,%22MODIFIED_DATE%22,%22SUPP_CD%22,%22SUPP_NAME%22,%22REG_NO%22,%22PRIME_FLAG%22],%22FILTER%22:[]}&silent=null"
        url = "{0}module-data/supplier{1}".format(MTDT_END_POINT_URL, extension)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${supplier_for_dist_ls}", response.json())
        print(response.status_code)
        return response.status_code

    def user_retrieves_all_bin_for_whs(self,whs_id):
        url = "{0}module-data/warehouse-bin".format(MTDT_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            bins = []
            whs_bin = response.json()
            for bin in whs_bin:
                if bin['WAREHOUSE_CODE'] == whs_id:
                    bins.append(bin)
            BuiltIn().set_test_variable("${bins_for_whs}", bins)
        print(response.status_code)
        return response.status_code
