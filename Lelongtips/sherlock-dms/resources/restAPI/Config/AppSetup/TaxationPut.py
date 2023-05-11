""" Python file related to application setup API """
import json

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Config.AppSetup import AppSetupPut, TaxationGet
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "setting" + APP_URL + "module-data/application-setup"


class TaxationPut:
    """ Functions related to application setup - taxation PUT request """

    @keyword('user updates app setup taxation details using ${data_type} data')
    def user_updates_app_setup_taxation_details_using_data(self, data_type):
        """ Functions to update application setup - taxation using fixed data """
        payload = self.create_payload_app_setup_taxation()
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

    def create_payload_app_setup_taxation(self):
        """ Functions to create payload for application setup - taxation """
        body_result = BuiltIn().get_variable_value("${body_result}")
        converted_details = AppSetupPut.AppSetupPut().convert_string_to_int(body_result)
        details = BuiltIn().get_variable_value("${AppSetupDetails}")
        if details:
            modified_data = self.retrieve_id_for_specific_taxation_field(details)
            modified_data = self.retrieve_id_for_discount_impact_field(modified_data)
            print("modified_data", modified_data)
            converted_details.update((k, v) for k, v in modified_data.items())
        payload = json.dumps(converted_details)
        return payload

    def retrieve_id_for_specific_taxation_field(self, fixed_data):
        """ Functions to retrieve id for specific field in application setup - taxation """
        modified_data = fixed_data
        if fixed_data.get("TAX_MODEL"):
            TaxationGet.TaxationGet().user_retrieves_option_values_tax_model(fixed_data["TAX_MODEL"])
            selected_tax_model_id = BuiltIn().get_variable_value("${selected_tax_model_id}")
            modified_data["TAX_MODEL"] = selected_tax_model_id
        return modified_data

    def retrieve_id_for_discount_impact_field(self, fixed_data):
        """ Functions to retrieve id for specific field in application setup - discount impact """
        modified_data = fixed_data
        if modified_data.get("DISCOUNTS_TO_BE_INCLUDED_FOR_TAX_COMPUTATION"):
            disc_include = modified_data['DISCOUNTS_TO_BE_INCLUDED_FOR_TAX_COMPUTATION'].split(",")
            disc_include_list = []
            for item in disc_include:
                print("DISC ITEM: ", item)
                data = TaxationGet.TaxationGet().user_retrieves_option_values_discount_included(item)
                disc_include_list.append(data)
            modified_data["DISCOUNTS_TO_BE_INCLUDED_FOR_TAX_COMPUTATION"] = disc_include_list
        return modified_data
