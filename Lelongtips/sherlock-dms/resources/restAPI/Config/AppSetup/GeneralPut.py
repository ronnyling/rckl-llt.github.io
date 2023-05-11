""" Python file related to application setup API """
import json
import datetime
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Config.AppSetup import AppSetupPut, GeneralGet, ReportGet
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "setting" + APP_URL + "module-data/application-setup"


class GeneralPut:
    """ Functions related to application setup - general PUT request """
    PRD_LVL_ID = "${selected_prod_level_id}"

    @keyword('user updates app setup general details using ${data_type} data')
    def user_updates_app_setup_general_details_using_data(self, data_type):
        """ Functions to update application setup - general using given data """
        payload = self.create_payload_app_setup_general()
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

    def create_payload_app_setup_general(self):
        """ Functions to create payload for application setup - general """
        body_result = BuiltIn().get_variable_value("${body_result}")
        print("body_result", body_result)
        converted_details = AppSetupPut.AppSetupPut().convert_string_to_int(body_result)
        print("converted_details: ", converted_details)
        details = BuiltIn().get_variable_value("${AppSetupDetails}")
        if details:
            modified_data = self.retrieve_id_for_specific_general_field(details)
            print("modified_data", modified_data)
            converted_details.update((k, v) for k, v in modified_data.items())
        payload = json.dumps(converted_details)
        return payload

    def retrieve_id_for_specific_general_field(self, given_data):
        """ Functions to retrieve id for specific field in application setup - general """
        modified_data = given_data
        if given_data.get("PROD_HIERARCHY_FOR_DISPLAY"):
            ReportGet.ReportGet().user_retrieves_option_values_prod_level(given_data["PROD_HIERARCHY_FOR_DISPLAY"])
            selected_prod_display_level_id = BuiltIn().get_variable_value(self.PRD_LVL_ID)
            modified_data["PROD_HIERARCHY_FOR_DISPLAY"] = selected_prod_display_level_id

        if given_data.get("CUST_HIERARCHY_FOR_DISPLAY"):
            ReportGet.ReportGet().user_retrieves_option_values_channel_level(given_data["CUST_HIERARCHY_FOR_DISPLAY"])
            selected_channel_display_level_id = BuiltIn().get_variable_value("${selected_channel_level_id}")
            modified_data["CUST_HIERARCHY_FOR_DISPLAY"] = selected_channel_display_level_id

        if given_data.get("HHT_PROD_GROUPING_BASED_ON"):
            GeneralGet.GeneralGet().user_retrieves_option_values_prod_group(
                given_data["HHT_PROD_GROUPING_BASED_ON"])
            selected_prod_group_id = BuiltIn().get_variable_value(
                "${selected_prod_group_id}")
            modified_data["HHT_PROD_GROUPING_BASED_ON"] = selected_prod_group_id

        if given_data.get("HHT_ORDER_UI_TEMPLATE"):
            GeneralGet.GeneralGet().user_retrieves_option_values_orderui_temp(
                given_data["HHT_ORDER_UI_TEMPLATE"])
            selected_order_tem_id = BuiltIn().get_variable_value(
                "${selected_order_temp_id}")
            modified_data["HHT_ORDER_UI_TEMPLATE"] = selected_order_tem_id

        if given_data.get("HHT_LANDING_PAGE"):
            GeneralGet.GeneralGet().user_retrieves_option_values_landing_pg(
                given_data["HHT_LANDING_PAGE"])
            selected_landing_pg_id = BuiltIn().get_variable_value(
                "${selected_landing_pg_id}")
            modified_data["HHT_LANDING_PAGE"] = selected_landing_pg_id

        if given_data.get("HHT_POSM_FILTER_BY"):
            GeneralGet.GeneralGet().user_retrieves_option_values_hht_posm_filter(
                given_data["HHT_POSM_FILTER_BY"])
            selected_posm_filter_id = BuiltIn().get_variable_value(
                "${posm_filter_id}")
            modified_data["HHT_POSM_FILTER_BY"] = selected_posm_filter_id

        if given_data.get("EFFECTIVE_DATE") == "rand":
            start_dt = datetime.datetime.today() + datetime.timedelta(days=1)
            modified_data["EFFECTIVE_DATE"] = start_dt.strftime("%Y-%m-%d")

        if given_data.get("HHT_SIGN_CONTR_SCR"):
            value = [given_data["HHT_SIGN_CONTR_SCR"]]
            modified_data["HHT_SIGN_CONTR_SCR"] = value

        if given_data.get("HHT_PROD_HIERARCHY_FOR_DISPLAY") == "all":
            ReportGet.ReportGet().user_retrieves_option_values_prod_level("Category")
            selected_prod_display_level_id2 = BuiltIn().get_variable_value(self.PRD_LVL_ID)
            ReportGet.ReportGet().user_retrieves_option_values_prod_level("Brand")
            selected_prod_display_level_id3 = BuiltIn().get_variable_value(self.PRD_LVL_ID)
            ReportGet.ReportGet().user_retrieves_option_values_prod_level("Variant")
            selected_prod_display_level_id4 = BuiltIn().get_variable_value(self.PRD_LVL_ID)
            value2 = [selected_prod_display_level_id2[0], selected_prod_display_level_id3[0],
                      selected_prod_display_level_id4[0]]
            print("Value2-->", value2)
            modified_data["HHT_PROD_HIERARCHY_FOR_DISPLAY"] = value2
        return modified_data
