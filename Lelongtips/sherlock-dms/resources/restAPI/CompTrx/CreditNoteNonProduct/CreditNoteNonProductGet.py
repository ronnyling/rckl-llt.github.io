import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "credit-note" + APP_URL


class CreditNoteNonProductGet(object):

    @keyword('user retrieves all company credit note non product')
    def user_retrieves_all_comp_credit_note_non_product(self):
        url = "{0}supplier-cn-np-header".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_scnnp = secrets.choice(range(0, len(body_result)))
            else:
                rand_scnnp = 0
            BuiltIn().set_test_variable("${rand_scnnp_selection}", body_result[rand_scnnp]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves company credit note non product by id')
    def user_retrieves_comp_credit_note_non_product_by_id(self):
        """ Function to retrieve comp credit note non product by id"""
        res_bd_comp_cnnp = BuiltIn().get_variable_value("${scnnp_id}")
        if res_bd_comp_cnnp is None:
            self.user_retrieves_all_comp_credit_note_non_product()
            res_bd_comp_cnnp = BuiltIn().get_variable_value("${rand_scnnp_selection}")
        url = "{0}supplier-cn-np-header/{1}".format(END_POINT_URL, res_bd_comp_cnnp)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            assert body_result['PRIME_FLAG'] == 'PRIME' or body_result['PRIME_FLAG'] == 'NON_PRIME', \
                                                        "Prime flag not showing correctly in respond"
            assert body_result['ID'] == res_bd_comp_cnnp, "ID retrieved not matched"
            return body_result
        BuiltIn().set_test_variable("${status_code}", response.status_code)