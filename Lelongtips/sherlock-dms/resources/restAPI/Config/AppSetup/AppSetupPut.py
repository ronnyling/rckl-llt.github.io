""" Python file related to application setup API """
import json

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Config.AppSetup import ReportGet
from resources.restAPI.Common import APIMethod
import numpy as np

END_POINT_URL = PROTOCOL + "setting" + APP_URL + "module-data/application-setup"


class AppSetupPut:
    """ Functions related to application setup PUT request """

    @keyword('user updates app setup details using ${data_type} data')
    def user_updates_app_setup_details_using_data(self, data_type):
        """ Functions to update application setup using fixed data """
        payload = self.create_payload_app_setup(data_type)
        app_setup_id = BuiltIn().get_variable_value("${app_setup_id}")
        url = "{0}/{1}".format(END_POINT_URL, app_setup_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            result = response.json()
            print("Result:", result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_revert_to_previous_setting(self):
        read_dictionary = np.load('appsetup.npy', allow_pickle='TRUE').item()
        BuiltIn().set_test_variable("${body_result}", read_dictionary)
        BuiltIn().set_test_variable("${AppSetupDetails}", None)
        self.user_updates_app_setup_details_using_data("fixed")

    def create_payload_app_setup(self, data_type):
        """ Functions to create payload for application setup """
        body_result = BuiltIn().get_variable_value("${body_result}")
        converted_details = self.convert_string_to_int(body_result)
        print("converted_details: ", converted_details)
        details = BuiltIn().get_variable_value("${AppSetupDetails}")
        if details is not None:
            converted_details.update((k, v) for k, v in details.items())

            if data_type == "multi_on":
                converted_details['ENABLE_MULTI_PRINCIPAL'] = True
            elif data_type == "multi_off":
                converted_details['ENABLE_MULTI_PRINCIPAL'] = False

            if 'MDSE_PROD_HIERARCHY_LEVEL' in details.keys():
                ReportGet.ReportGet().user_retrieves_option_values_prod_level(details['MDSE_PROD_HIERARCHY_LEVEL'])
                if BuiltIn().get_variable_value("${selected_prod_level_id}"):
                    converted_details['MDSE_PROD_HIERARCHY_LEVEL'] = \
                                                    BuiltIn().get_variable_value("${selected_prod_level_id[0]}")
                else:
                    converted_details['MDSE_PROD_HIERARCHY_LEVEL'] = details['MDSE_PROD_HIERARCHY_LEVEL']
        payload = json.dumps(converted_details)
        return payload

    def convert_string_to_int(self, payload):
        """ Functions to convert string into integer format """
        for key, value in payload.items():
            print(key, '->', value)
            try:
                flag = isinstance(value, (dict, list))
                if flag is False and value is not None and value is not True and value is not False:
                    payload[key] = int(value)
                else:
                    flag = isinstance(value, (dict, list))
                    if flag is False and value is not None and value is not True and value is not False:
                        payload[key] = int(value)
            except Exception as e:
                print(e.__class__, "occured")
                print("Conversion failed!")

        return payload
