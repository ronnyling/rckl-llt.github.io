""" Python file related to application setup API """
import json

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Config.AppSetup import AppSetupGet, AppSetupPut, GamificationGet
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "setting" + APP_URL + "module-data/application-setup"


class GamificationPut:
    """ Functions related to application setup - gamification PUT request """

    @keyword('user updates app setup gamification details using ${data_type} data')
    def user_updates_app_setup_gamification_details_using_data(self, data_type):
        """ Functions to update application setup - gamification using fixed data """
        payload = self.create_payload_app_setup_gamification()
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

    def create_payload_app_setup_gamification(self):
        """ Functions to create payload for application setup - gamification """
        body_result = BuiltIn().get_variable_value("${body_result}")
        converted_details = AppSetupPut.AppSetupPut().convert_string_to_int(body_result)
        details = BuiltIn().get_variable_value("${AppSetupDetails}")
        if details:
            modified_data = self.retrieve_id_for_specific_gamification_field(details)
            print("modified_data", modified_data)
            converted_details.update((k, v) for k, v in modified_data.items())
        payload = json.dumps(converted_details)
        return payload

    def retrieve_id_for_specific_gamification_field(self, fixed_data):
        """ Functions to retrieve id for specific field in application setup - gamification """
        modified_data = fixed_data
        if fixed_data["GEO_LEVEL_FOR_LEADERBOARD"]:
            GamificationGet.GamificationGet().user_retrieves_option_values_geo_level_leaderboard(
                fixed_data["GEO_LEVEL_FOR_LEADERBOARD"])
            geo_level_leaderboard_id = BuiltIn().get_variable_value(
                "${geo_level_leaderboard_id}")
            modified_data["GEO_LEVEL_FOR_LEADERBOARD"] = geo_level_leaderboard_id
        return modified_data
