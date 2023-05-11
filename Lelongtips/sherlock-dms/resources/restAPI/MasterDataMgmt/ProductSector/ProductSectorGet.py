from resources.restAPI import PROTOCOL, APP_URL, BuiltIn
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "product-sector" + APP_URL


class ProductSectorGet:

    @keyword('user retrieve ${cond} product sector')
    def user_retrieve_product_sector(self, cond):
        if cond == 'created':
            ps_id = BuiltIn().get_variable_value("${product_sector_id}")
            url = "{0}product-sector/{1}".format(END_POINT_URL, ps_id)
        else:
            url = "{0}product-sector/".format(END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        print("Get Status code for product sector info is " + str(response.status_code))
        if response.status_code != 200:
            print(response.text)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body_result = response.json()
        print("body result = ", body_result)
        BuiltIn().set_test_variable("${ps_br}", body_result)

    def user_retrieve_hq_product_for_dist(self):
        url = "{0}all-hq-products-dist".format(END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        if response.status_code == 200:
            BuiltIn().set_test_variable("${hq_prd_for_dist_ls}", response.json())
            BuiltIn().set_test_variable("${retrieve_success}", "YES")
            body_result = response.json()
            # print("body result = ", body_result)
            BuiltIn().set_test_variable("${ps_br}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

