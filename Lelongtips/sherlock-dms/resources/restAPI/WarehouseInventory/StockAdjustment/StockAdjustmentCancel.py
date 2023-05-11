from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL

class StockAdjustmentCancel(object):

    @keyword("user cancel stock adjustment")
    def user_cancel_stock_adjustment(self):
        stock_adjustment_id = BuiltIn().get_variable_value("${stock_adjustment_id}")

        payload = self.gen_stock_adjustment_cancel_payload(stock_adjustment_id)
        payload = json.dumps(payload)
        url = "{0}inventory/receipt/cancel".format(INVT_END_POINT_URL, stock_adjustment_id)
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code

    def gen_stock_adjustment_cancel_payload(self, stock_adjustment_id):
        payload = []
        payload.append(stock_adjustment_id)
        return payload


