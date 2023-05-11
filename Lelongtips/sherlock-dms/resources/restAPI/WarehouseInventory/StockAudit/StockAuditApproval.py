
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL


class StockAuditApproval(object):
    @keyword("user puts to ${approval} stock audit approval")
    def user_puts_to_stock_audit(self, approval):
        stk_audit_id = BuiltIn().get_variable_value("${stk_audit_id}")

        url = "{0}inventory-stock-audit/action/{1}}".format(INVT_END_POINT_URL, approval)
        payload = [stk_audit_id]
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code
