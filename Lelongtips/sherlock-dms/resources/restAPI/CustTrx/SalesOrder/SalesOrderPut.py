from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.CustTrx.SalesOrder import SalesOrderPost
from resources.restAPI.Common import APIMethod, TokenAccess
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


END_POINT_URL = PROTOCOL + "salesorder" + APP_URL


class SalesOrderPut(object):
    """ Functions to retrieve sales order transaction """

    @keyword('user updates sales order with ${data_type} data')
    def user_updates_sales_order_with_data(self, data_type):
        """ Function to update sales order transaction """
        url = "{0}salesorder".format(END_POINT_URL)
        BuiltIn().set_test_variable("${action}", "update")
        payload = SalesOrderPost.SalesOrderPost().payload_sales_order()
        payload = SalesOrderPost.SalesOrderPost().so_payload(payload[0], payload[1], payload[2], payload[3])
        print("Payload is {0}".format(payload))
        user = BuiltIn().get_variable_value("${user_role}")
        TokenAccess.TokenAccess().get_token_by_role(user)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
