from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL

END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL


class CustomerTransferDelete(object):

    @keyword('user delete created customer transfer')
    def user_deletes_created_customer_trasfer(self):
        transfer_id = BuiltIn().get_variable_value("${transfer_id}")
        url = "{0}customer-transfer/{1}".format(END_POINT_URL, transfer_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        assert response.status_code == 200
        BuiltIn().set_test_variable("${status_code}", response.status_code)
