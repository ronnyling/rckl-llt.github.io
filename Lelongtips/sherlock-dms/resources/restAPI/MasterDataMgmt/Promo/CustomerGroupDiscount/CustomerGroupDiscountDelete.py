from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "promotion" + APP_URL

class CustomerGroupDiscountDelete(object):


    def user_deletes_customer_group_discount(self):
        group_disc_id = BuiltIn().get_variable_value("${res_bd_grpdisc_id}")
        url = "{0}cust-group-discount/{1}".format(END_POINT_URL, group_disc_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        if response.status_code == 201:
            body_result = response.json()
            print("PUT Body Result: ", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)