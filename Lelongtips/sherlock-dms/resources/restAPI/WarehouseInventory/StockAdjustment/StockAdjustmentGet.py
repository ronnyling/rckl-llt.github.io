
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL
MTDT_END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class StockAdjustmentGet(object):

    def user_retrieves_stock_adjustment_listing(self):
        url = "{0}inventory-stock-adjustment".format(INVT_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        if response.status_code == 201:
            BuiltIn().set_test_variable("${stock_adjustment_ls}", response.json())
        return response.status_code

    def user_retrieves_stock_adjustment_details(self):
        stock_adjustment_id = BuiltIn().get_variable_value("${stock_adjustment_id}")
        url = "{0}inventory-stock-adjustment/{1}".format(INVT_END_POINT_URL, stock_adjustment_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            BuiltIn().set_test_variable("${stock_adjustment_details}", response.json())
        print(response.status_code)
        return response.status_code

    def user_retrieves_all_stock_adjustment_types(self):
        url = "{0}module-data/stock-adjustment-types".format(MTDT_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${stock_adjustment_type_ls}", response.json())
        print(response.status_code)
        return response.status_code
