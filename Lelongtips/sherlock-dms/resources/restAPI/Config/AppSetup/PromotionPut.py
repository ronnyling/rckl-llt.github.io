""" Python file related to application setup API """
import json

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Config.AppSetup import AppSetupPut, PromotionGet
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "setting" + APP_URL + "module-data/application-setup"


class PromotionPut:
    """ Functions related to application setup - promotion PUT request """

    @keyword('user updates app setup promotion details using ${data_type} data')
    def user_updates_app_setup_promotion_details_using_data(self, data_type):
        """ Functions to update application setup - promotion using fixed data """
        payload = self.create_payload_app_setup_promotion()
        app_setup_id = BuiltIn().get_variable_value("${app_setup_id}")
        url = "{0}/{1}".format(END_POINT_URL, app_setup_id)
        print("url", url)
        print("payload", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def create_payload_app_setup_promotion(self):
        """ Functions to create payload for application setup - promotion """
        body_result = BuiltIn().get_variable_value("${body_result}")
        print("body_result", body_result)
        converted_details = AppSetupPut.AppSetupPut().convert_string_to_int(body_result)
        print("converted_details: ", converted_details)
        details = BuiltIn().get_variable_value("${AppSetupDetails}")
        if details:
            modified_data = self.retrieve_id_for_specific_promotion_field(details)
            print("modified_data", modified_data)
            converted_details.update((k, v) for k, v in modified_data.items())
        payload = json.dumps(converted_details)
        return payload

    def retrieve_id_for_specific_promotion_field(self, fixed_data):
        """ Functions to retrieve id for specific field in application setup - promotion """
        modified_data = fixed_data
        if fixed_data.get("QPS_ELG_BASED_ON"):
            PromotionGet.PromotionGet().user_retrieves_option_values_qps_eligibility_based_on(
                fixed_data["QPS_ELG_BASED_ON"])
            selected_qps_eligibility_based_on_id = BuiltIn().get_variable_value(
                "${selected_qps_eligibility_based_on_id}")
            modified_data["QPS_ELG_BASED_ON"] = selected_qps_eligibility_based_on_id
        if fixed_data.get("QPS_OPN_INV_CHK"):
            PromotionGet.PromotionGet().user_retrieves_option_values_qps_open_inv_check(fixed_data["QPS_OPN_INV_CHK"])
            selected_qps_open_inv_check_id = BuiltIn().get_variable_value("${selected_qps_open_inv_check_id}")
            modified_data["QPS_OPN_INV_CHK"] = selected_qps_open_inv_check_id
        if fixed_data.get("APPLY_PROMOTION_BASED_ON"):
            PromotionGet.PromotionGet().user_retrieves_option_values_apply_promotion_based_on(
                fixed_data["APPLY_PROMOTION_BASED_ON"])
            selected_apply_promotion_based_on_id = BuiltIn().get_variable_value(
                "${selected_apply_promotion_based_on_id}")
            modified_data["APPLY_PROMOTION_BASED_ON"] = selected_apply_promotion_based_on_id
        return modified_data
