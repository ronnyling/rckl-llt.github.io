import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL
MTDT_DIST_END_POINT_URL = PROTOCOL + "metadata" + APP_URL

class StockAuditGet(object):

    def user_retrieves_stock_audit_listing(self):
        url = "{0}inventory-stock-audit".format(INVT_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${stk_audit_ls}", response.json())
        return response.status_code

    def user_retrieves_stock_audit_details(self):
        stk_audit_id = BuiltIn().get_variable_value("${stk_audit_id}")
        if stk_audit_id is None:
            self.user_retrieves_stock_audit_listing()
            stk_audit_ls = BuiltIn().get_variable_value("${stk_audit_ls}")
            rand = secrets.choice(stk_audit_ls)
            rand_stk_audit_id = rand['TXN_ID']
            stk_audit_id = rand_stk_audit_id
            BuiltIn().set_test_variable("${stk_audit_id}", stk_audit_id)

        url = "{0}inventory-stock-audit/{1}".format(INVT_END_POINT_URL, stk_audit_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${stk_audit_details}", response.json())
        print(response.status_code)
        return response.status_code

    def user_retrieves_audit_type_id_by_audit_type(self, audit_type):
        if audit_type == "bin":
            audit_code = "B"
        elif audit_type == "product":
            audit_code = "P"
        url = "{0}module-data/stock-audit-type".format(MTDT_DIST_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            audit_types = response.json()
            audit_type_id = None
            for audit_type_object in audit_types:
                if audit_type_object['CODE'] == audit_code:
                    audit_type_id = audit_type_object['ID']
                    break
            BuiltIn().set_test_variable("${stk_audit_type_id}", audit_type_id)
        print(response.status_code)
        return response.status_code

