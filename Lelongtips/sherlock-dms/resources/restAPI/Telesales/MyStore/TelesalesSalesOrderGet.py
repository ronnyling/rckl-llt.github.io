from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn


END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class TelesalesSalesOrderGet(object):

    def user_retrieves_master_product_hierarchy_list(self):
        details = BuiltIn().get_variable_value("${AppSetupDetails}")
        url = "{0}telesales/transaction/product-category-value".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        body_result = response.json()
        product_hierarchy = body_result['TREE_DESC']
        if details is not None:
            assert product_hierarchy == 'Brand', "INCORRECT PRODUCT HIERARCHY CODE"
        print("Product hierarchy: ", product_hierarchy)
        print("Response is: ", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
