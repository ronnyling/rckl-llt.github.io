import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod

CLAIM_POINT_URL = PROTOCOL + "claim" + APP_URL


class ClaimGet(object):

    @keyword("user retrieves all claim")
    def user_retrieves_all_claims(self):
        url = "{0}claim".format(CLAIM_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_claims = secrets.choice(range(0, len(body_result)))
            else:
                rand_claims = 0
            BuiltIn().set_test_variable("${rand_claims_selection}", body_result[rand_claims]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves claim by id')
    def user_retrieves_claim_by_id(self):
        """ Functions to retrieve claim by using id """
        claim_id = BuiltIn().get_variable_value("${claim_id}")
        if claim_id is None:
            self.user_retrieves_all_claims()
            claim_id = BuiltIn().get_variable_value("${rand_claims_selection}")
        url = "{0}claim/{1}".format(CLAIM_POINT_URL, claim_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['CLAIM_HEADER']['CLAIM_ID']
            assert res_bd_id == claim_id, "ID retrieved not matched"
            return body_result
        BuiltIn().set_test_variable("${status_code}", response.status_code)
