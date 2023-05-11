import secrets

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "debit-note-sup" + APP_URL


class DebitNoteProductGet(object):

    @keyword('user retrieves all company debit note product')
    def user_retrieves_all_comp_debit_note_product(self):
        url = "{0}supplier-dn-prd-header".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_sdnp = secrets.choice(range(0, len(body_result)))
            else:
                rand_sdnp = 0
            BuiltIn().set_test_variable("${rand_sdnp_selection}", body_result[rand_sdnp]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves company debit note product by id')
    def user_retrieves_comp_debit_note_product_by_id(self):
        """ Function to retrieve comp credit note product by id"""
        res_bd_comp_dnp = BuiltIn().get_variable_value("${sdnp_id}")
        if res_bd_comp_dnp is None:
            self.user_retrieves_all_comp_debit_note_product()
            res_bd_comp_dnp = BuiltIn().get_variable_value("${rand_sdnp_selection}")
        url = "{0}supplier-dn-prd-header/{1}".format(END_POINT_URL, res_bd_comp_dnp)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            assert body_result['PRIME_FLAG'] == 'PRIME' or body_result['PRIME_FLAG'] == 'NON_PRIME', \
                                                        "Prime flag not showing correctly in respond"
            assert body_result['ID'] == res_bd_comp_dnp, "ID retrieved not matched"
            return body_result
        BuiltIn().set_test_variable("${status_code}", response.status_code)

