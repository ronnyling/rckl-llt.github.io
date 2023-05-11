from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class InvoiceTermGet(object):
    """ Functions to retrieve invoice term records """

    def user_gets_all_invoice_term_data(self):
        """ Function to retrieve all invoice term data """
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/setting-invoice-term".format(END_POINT_URL, dist_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_gets_invoice_term_by_using_id(self):
        """ Function to retrieve invoice term data by using id """
        res_bd_inv_term_id = BuiltIn().get_variable_value("${res_bd_inv_term_id}")
        dist_id = BuiltIn().get_variable_value("${dist_id}")
        url = "{0}distributors/{1}/setting-invoice-term/{2}".format(END_POINT_URL, dist_id, res_bd_inv_term_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_inv_term_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)
