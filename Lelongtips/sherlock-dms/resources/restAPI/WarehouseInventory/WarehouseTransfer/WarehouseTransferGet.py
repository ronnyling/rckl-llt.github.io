import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL
PRFL_DIST_END_POINT_URL = PROTOCOL + "profile-dist" + APP_URL

class WarehouseTransferGet(object):

    def user_retrieves_warehouse_transfer_listing(self):
        url = "{0}inventory-warehouse-transfer".format(INVT_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${whs_trsf_ls}", response.json())
        return response.status_code

    def user_retrieves_warehouse_transfer_details(self):
        whs_trsf_id = BuiltIn().get_variable_value("${whs_trsf_id}")
        if whs_trsf_id is None:
            self.user_retrieves_warehouse_transfer_listing()
            whs_trsf_ls = BuiltIn().get_variable_value("${whs_trsf_ls}")
            rand = secrets.choice(whs_trsf_ls)
            rand_whs_trsf_id = rand['TXN_ID']
            whs_trsf_id = rand_whs_trsf_id
            BuiltIn().set_test_variable("${whs_trsf_id}", whs_trsf_id)

        url = "{0}inventory-warehouse-transfer/{1}".format(INVT_END_POINT_URL, whs_trsf_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${whs_trsf_details}", response.json())
        print(response.status_code)
        return response.status_code

    def user_retrieves_main_dist_by_sub_dist(self):
        url = "{0}get-main-dist-by-sub-dist".format(PRFL_DIST_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${main_dist_sub_dist_ls}", response.json())
        print(response.status_code)
        return response.status_code

    def user_retrieves_warehouse_product_list(self, dist_id, whs_id):
        url = "{0}warehouse-product-list/{1}/{2}".format(INVT_END_POINT_URL, dist_id, whs_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${whs_prd_ls}", response.json())
        print(response.status_code)
        return response.status_code


