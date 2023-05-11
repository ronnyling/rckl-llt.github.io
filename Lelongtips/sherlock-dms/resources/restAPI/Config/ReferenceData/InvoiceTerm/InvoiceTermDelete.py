from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, APIAssertion
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class InvoiceTermDelete(object):
    """ Functions for invoice term deletion """

    def user_deletes_invoice_term_with_created_data(self):
        """ Function to delete invoiceterm with id """
        inv_term_id = BuiltIn().get_variable_value("${res_bd_inv_term_id}")
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/setting-invoice-term/{2}".format(END_POINT_URL, dist_id, inv_term_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_deletes_invoice_term_as_teardown(self):
        self.user_deletes_invoice_term_with_created_data()
        APIAssertion.APIAssertion().expected_return_status_code("200")
