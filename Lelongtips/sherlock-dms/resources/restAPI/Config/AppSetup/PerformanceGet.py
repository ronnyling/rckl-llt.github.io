""" Python file related to application setup API """
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL_DAILY_VISIT_TARGET_FORMULA = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-daily-visit-target-formula"
END_POINT_URL_SALES_PERFORMANCE_VALUE = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-sales-performance-value"


class PerformanceGet:
    """ Functions related to application setup - performance GET request """

    def user_retrieves_option_values_daily_visit_target_formula(self, fixed_data):
        """ Functions to retrieve option values for daily visit target formula """
        url = END_POINT_URL_DAILY_VISIT_TARGET_FORMULA
        print("GET url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if dic["VAL_DESC"] == fixed_data:
                    selected_daily_visit_target_formula_id = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_daily_visit_target_formula_id}",
                                        selected_daily_visit_target_formula_id)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_option_values_sales_performance_value(self, fixed_data):
        """ Functions to retrieve option values for sales performance value """
        url = END_POINT_URL_SALES_PERFORMANCE_VALUE
        print("GET url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if dic["VAL_DESC"] == fixed_data:
                    selected_sales_performance_value_id = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_sales_performance_value_id}",
                                        selected_sales_performance_value_id)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
