from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "product" + APP_URL


class ProductUomDelete(object):
    """ Functions to delete product uom """

    @keyword('user deletes created product uom')
    def user_deletes_prd_uom(self):
        prd_id = BuiltIn().get_variable_value("${prd_id}")
        prd_uom_id = BuiltIn().get_variable_value("${prd_uom_id}")
        url = "{0}product/{1}/product-uom/{2}".format(END_POINT_URL, prd_id, prd_uom_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
