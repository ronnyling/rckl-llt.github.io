import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "credit-note" + APP_URL


class CreditNoteProductGet(object):

    @keyword('user retrieves all company credit note product')
    def user_retrieves_all_comp_credit_note_product(self):
        url = "{0}supplier-cn-prd-header".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_scnp = secrets.choice(range(0, len(body_result)))
            else:
                rand_scnp = 0
            BuiltIn().set_test_variable("${rand_scnp_selection}", body_result[rand_scnp]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves company credit note product by id')
    def user_retrieves_comp_credit_note_product_by_id(self):
        """ Function to retrieve comp credit note product by id"""
        res_bd_comp_cnp = BuiltIn().get_variable_value("${scnp_id}")
        if res_bd_comp_cnp is None:
            self.user_retrieves_all_comp_credit_note_product()
            res_bd_comp_cnp = BuiltIn().get_variable_value("${rand_scnp_selection}")
        url = "{0}supplier-cn-prd-header/{1}".format(END_POINT_URL, res_bd_comp_cnp)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            assert body_result['PRIME_FLAG'] == 'PRIME' or body_result['PRIME_FLAG'] == 'NON_PRIME', \
                                                        "Prime flag not showing correctly in respond"
            assert body_result['ID'] == res_bd_comp_cnp, "ID retrieved not matched"
            return body_result
        BuiltIn().set_test_variable("${status_code}", response.status_code)