import json
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI.VanInventory.VanStockRequest.VanStockRequestGet import VanStockRequestGet

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL


class VanStockRequestReject(object):
    def user_puts_to_reject_van_stock_request(self):
        stk_req_id = BuiltIn().get_variable_value("${stk_req_id}")
        if stk_req_id is None:
            VanStockRequestGet().user_retrieves_van_stock_request_listing()
            van_stk_req_ls = BuiltIn().get_variable_value("${van_stk_req_ls}")
            valid_stk_req_id = next(van_stk_req['ID'] for van_stk_req in van_stk_req_ls if van_stk_req['STATUS'] == "P")
            stk_req_id = valid_stk_req_id
            assert stk_req_id is not None, "Please prepare open/pending status for this operation"
        payload = self.gen_reject_stk_request_payload(stk_req_id)
        payload = json.dumps(payload)
        url = "{0}van-stock-request{1}".format(INVT_END_POINT_URL, stk_req_id)
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code

    def gen_reject_stk_request_payload(self, stk_req_id):
        payload = {
            "STATUS": "R",
            "ID": stk_req_id,
            "PRIME_FLAG": "PRIME"
        }
        return payload
