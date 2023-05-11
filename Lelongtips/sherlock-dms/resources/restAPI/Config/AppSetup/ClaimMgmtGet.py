""" Python file related to application setup API """
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL_AUTO_PROMO_TYPE = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-auto-promo-claim-type"
END_POINT_URL_AUTO_CLAIM_STAT = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-auto-claim-status"


class ClaimMgmtGet:
    """ Functions related to application setup - claim management GET Request """

    def user_retrieves_option_values_auto_promo_type(self, given_data):
        """ Functions to retrieve option values for auto promo type """
        url = END_POINT_URL_AUTO_PROMO_TYPE
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if dic["VAL_DESC"] == given_data:
                    selected_auto_promo_id = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_auto_promo_id}",
                                        selected_auto_promo_id)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_option_values_auto_claim_status(self, given_data):
        """ Functions to retrieve option values for auto claim status """
        url = END_POINT_URL_AUTO_CLAIM_STAT
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if dic["VAL_DESC"] == given_data:
                    selected_auto_claim_stat_id = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_auto_claim_stat_id}",
                                        selected_auto_claim_stat_id)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
