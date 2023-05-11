""" Python file related to application setup API """
import json
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Config.AppSetup import AppSetupPut, PricingGet
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "setting" + APP_URL + "module-data/application-setup"


class PricingPut:
    """ Functions related to application setup - pricing PUT request """

    @keyword('user updates app setup pricing details using ${data_type} data')
    def user_updates_app_setup_pricing_details_using_data(self, data_type):
        """ Functions to update application setup - pricing using fixed data """
        payload = self.create_payload_app_setup_pricing()
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

    def create_payload_app_setup_pricing(self):
        """ Functions to create payload for application setup - pricing """
        body_result = BuiltIn().get_variable_value("${body_result}")
        converted_details = AppSetupPut.AppSetupPut().convert_string_to_int(body_result)
        details = BuiltIn().get_variable_value("${AppSetupDetails}")
        if details:
            modified_data = self.retrieve_id_for_specific_pricing_field(details)
            print("modified_data", modified_data)
            converted_details.update((k, v) for k, v in modified_data.items())
        payload = json.dumps(converted_details)
        return payload

    def retrieve_id_for_specific_pricing_field(self, fixed_data):
        """ Functions to retrieve id for specific field in application setup - pricing """
        modified_data = fixed_data
        if fixed_data["NO_OF_MARGIN_INPUT"]:
            PricingGet.PricingGet().user_retrieves_option_values_no_of_margin_input(fixed_data["NO_OF_MARGIN_INPUT"])
            selected_no_of_margin_input = BuiltIn().get_variable_value("${selected_no_of_margin_input}")
            modified_data["NO_OF_MARGIN_INPUT"] = selected_no_of_margin_input
        return modified_data
