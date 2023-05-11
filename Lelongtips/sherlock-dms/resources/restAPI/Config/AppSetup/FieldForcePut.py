""" Python file related to application setup API """
import json
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Config.AppSetup import AppSetupPut, ReportGet
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "setting" + APP_URL + "module-data/application-setup"


class FieldForcePut:
    """ Functions related to application setup - Field Force PUT Request """

    @keyword('user updates app setup field force details using ${data_type} data')
    def user_updates_app_setup_field_force_details_using_data(self, data_type):
        """ Functions to update application setup - field force using given data """
        payload = self.create_payload_app_setup_field_force()
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

    @keyword('user updates app setup to ${field} : ${value}')
    def user_updates_app_setup(self, field, value):
        """ Functions to update application setup using given data """
        payload = self.create_app_setup_payload(field, value)
        app_setup_id = BuiltIn().get_variable_value("${app_setup_id}")
        url = "{0}/{1}".format(END_POINT_URL, app_setup_id)
        print("App Setup URL: ", url)
        print("App Setup Payload: ", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def create_app_setup_payload(self, field, value):
        """ Functions to create payload for application setup """
        body_result = BuiltIn().get_variable_value("${body_result}")
        converted_details = AppSetupPut.AppSetupPut().convert_string_to_int(body_result)
        details = {field: value}
        if details:
            converted_details.update((k, v) for k, v in details.items())
        payload = json.dumps(converted_details)
        return payload

    def create_payload_app_setup_field_force(self):
        """ Functions to create payload for application setup - field force """
        body_result = BuiltIn().get_variable_value("${body_result}")
        converted_details = AppSetupPut.AppSetupPut().convert_string_to_int(body_result)
        print("converted_details: ", converted_details)
        details = BuiltIn().get_variable_value("${AppSetupDetails}")
        if 'SO_PROD_FILTER_LEVEL' in details.keys():
            ReportGet.ReportGet().user_retrieves_option_values_prod_level(details['SO_PROD_FILTER_LEVEL'])
            details["SO_PROD_FILTER_LEVEL"] = BuiltIn().get_variable_value("${selected_prod_level_id[0]}")
        if details:
            converted_details.update((k, v) for k, v in details.items())
        payload = json.dumps(converted_details)
        return payload

