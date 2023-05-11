from resources.restAPI import PROTOCOL, APP_URL
import json
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Product.ProductUomPost import ProductUomPost
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "product" + APP_URL


class ProductUomPut:

    @keyword('user updates product uom with ${data_type} data')
    def user_updates_product_uom(self, data_type):
        prd_id = BuiltIn().get_variable_value("${prd_id}")
        prd_uom_id = BuiltIn().get_variable_value("${prd_uom_id}")
        url = "{0}product/{1}/product-uom/{2}".format(END_POINT_URL, prd_id, prd_uom_id)
        payload = ProductUomPost().payload('updates')
        payload = json.dumps(payload)
        print("payload ", payload)
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${prd_uom_id}", body_result["ID"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)
