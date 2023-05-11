from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL
MTDT_DIST_END_POINT_URL = PROTOCOL + "metadata" + APP_URL

class StockAuditCancel(object):

    def user_cancels_stock_out(self):
        url = "{0}inventory/audit/cancel".format(INVT_END_POINT_URL)
        stk_audit_id = BuiltIn().get_variable_value("${stk_audit_id}")
        payload = [stk_audit_id]
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code
