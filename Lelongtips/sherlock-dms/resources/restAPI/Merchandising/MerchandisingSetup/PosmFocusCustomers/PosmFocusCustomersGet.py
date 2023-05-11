from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "posm-management" + APP_URL
MTDT_END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class PosmFocusCustomersGet(object):

    @keyword('user retrieves posm focus customers')
    def user_retrieves_posm_focus_customers(self):
        url = "{0}posm-focused-customers-assignment".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${posm_cust_all}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_posm_focus_customers_by_id(self, node_id):
        url = "{0}posm-focused-customers-assignment/{1}".format(END_POINT_URL, node_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${posm_cust_details}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieve_attribute_value_creation(self):
        url = "{0}module-data/attribute-value-creation".format(MTDT_END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${attr_val_ls}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieve_dynamic_attribute(self):
        url = "{0}module-data/dynamic-attribute".format(MTDT_END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${dyn_attr_ls}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)