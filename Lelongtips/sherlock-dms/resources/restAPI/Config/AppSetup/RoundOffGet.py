""" Python file related to application setup API """
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.Common import Common

END_POINT_URL_INV_ADJ_MTD = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-invoice-adjustment-method"
END_POINT_URL_ROUND_OFF_DECIMAL = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-round-off-decimal"
END_POINT_URL_ROUND_OFF_VALUE = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-round-off-value"
END_POINT_URL_ROUND_OFF_TO_THE = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-round-off-to-the"
END_POINT_URL_ROUND_OFF_DECIMAL_DISPLAY = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-round-off-decimal-display"


class RoundOffGet:
    """ Functions related to application setup - round off GET request """

    def user_retrieves_option_values_invoice_adjustment_method(self, fixed_data):
        """ Functions to retrieve option values for invoice adjustment method """
        url = END_POINT_URL_INV_ADJ_MTD
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if dic["VAL_DESC"] == fixed_data:
                    selected_invoice_adjustment_method_id = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_invoice_adjustment_method_id}",
                                        selected_invoice_adjustment_method_id)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    def user_retrieves_option_values_round_off_decimal(self, fixed_data):
        """ Functions to retrieve option values for round off decimal """
        url = END_POINT_URL_ROUND_OFF_DECIMAL
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if str(dic["ROUND_OFF_DECIMAL"]) == str(fixed_data):
                    selected_round_off_decimal_id = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_round_off_decimal_id}", selected_round_off_decimal_id)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    def user_retrieves_option_values_round_off_value(self, fixed_data):
        """ Functions to retrieve option values for round off value """
        url = END_POINT_URL_ROUND_OFF_VALUE
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        selected_round_off_decimal_display_id = BuiltIn().get_variable_value("${selected_round_off_decimal_display_id}")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if str(dic["ROUND_OFF_VALUE"]) == str(fixed_data):
                    print('dic["ROUND_OFF_DECIMAL_DISPLAY"]', str(dic["ROUND_OFF_DECIMAL_DISPLAY"]))
                    print('selected_round_off_decimal_display_id', str(selected_round_off_decimal_display_id))
                    if str(dic["ROUND_OFF_DECIMAL_DISPLAY"]) == str(selected_round_off_decimal_display_id):
                        print('dic', dic)
                        selected_round_off_value_id = dic["ID"]
                        break
            BuiltIn().set_test_variable("${selected_round_off_value_id}", selected_round_off_value_id)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    def user_retrieves_option_values_round_off_to_the(self, fixed_data):
        """ Functions to retrieve option values for round off to the value """
        url = END_POINT_URL_ROUND_OFF_TO_THE
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if str(dic["VAL_CODE"]) == str(fixed_data).upper():
                    selected_round_off_to_the_id = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_round_off_to_the_id}", selected_round_off_to_the_id)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    def user_retrieves_option_values_round_off_decimal_display(self, fixed_data):
        """ Functions to retrieve option values for round off decimal display """
        url = END_POINT_URL_ROUND_OFF_DECIMAL_DISPLAY
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if str(dic["ROUND_OFF_DECIMAL_DISPLAY"]) == str(fixed_data):
                    selected_round_off_decimal_display_id = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_round_off_decimal_display_id}", selected_round_off_decimal_display_id)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)
