from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class InboundCustomerGet(object):
    @keyword('user retrieves inbound customer listing')
    def user_retrieves_inbound_customer_listing(self):
        url = "{0}inbound-customers-for-telesales".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve inbound customer listing"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        print("Inbound customer for telesales user: ", body_result)



