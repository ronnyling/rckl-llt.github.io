from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Customer.CustomerGet import CustomerGet

END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class OutletNoteGet(object):
    @keyword('user retrieves outlet note for ${customer_name}')
    def user_retrieves_outlet_note_for(self, customer_name):
        customer_id = CustomerGet().user_retrieves_cust_name(customer_name)['ID']
        url = "{0}outletnote/{1}".format(END_POINT_URL, customer_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve outlet note"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        print("Outlet note with customer name {0}: ".format(customer_name), body_result)


