from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL

class InventoryListGet(object):

    def user_retrieves_inventory_summary_for_all_warehouse(self):
        extension = "Good%20Stock/false/false/Selling%20Price/false/false/false/prime"
        url = "{0}inventory-summary/{1}".format(INVT_END_POINT_URL, extension)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        if response.status_code == 200:
            BuiltIn().set_test_variable("${whs_list}", response.json())
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code

    def user_retrieves_warehouse_with_bin_batch(self):
        self.user_retrieves_inventory_summary_for_all_warehouse()
        whs_list = BuiltIn().get_variable_value("${whs_list}")
        whs_with_bin_batch = {}
        for whs in whs_list:
            if whs['WAREHOUSE_TYPE'] == "managed":
                whs_with_bin_batch = whs
                break
        return whs_with_bin_batch

    def user_retrieves_bin_wise_details_for_wh(self):
        whs_with_bin_batch = self.user_retrieves_warehouse_with_bin_batch()
        product_id = whs_with_bin_batch['PRODUCT_ID']
        whs_id = whs_with_bin_batch['WAREHOUSE_ID']
        url = "{0}inventory-summary/{1}/{2}/prime".format(INVT_END_POINT_URL, product_id, whs_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code
