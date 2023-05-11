from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

END_POINT_URL = PROTOCOL + "inventory" + APP_URL


class CompanyInvoiceDelete(object):

    def user_deletes_company_invoice(self):
        """Function to delete company invoice"""
        com_inv_id = BuiltIn().get_variable_value("${inv_id}")
        url = "{0}company-invoice/delete".format(END_POINT_URL)
        payload = self.payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, json.dumps(payload))
        print("DELETE Status code for  is " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code != 200:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            print("Body Result:", body_result)
            BuiltIn().set_test_variable("${com_inv_id}", com_inv_id)
            BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload(self):
        com_inv_id = BuiltIn().get_variable_value("${inv_id}")

        payload = [com_inv_id]

        return payload
