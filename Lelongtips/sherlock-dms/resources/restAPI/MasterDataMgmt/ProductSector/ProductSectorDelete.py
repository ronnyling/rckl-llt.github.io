from resources.restAPI import PROTOCOL, APP_URL, Common, BuiltIn
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "product-sector" + APP_URL

class ProductSectorDelete:

    @keyword('user deletes ${cond} product sector')
    def user_deletes_product_sector(self, cond):
        if cond == 'invalid':
            ps_id = Common().generate_random_id("0")
        else:
            ps_id = BuiltIn().get_variable_value("${product_sector_id}")
        url = "{0}product-sector/{1}".format(END_POINT_URL, ps_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        print("Get Status code for product sector info is " + str(response.status_code))
        if response.status_code != 200:
            print(response.text)
        BuiltIn().set_test_variable("${status_code}", response.status_code)