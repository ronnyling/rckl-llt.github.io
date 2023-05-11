from resources.restAPI import PROTOCOL, APP_URL
import json
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Product import ProductPost
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "product" + APP_URL


class ProductPut:

    @keyword('user updates product with ${data_type} data')
    def user_updates_product(self, data_type):
        update_detail = BuiltIn().get_variable_value("${update_product_details}")
        prod_id = BuiltIn().get_variable_value("${prd_id}")
        prd_cd = BuiltIn().get_variable_value("${prd_cd}")
        if update_detail is not None:
            payload = {"ID": prod_id, "PRD_CD": prd_cd}
            update_detail.update(payload)
        else:
            update_detail = {"ID": prod_id, "PRD_CD": prd_cd}
        BuiltIn().set_test_variable("${update_product_details}", update_detail)
        url = "{0}product/{1}".format(END_POINT_URL, prod_id)
        payload = ProductPost.ProductPost().payload_product_master_info("hqadm")
        payload = json.dumps(payload)
        print("payload ", payload)
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code

