""" Python file related to application setup API """
import json

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Config.AppSetup import AppSetupPut, RoundOffGet
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "setting" + APP_URL + "module-data/application-setup"


class RoundOffPut:
    """ Functions related to application setup - round off PUT request """

    @keyword('user updates app setup round off details using ${data_type} data')
    def user_updates_app_setup_round_off_details_using_data(self, data_type):
        """ Functions to update application setup - round off using fixed data """
        payload = self.create_payload_app_setup_round_off()
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

    def create_payload_app_setup_round_off(self):
        """ Functions to create payload for application setup - round off """
        body_result = BuiltIn().get_variable_value("${body_result}")
        print("body_result", body_result)
        converted_details = AppSetupPut.AppSetupPut().convert_string_to_int(body_result)
        print("converted_details: ", converted_details)
        details = BuiltIn().get_variable_value("${AppSetupDetails}")
        if details:
            modified_data = self.retrieve_id_for_specific_round_off_field(details)
            print("modified_data", modified_data)
            converted_details.update((k, v) for k, v in modified_data.items())
        payload = json.dumps(converted_details)
        return payload

    def retrieve_id_for_specific_round_off_field(self, fixed_data):
        """ Functions to retrieve id for specific field in application setup - round off """
        modified_data = fixed_data
        if fixed_data["INVOICE_ADJUSTMENT_METHOD"]:
            RoundOffGet.RoundOffGet().user_retrieves_option_values_invoice_adjustment_method(fixed_data["INVOICE_ADJUSTMENT_METHOD"])
            selected_invoice_adjustment_method_id = BuiltIn().get_variable_value("${selected_invoice_adjustment_method_id}")
            modified_data["INVOICE_ADJUSTMENT_METHOD"] = selected_invoice_adjustment_method_id
        if fixed_data["ROUND_OFF_DECIMAL"]:
            RoundOffGet.RoundOffGet().user_retrieves_option_values_round_off_decimal(fixed_data["ROUND_OFF_DECIMAL"])
            selected_round_off_decimal_id = BuiltIn().get_variable_value("${selected_round_off_decimal_id}")
            modified_data["ROUND_OFF_DECIMAL"] = selected_round_off_decimal_id
        if fixed_data["ROUND_OFF_DECIMAL_DISPLAY"]:
            RoundOffGet.RoundOffGet().user_retrieves_option_values_round_off_decimal_display(fixed_data["ROUND_OFF_DECIMAL_DISPLAY"])
            selected_round_off_decimal_display_id = BuiltIn().get_variable_value("${selected_round_off_decimal_display_id}")
            modified_data["ROUND_OFF_DECIMAL_DISPLAY"] = selected_round_off_decimal_display_id
        if fixed_data["ROUND_OFF_VALUE"]:
            RoundOffGet.RoundOffGet().user_retrieves_option_values_round_off_value(fixed_data["ROUND_OFF_VALUE"])
            selected_round_off_value_id = BuiltIn().get_variable_value("${selected_round_off_value_id}")
            modified_data["ROUND_OFF_VALUE"] = selected_round_off_value_id
        if fixed_data["ROUND_OFF_TO_THE"]:
            RoundOffGet.RoundOffGet().user_retrieves_option_values_round_off_to_the(fixed_data["ROUND_OFF_TO_THE"])
            selected_round_off_to_the_id = BuiltIn().get_variable_value("${selected_round_off_to_the_id}")
            modified_data["ROUND_OFF_TO_THE"] = selected_round_off_to_the_id
        return modified_data
