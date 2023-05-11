from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY


CUST_END_POINT_URL = PROTOCOL + "profile-cust" + APP_URL
METADATA_END_POINT_URL = PROTOCOL + "metadata" + APP_URL

class CustomerDelete(object):
    DISTRIBUTOR_ID = "${distributor_id}"
    CUSTOMER_ID = "${cust_id}"

    @keyword("user deletes created customer data")
    def user_deletes_created_customer_data(self):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        cust_id = BuiltIn().get_variable_value("${res_bd_cust_id}")
        url = "{0}distributors/{1}/customer/{2}".format(CUST_END_POINT_URL, dist_id, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("Delete", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_all_custs(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        url = "{0}distributors/{1}/customer".format(CUST_END_POINT_URL, dist_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        body_result = response.json()
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return body_result

    @keyword("user deletes created customer invoice term")
    def user_deletes_customer_invoice_term(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        invoice_term_id = BuiltIn().get_variable_value("${invoice_term_id}")
        url = "{0}distributors/{1}/customer/{2}/customer-invoice-terms/{3}".format(CUST_END_POINT_URL,
                                                                                   dist_id, cust_id, invoice_term_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code
