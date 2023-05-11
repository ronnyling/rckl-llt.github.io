
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

from resources.restAPI.WarehouseInventory.StockOut.StockOutGet import StockOutGet

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL

class StockOutPut(object):
    @keyword("user puts to ${operation} stock out")
    def user_puts_to_stock_audit(self, operation):
        stk_out_id = BuiltIn().get_variable_value("${stk_out_id}")

        url = "{0}inventory-stock-out/{1}".format(INVT_END_POINT_URL, stk_out_id)
        payload = self.gen_stk_out_payload(operation, stk_out_id)
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code

    def gen_stk_out_payload(self, operation, stk_out_id):
        BuiltIn().set_test_variable("${stk_out_id}", stk_out_id)
        StockOutGet().user_retrieves_stock_out_details()
        stk_out_payload = json.loads(BuiltIn().get_variable_value("${stk_out_payload}"))
        payload = stk_out_payload
        if operation == "save":
            payload['STATUS'] = "O"
        elif operation == "confirm":
            payload['STATUS'] = "C"
        return payload
