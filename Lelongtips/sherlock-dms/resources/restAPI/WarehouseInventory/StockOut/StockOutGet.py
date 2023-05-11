import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI.Config.ReferenceData.ReasonType.ReasonGet import ReasonGet

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL
SETTING_END_POINT_URL = PROTOCOL + "setting" + APP_URL
MTDT_DIST_END_POINT_URL = PROTOCOL + "metadata" + APP_URL

class StockOutGet(object):

    def user_retrieves_stock_out_listing(self):
        url = "{0}inventory-stock-out".format(INVT_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${stk_out_ls}", response.json())
        return response.status_code

    def user_retrieves_stock_out_details(self):
        stk_out_id = BuiltIn().get_variable_value("${stk_out_id}")
        if stk_out_id is None:
            self.user_retrieves_stock_out_listing()
            stk_out_ls = BuiltIn().get_variable_value("${stk_out_ls}")
            rand = secrets.choice(stk_out_ls)
            rand_stk_out_id = rand['TXN_ID']
            stk_out_id = rand_stk_out_id
            BuiltIn().set_test_variable("${stk_out_id}", stk_out_id)

        url = "{0}inventory-stock-out/{1}".format(INVT_END_POINT_URL, stk_out_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${stk_out_details}", response.json())
        print(response.status_code)
        return response.status_code

    def user_retrieves_rand_reason_for_stock_out_type(self):
        ReasonGet().user_retrieves_all_reasons_for_all_operations()
        rsn_all_ops_ls = BuiltIn().get_variable_value("${rsn_all_ops_ls}")
        # print("why empty " + str(rsn_all_ops_ls))
        stock_out_rsn_type_id = next((i['ID'] for i in rsn_all_ops_ls if i['REASON_TYPE_CD'] == 'ISO'))
        BuiltIn().set_test_variable("${res_bd_reason_type_id}", stock_out_rsn_type_id)
        ReasonGet().user_retrieves_all_reasons()
        rand_reason_id = BuiltIn().get_variable_value("${rand_reason}")
        BuiltIn().set_test_variable("${rand_stkout_rsn_id}", rand_reason_id)

    def user_retrieves_rand_stock_out_type(self):
        url = "{0}module-data/stock-out-types".format(MTDT_DIST_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            rand_type = secrets.choice(response.json())
            BuiltIn().set_test_variable("${rand_stkout_type_id}", rand_type['ID'])
        print(response.status_code)
        return response.status_code

    def user_retrieves_rand_stock_out_return_type(self):
        url = "{0}module-data/stock-out-return-type".format(MTDT_DIST_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            rand_rtn_type = secrets.choice(response.json())
            BuiltIn().set_test_variable("${rand_stkout_return_type_id}", rand_rtn_type['ID'])
        print(response.status_code)
        return response.status_code
