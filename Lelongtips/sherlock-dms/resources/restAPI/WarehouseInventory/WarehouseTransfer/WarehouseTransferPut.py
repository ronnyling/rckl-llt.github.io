
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

from resources.restAPI.WarehouseInventory.WarehouseTransfer.WarehouseTransferGet import WarehouseTransferGet

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL

class WarehouseTransferPut(object):

    @keyword("user puts to ${operation} warehouse transfer")
    def user_puts_warehouse_transfer(self, operation):
        whs_trsf_id = BuiltIn().get_variable_value("${whs_trsf_id}")
        WarehouseTransferGet().user_retrieves_warehouse_transfer_details()
        whs_trsf_details = BuiltIn().get_variable_value("${whs_trsf_details}")

        url = "{0}inventory-warehouse-transfer/{1}".format(INVT_END_POINT_URL, whs_trsf_id)
        whs_trsf_payload = whs_trsf_details
        if operation == "confirm":
            whs_trsf_payload['STATUS'] = 'C'
            whs_trsf_payload['POST_TYPE'] = 'save and confirm'

        elif operation == "save":
            whs_trsf_payload['STATUS'] = 'O'
            whs_trsf_payload['POST_TYPE'] = 'save'

        payload = json.dumps(whs_trsf_payload)
        print("payload = " + str(payload))
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code
