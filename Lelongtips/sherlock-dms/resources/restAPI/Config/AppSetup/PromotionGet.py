""" Python file related to application setup API """
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.Common import Common

END_POINT_URL_QPS_ELIGIBILITY_BASED_ON = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-qps-elg-based-on"
END_POINT_URL_QPS_OPEN_INV_CHECK = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-qps-open-inv-check"
END_POINT_URL_APPLY_PROMOTION_BASED_ON = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-apply-promotion-based-on"


class PromotionGet:
    """ Functions related to application setup - promotion GET request """

    def user_retrieves_option_values_qps_eligibility_based_on(self, fixed_data):
        """ Functions to retrieve option values for qps eligibility based on """
        url = END_POINT_URL_QPS_ELIGIBILITY_BASED_ON
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if dic["VAL_DESC"] == fixed_data:
                    selected_qps_eligibility_based_on_id = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_qps_eligibility_based_on_id}",
                                        selected_qps_eligibility_based_on_id)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    def user_retrieves_option_values_qps_open_inv_check(self, fixed_data):
        """ Functions to retrieve option values for qps open invoice check """
        url = END_POINT_URL_QPS_OPEN_INV_CHECK
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if dic["VAL_DESC"] == fixed_data:
                    selected_qps_open_inv_check_id = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_qps_open_inv_check_id}",
                                        selected_qps_open_inv_check_id)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    def user_retrieves_option_values_apply_promotion_based_on(self, fixed_data):
        """ Functions to retrieve option values for apply promotion based on """
        url = END_POINT_URL_APPLY_PROMOTION_BASED_ON
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if dic["VAL_DESC"] == fixed_data:
                    selected_apply_promotion_based_on_id = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_apply_promotion_based_on_id}",
                                        selected_apply_promotion_based_on_id)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)
