""" Python file related to application setup API """
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL_NO_OF_MARGIN_INPUT = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-no-of-margin-input"


class PricingGet:
    """ Functions related to application setup - pricing GET request """

    def user_retrieves_option_values_no_of_margin_input(self, fixed_data):
        """ Functions to retrieve option values for no of margin input """
        url = END_POINT_URL_NO_OF_MARGIN_INPUT
        print("GET url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                print("dic", dic)
                if str(dic["NO_OF_MARGIN_INPUT"]) == str(fixed_data):
                    selected_no_of_margin_input = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_no_of_margin_input}", selected_no_of_margin_input)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
