import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL

fake = Faker()


END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class OutletNoteGet(object):
    CUSTOMER_ID = "${cust_id}"

    def user_retrieves_all_outlet_note(self):
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        url = "{0}outletnote/{1}".format(END_POINT_URL, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            print(body_result)
        return str(response.status_code), response.json()

    @keyword("user retrieves outlet note by date")
    def user_retrieves_outlet_note(self):
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        details = BuiltIn().get_variable_value("${note_details}")
        date_from = details['dateFrom']
        date_to = details['dateTo']
        url = "{0}outletnote/{1}?dateFrom={2}&dateTo={3}".format(END_POINT_URL, cust_id, date_from, date_to)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code
