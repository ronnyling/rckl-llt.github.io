from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

from resources.restAPI.WarehouseInventory.StockAdjustment.StockAdjustmentPost import StockAdjustmentPost

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL

class StockAdjustmentPut(object):

    @keyword("user puts to ${mode} stock adjustment")
    def user_puts_stock_adjustment(self, mode):
        post_type = None
        if mode == "save":
            post_type = "O"
        elif mode == "confirm":
            post_type = "C"

        stock_adjustment_id = BuiltIn().get_variable_value("${stock_adjustment_id}")
        payload = BuiltIn().get_variable_value("${stock_adjustment_payload}")
        if payload is None:
            payload = StockAdjustmentPost().gen_stock_adjustment_payload()
        payload = json.loads(payload)
        payload['STATUS'] = post_type
        payload = json.dumps(payload)
        print("payload stoack adjustment = " + str(payload))
        url = "{0}inventory-stock-adjustment/{1}".format(INVT_END_POINT_URL, stock_adjustment_id)
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code


