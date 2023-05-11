import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL
SETTING_END_POINT_URL = PROTOCOL + "setting" + APP_URL
MTDT_DIST_END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class VanStockInGet(object):
    def user_retrieves_van_stock_in_listing(self):
        url = "{0}van-stock-in".format(INVT_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${van_stk_in_ls}", response.json())
        return response.status_code

    def user_retrieves_van_stock_in_details(self):
        van_stk_in_id = BuiltIn().get_variable_value("${van_stk_in_id}")
        if van_stk_in_id is None:
            self.user_retrieves_van_stock_in_listing()
            van_stk_in_ls = BuiltIn().get_variable_value("${van_stk_in_ls}")
            rand = secrets.choice(van_stk_in_ls)
            rand_van_stk_in_id = rand['ID']
            van_stk_in_id = rand_van_stk_in_id
            BuiltIn().set_test_variable("${van_stk_in_id}", van_stk_in_id)

        url = "{0}van-stock-in/{1}".format(INVT_END_POINT_URL, van_stk_in_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${van_stk_in_details}", response.json())
        print(response.status_code)
        return response.status_code
