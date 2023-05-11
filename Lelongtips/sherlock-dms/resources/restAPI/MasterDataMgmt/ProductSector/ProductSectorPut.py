from resources.restAPI import PROTOCOL, APP_URL
import json
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.ProductSector.ProductSectorPost import ProductSectorPost
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "product-sector" + APP_URL


class ProductSectorPut:
    @keyword('user updates product sector with ${data_type} data')
    def user_updates_product_sector(self, data_type):
        update_detail = BuiltIn().get_variable_value("${update_product_sector_details}")
        prod_sector_id = BuiltIn().get_variable_value("${product_sector_id}")
        if update_detail is not None:
            payload = {"ID": prod_sector_id}
            update_detail.update(payload)
        else:
            update_detail = {"ID": prod_sector_id}
        BuiltIn().set_test_variable("${update_product_sector_details}", update_detail)
        url = "{0}product-sector/{1}".format(END_POINT_URL, prod_sector_id)
        payload = ProductSectorPost().product_sector_general_payload()
        print("payload ", payload)
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code
