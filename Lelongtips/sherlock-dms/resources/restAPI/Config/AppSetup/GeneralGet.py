""" Python file related to application setup API """
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod

END_POINT_URL_PROD_GROUP = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-hht-product-grouping"
END_POINT_URL_HHT_LANDING_PG = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-hht-landing-page"
END_POINT_URL_HHT_ORDER_UI_TEMP = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-hht-orderui-template"
END_POINT_URL_HHT_POSM_FILTER = PROTOCOL + "dynamic-attribute" + APP_URL + "dynamic-attribute"


class GeneralGet:
    """ Functions related to application setup -  General GET request """

    def user_retrieves_option_values_prod_group(self, given_data):
        """ Functions to retrieve option values for hht prod grouping """
        url = END_POINT_URL_PROD_GROUP
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if dic["VAL_DESC"] == given_data:
                    selected_prod_group_id = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_prod_group_id}",
                                        selected_prod_group_id)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_option_values_landing_pg(self, given_data):
        """ Functions to retrieve option values for hht landing page """
        url = END_POINT_URL_HHT_LANDING_PG
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if dic["DESC"] == given_data:
                    selected_landing_pg_id = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_landing_pg_id}",
                                        selected_landing_pg_id)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_option_values_orderui_temp(self, given_data):
        """ Functions to retrieve option values for order ui template """
        url = END_POINT_URL_HHT_ORDER_UI_TEMP
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if dic["DESC"] == given_data:
                    selected_order_temp_id = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_order_temp_id}",
                                        selected_order_temp_id)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_option_values_hht_posm_filter(self, given_data):
        """ Functions to retrieve option values for hht posm filter """
        url = END_POINT_URL_HHT_POSM_FILTER
        print("GET url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            print("body result", body_result)
            for dic in body_result:
                print("Dic1", dic)
                if dic["ATTRIBUTE"] == given_data:
                    print('dic["ID"]', dic["ID"])
                    posm_filter_id = (dic["ID"])
                    BuiltIn().set_test_variable("${posm_filter_id}", posm_filter_id)
                    break
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)