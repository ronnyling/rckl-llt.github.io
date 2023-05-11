from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.ReferenceData.InvoiceTerm.InvoiceTermPost import InvoiceTermPost
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class InvoiceTermPut(object):
    """ Functions to edit invoice term record """

    @keyword('user edits invoice term with ${data_type}')
    def user_edits_invoice_term_with(self, data_type):
        """ Functions to create edit using fixed/random data"""
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        inv_term_id = BuiltIn().get_variable_value("${res_bd_inv_term_id}")
        url = "{0}distributors/{1}/setting-invoice-term/{2}".format(END_POINT_URL, dist_id, inv_term_id)
        payload = InvoiceTermPost().payload_invoice_term()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
