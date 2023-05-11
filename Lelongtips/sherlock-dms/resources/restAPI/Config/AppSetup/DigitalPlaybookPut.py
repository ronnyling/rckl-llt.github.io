""" Python file related to application setup API """
import json
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Config.AppSetup import AppSetupPut, DigitalPlaybookGet, ReportGet
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "setting" + APP_URL + "module-data/application-setup"


class DigitalPlaybookPut:
    """ Functions related to application setup - digital playbook PUT Request """

    @keyword('user updates app setup digital playbook details using ${data_type} data')
    def user_updates_app_setup_digital_playbook_details_using_data(self, data_type):
        """ Functions to update application setup - digital playbook using given data """
        payload = self.create_payload_app_setup_digital_playbook()
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

    def create_payload_app_setup_digital_playbook(self):
        """ Functions to create payload for application setup - digital playbook """
        body_result = BuiltIn().get_variable_value("${body_result}")
        converted_details = AppSetupPut.AppSetupPut().convert_string_to_int(body_result)
        print("converted_details: ", converted_details)
        details = BuiltIn().get_variable_value("${AppSetupDetails}")
        if details:
            modified_data = self.retrieve_id_for_specific_digital_playbook_field(details)
            converted_details.update((k, v) for k, v in modified_data.items())
        payload = json.dumps(converted_details)
        return payload

    def retrieve_id_for_specific_digital_playbook_field(self, given_data):
        """ Functions to retrieve id for specific field in application setup - digital playbook """
        modified_data = given_data
        if given_data["PLAYBK_MAX_CONTENT_SIZE"]:
            DigitalPlaybookGet.DigitalPlaybookGet().user_retrieves_option_values_playbook_max_content_size(
                given_data["PLAYBK_MAX_CONTENT_SIZE"])
            selected_max_size_id = BuiltIn().get_variable_value("${selected_max_size_id}")
            if selected_max_size_id:
                modified_data["PLAYBK_MAX_CONTENT_SIZE"] = selected_max_size_id
        if given_data["PLAYBK_PROD_HIERARCHY_LEVEL"]:
            ReportGet.ReportGet().user_retrieves_option_values_prod_level(given_data['PLAYBK_PROD_HIERARCHY_LEVEL'])
            selected_prod_level_id = BuiltIn().get_variable_value("${selected_prod_level_id[0]}")
            if selected_prod_level_id:
                modified_data["PLAYBK_PROD_HIERARCHY_LEVEL"] = selected_prod_level_id
        return modified_data
