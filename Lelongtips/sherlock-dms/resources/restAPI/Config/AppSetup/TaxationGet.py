""" Python file related to application setup API """
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class TaxationGet:
    """ Functions related to application setup - taxation GET request """

    def user_retrieves_option_values_tax_model(self, fixed_data):
        """ Functions to retrieve option values for tax model """
        url = "{0}module-data/{1}/".format(END_POINT_URL, "opt-val-tax-model")
        print("GET url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if dic["VAL_DESC"] == fixed_data:
                    selected_tax_model_id = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_tax_model_id}", selected_tax_model_id)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_option_values_discount_included(self, discount_type):
        url = "{0}module-data/{1}".format(END_POINT_URL, "opt-val-discounts-to-be-included")

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        count = 0
        flag = False
        if response.status_code == 200:
            body_result = response.json()
            for item in body_result:
                if discount_type == item['VAL_DESC']:
                    flag = True
                    break;
                count = count + 1
        assert flag , "discount to be included not found"
        return body_result[count]
