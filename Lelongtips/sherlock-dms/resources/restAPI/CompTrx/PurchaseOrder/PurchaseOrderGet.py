import secrets

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "purchase-order" + APP_URL


class PurchaseOrderGet(object):

    @keyword('user retrieves all purchase order')
    def user_retrieves_all_purchase_order(self):
        url = "{0}purchase-order".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_po = secrets.randbelow(len(body_result))
            else:
                rand_po = 0
            BuiltIn().set_test_variable("${po_id}", body_result[rand_po]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves purchase order by id')
    def user_retrieves_purchase_order_by_id(self):
        po_id = BuiltIn().get_variable_value("${po_id}")
        url = "{0}purchase-order/{1}".format(END_POINT_URL, po_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            return body_result
            #BuiltIn().set_test_variable("${res_bd_po}")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)