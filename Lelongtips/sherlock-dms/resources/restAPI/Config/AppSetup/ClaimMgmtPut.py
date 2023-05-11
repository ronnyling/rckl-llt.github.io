""" Python file related to application setup API """
import json
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Config.AppSetup import AppSetupGet, AppSetupPut, ClaimMgmtGet
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "setting" + APP_URL + "module-data/application-setup"


class ClaimMgmtPut:
    """ Functions related to application setup - claim management PUT Request """

    @keyword('user updates app setup claim management details using ${data_type} data')
    def user_updates_app_setup_claim_management_details_using_data(self, data_type):
        """ Functions to update application setup - claim management using given data """
        payload = self.create_payload_app_setup_claim_management()
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

    def create_payload_app_setup_claim_management(self):
        """ Functions to create payload for application setup - claim management """
        body_result = BuiltIn().get_variable_value("${body_result}")
        print("body_result", body_result)
        converted_details = AppSetupPut.AppSetupPut().convert_string_to_int(body_result)
        print("converted_details: ", converted_details)
        details = BuiltIn().get_variable_value("${AppSetupDetails}")
        if details:
            modified_data = self.retrieve_id_for_specific_claim_management_field(details)
            print("modified_data", modified_data)
            converted_details.update((k, v) for k, v in modified_data.items())
        payload = json.dumps(converted_details)
        return payload

    def retrieve_id_for_specific_claim_management_field(self, given_data):
        """ Functions to retrieve id for specific field in application setup - claim management """
        modified_data = given_data
        if given_data["CM_AUTO_CLAIM_STAT"]:
            ClaimMgmtGet.ClaimMgmtGet().user_retrieves_option_values_auto_claim_status(
                given_data["CM_AUTO_CLAIM_STAT"])
            selected_auto_claim_stat_id = BuiltIn().get_variable_value(
                "${selected_auto_claim_stat_id}")
            modified_data["CM_AUTO_CLAIM_STAT"] = selected_auto_claim_stat_id
        if given_data["CM_AUTO_PROMO_CLAIM_TYPE"]:
            ClaimMgmtGet.ClaimMgmtGet().user_retrieves_option_values_auto_promo_type(given_data["CM_AUTO_PROMO_CLAIM_TYPE"])
            selected_auto_promo_id = BuiltIn().get_variable_value("${selected_auto_promo_id}")
            modified_data["CM_AUTO_PROMO_CLAIM_TYPE"] = selected_auto_promo_id
        return modified_data
