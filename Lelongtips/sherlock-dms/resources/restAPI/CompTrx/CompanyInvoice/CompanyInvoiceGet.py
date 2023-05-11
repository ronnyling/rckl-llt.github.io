import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "inventory" + APP_URL


class CompanyInvoiceGet(object):

    @keyword('user retrieves all company invoice')
    def user_retrieves_all_company_invoice(self):
        url = "{0}company-invoice".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_com_inv = secrets.choice(range(0, len(body_result)))
            else:
                rand_com_inv = 0
            BuiltIn().set_test_variable("${rand_com_inv_selection}", body_result[rand_com_inv]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves company invoice by id')
    def user_retrieves_company_invoice_by_id(self):
        """ Functions to retrieve company invoice by using id """
        com_inv_id = BuiltIn().get_variable_value("${inv_id}")
        if com_inv_id is None:
            self.user_retrieves_all_company_invoice()
            com_inv_id = BuiltIn().get_variable_value("${rand_com_inv_selection}")
        url = "{0}company-invoice/{1}".format(END_POINT_URL, com_inv_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            prime_status = body_result['PRIME_FLAG']
            BuiltIn().set_test_variable("${inv_dtls}", body_result)
            assert prime_status == 'PRIME' or prime_status == 'NON_PRIME', "Prime flag not showing correctly in respond"
            assert res_bd_id == com_inv_id, "ID retrieved not matched"
            return body_result
        BuiltIn().set_test_variable("${status_code}", response.status_code)

