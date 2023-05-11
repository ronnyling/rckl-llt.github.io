
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL

class WarehouseTransferCancel(object):

    @keyword("user puts to cancel warehouse transfer")
    def user_puts_warehouse_transfer(self):
        whs_trsf_id = BuiltIn().get_variable_value("${whs_trsf_id}")
        url = "{0}inventory/war_transfer/cancel".format(INVT_END_POINT_URL)
        payload = json.dumps([whs_trsf_id])
        print("payload = " + str(payload))
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code
