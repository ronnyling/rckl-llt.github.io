""" Python file related to application setup API """
import json

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.AppSetup import AppSetupGet, AppSetupPut

END_POINT_URL = PROTOCOL + "setting" + APP_URL + "module-data/application-setup"


class DeliveryOptimizationPut:
    """ Functions related to application setup - delivery optimization PUT request """

    @keyword('user updates app setup delivery optimization details using ${data_type} data')
    def user_updates_app_setup_delivery_optimization_details_using_data(self, data_type):
        """ Functions to update application setup - delivery optimization using fixed data """
        payload = self.create_payload_app_setup_del_opt()
        app_setup_id = BuiltIn().get_variable_value("${app_setup_id}")
        url = "{0}/{1}".format(END_POINT_URL, app_setup_id)
        print("payload", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def create_payload_app_setup_del_opt(self):
        """ Functions to create payload for application setup - delivery optimization """
        body_result = BuiltIn().get_variable_value("${body_result}")
        converted_details = AppSetupPut.AppSetupPut().convert_string_to_int(body_result)
        details = BuiltIn().get_variable_value("${AppSetupDetails}")
        if details:
            modified_data = self.retrieve_id_for_specific_delivery_optimization_field(details)
            print("modified_data", modified_data)
            converted_details.update((k, v) for k, v in modified_data.items())
        payload = json.dumps(converted_details)
        return payload

    def retrieve_id_for_specific_delivery_optimization_field(self, fixed_data):
        """ Functions to retrieve id for specific field in application setup - delivery optimization """
        modified_data = fixed_data
        try:
            value = [fixed_data["DO_ADD_FIELDS_FOR_DEL_OPT"]]
            modified_data["DO_ADD_FIELDS_FOR_DEL_OPT"] = value
        except Exception as e:
            print(e.__class__, "occured")
            print("Fixed data doesn't consists DO_ADD_FIELDS_FOR_DEL_OPT")
        return modified_data
