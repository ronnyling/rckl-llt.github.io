import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL
SETTING_END_POINT_URL = PROTOCOL + "setting" + APP_URL
MTDT_DIST_END_POINT_URL = PROTOCOL + "metadata" + APP_URL
PS_END_POINT_URL = PROTOCOL + "product-sector" + APP_URL


class VanReplenishmentGet(object):
    def user_retrieves_van_replenishment_listing(self):
        url = "{0}van-replenishment".format(INVT_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${van_repl_ls}", response.json())
        return response.status_code

    def user_retrieves_van_replenishment_details(self):
        van_rep_id = BuiltIn().get_variable_value("${van_rep_id}")
        if van_rep_id is None:
            self.user_retrieves_van_replenishment_listing()
            van_repl_ls = BuiltIn().get_variable_value("${van_repl_ls}")
            rand = secrets.choice(van_repl_ls)
            rand_van_repl_id = rand['ID']
            van_rep_id = rand_van_repl_id
            BuiltIn().set_test_variable("${van_repl_id}", van_rep_id)

        url = "{0}van-replenishment/{1}".format(INVT_END_POINT_URL, van_rep_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${van_rep_details}", response.json())
        print(response.status_code)
        return response.status_code

    def user_retrieves_all_prd_for_dist_status(self):
        url = "{0}all-product-for-dist-status".format(PS_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            body_result = response.json()
            valid_prd_for_dist_ls = [prd for prd in body_result
                                     if prd.get('SELLING_IND', None) == "1"
                                     and prd.get('STATUS', None) == 'Active'
                                     and prd.get('PRIORITY', None) == 'Active'
                                     and prd.get('UOMS', None) is not None
                                     and prd.get('COST_PRICE', None) is not None
                                     ]
            BuiltIn().set_test_variable("${valid_prd_for_dist_ls}", valid_prd_for_dist_ls)
        print(response.status_code)
        return response.status_code
