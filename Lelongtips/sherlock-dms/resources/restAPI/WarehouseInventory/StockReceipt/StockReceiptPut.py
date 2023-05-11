import secrets
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

from resources.restAPI.WarehouseInventory.StockReceipt.StockReceiptPost import StockReceiptPost

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL

class StockReceiptPut(object):

    @keyword("user puts to ${mode} stock receipt")
    def user_puts_stock_receipt(self, mode):
        post_type = None
        if mode == "save":
            post_type = "save"
        elif mode == "confirm":
            post_type = "save and confirm"

        stock_receipt_id = BuiltIn().get_variable_value("${stock_receipt_id}")
        payload = BuiltIn().get_variable_value("${stock_receipt_payload}")
        if payload is None:
            StockReceiptPost().gen_stock_receipt_payload("save")
        payload = json.loads(payload)
        payload['POST_TYPE'] = post_type
        payload = json.dumps(payload)
        url = "{0}inventory-stock-receipt/{1}".format(INVT_END_POINT_URL, stock_receipt_id)
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code


