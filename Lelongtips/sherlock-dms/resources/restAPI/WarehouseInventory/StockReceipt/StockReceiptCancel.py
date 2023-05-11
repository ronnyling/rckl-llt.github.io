from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL

class StockReceiptCancel(object):

    @keyword("user cancel stock receipt")
    def user_cancel_stock_receipt(self):
        stock_receipt_id = BuiltIn().get_variable_value("${stock_receipt_id}")

        payload = self.gen_stock_receipt_cancel_payload(stock_receipt_id)
        payload = json.dumps(payload)
        url = "{0}inventory/receipt/cancel".format(INVT_END_POINT_URL, stock_receipt_id)
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code

    def gen_stock_receipt_cancel_payload(self, stock_receipt_id):
        payload = []
        payload.append(stock_receipt_id)
        return payload


