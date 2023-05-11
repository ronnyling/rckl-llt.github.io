import secrets

from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class AttributeModuleGet(object):
    ATT_ID = "${att_module_id}"

    @keyword('user retrieves ${condition} attribute module')
    def user_retrieves_attribute_module_data(self, condition):
        attribute_module_id = BuiltIn().get_variable_value("${attribute_module_id}")
        if condition == 'created':
            url = "{0}module-data/module/{1}".format(END_POINT_URL, attribute_module_id)
        else:
            url = "{0}module-data/module".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response

    def user_retrieves_attribute_module_by_name(self, name):
        att_filter = {"MODULE": {"$eq": name}}
        att_filter = json.dumps(att_filter)
        url = "{0}module-data/module?filter={1}".format(END_POINT_URL, att_filter)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve attribute module"
        body_result = response.json()
        att_module_id = body_result[0]['ID']
        BuiltIn().set_test_variable(self.ATT_ID, att_module_id)
        return att_module_id

    def user_retrieves_all_attribute_module(self):
        url = "{0}module-data/module".format(END_POINT_URL)
        print("URL: ", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_so = secrets.randbelow(len(body_result))
            else:
                rand_so = 0
            BuiltIn().set_test_variable(self.ATT_ID, body_result[rand_so]["ID"])
            BuiltIn().set_test_variable("${atr_all}", body_result)
            print("ID:  ", body_result[rand_so]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_attribute_module_by_id(self, type):
        self.user_retrieves_all_attribute_module()
        if type == 'valid':
            res_attribute_selection_id = BuiltIn().get_variable_value(self.ATT_ID)
            print("Valid Id: ", res_attribute_selection_id)
        else:
            res_attribute_selection_id = COMMON_KEY.generate_random_id("0")

        url = "{0}module-data/module/{1}".format(END_POINT_URL, res_attribute_selection_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${att_module_res_body}", response.json())
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
