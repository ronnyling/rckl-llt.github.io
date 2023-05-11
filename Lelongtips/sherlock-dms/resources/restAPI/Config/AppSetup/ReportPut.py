""" Python file related to application setup API """
import json
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Config.AppSetup import AppSetupPut, ReportGet
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "setting" + APP_URL + "module-data/application-setup"


class ReportPut:
    """ Functions related to application setup - report PUT request """

    @keyword('user updates app setup report details using ${data_type} data')
    def user_updates_app_setup_report_details_using_data(self, data_type):
        """ Functions to update application setup - report using given data """
        payload = self.create_payload_app_setup_report()
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

    def create_payload_app_setup_report(self):
        """ Functions to create payload for application setup - report """
        body_result = BuiltIn().get_variable_value("${body_result}")
        converted_details = AppSetupPut.AppSetupPut().convert_string_to_int(body_result)
        details = BuiltIn().get_variable_value("${AppSetupDetails}")
        if details:
            modified_data = self.retrieve_id_for_specific_report_field(details)
            print("modified_data", modified_data)
            converted_details.update((k, v) for k, v in modified_data.items())
        payload = json.dumps(converted_details)
        return payload

    def retrieve_id_for_specific_report_field(self, given_data):
        """ Functions to retrieve id for specific field in application setup - report """
        modified_data = given_data
        if given_data["RPT_REGION_LEVEL"]:
            ReportGet.ReportGet().user_retrieves_option_values_geo_level_region(
                given_data["RPT_REGION_LEVEL"])
            geo_level_rpt_region_id = BuiltIn().get_variable_value(
                "${geo_level_region_id}")
            modified_data["RPT_REGION_LEVEL"] = geo_level_rpt_region_id
        if given_data["RPT_SEGMENTATION"]:
            ReportGet.ReportGet().user_retrieves_option_values_segment(given_data["RPT_SEGMENTATION"])
            segment_id = BuiltIn().get_variable_value("${segment_id}")
            modified_data["RPT_SEGMENTATION"] = segment_id
        if given_data["RPT_PROD_LEVEL"]:
            ReportGet.ReportGet().user_retrieves_option_values_prod_level(given_data["RPT_PROD_LEVEL"])
            selected_prod_level_id = BuiltIn().get_variable_value("${selected_prod_level_id}")
            modified_data["RPT_PROD_LEVEL"] = selected_prod_level_id
        if given_data["RPT_BRAND_LEVEL"]:
            ReportGet.ReportGet().user_retrieves_option_values_prod_level(given_data["RPT_BRAND_LEVEL"])
            selected_brand_level_id = BuiltIn().get_variable_value("${selected_prod_level_id}")
            modified_data["RPT_BRAND_LEVEL"] = selected_brand_level_id
        if given_data["RPT_CHANNEL_LEVEL"]:
            ReportGet.ReportGet().user_retrieves_option_values_channel_level(given_data["RPT_CHANNEL_LEVEL"])
            selected_channel_level_id = BuiltIn().get_variable_value("${selected_channel_level_id}")
            modified_data["RPT_CHANNEL_LEVEL"] = selected_channel_level_id
        if given_data["RPT_OUTLET_TYPE"]:
            ReportGet.ReportGet().user_retrieves_option_values_channel_level(given_data["RPT_OUTLET_TYPE"])
            selected_channel_level_id = BuiltIn().get_variable_value("${selected_channel_level_id}")
            modified_data["RPT_OUTLET_TYPE"] = selected_channel_level_id
        return modified_data
