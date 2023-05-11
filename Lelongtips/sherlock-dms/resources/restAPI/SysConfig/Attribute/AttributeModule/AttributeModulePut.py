import json
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class AttributeModulePut(object):

    @keyword('user update created attribute module')
    def user_update_attribute_module_data(self):
        attribute_module_id = BuiltIn().get_variable_value("${attribute_module_id}")
        url = "{0}module-data/module/{1}".format(END_POINT_URL, attribute_module_id)
        payload = self.attribute_module_payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print("response", response)
        if response.status_code == 200:
            body = response.json()
            BuiltIn().set_test_variable("${attribute_module_id}", body['ID'])
            BuiltIn().set_test_variable("${body_result_attrModule}", body)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print("payload", payload)

    def attribute_module_payload(self):
        aging_module_code = BuiltIn().get_variable_value("${attribute_module_Code}")
        payload = {
            'MODULE_CD': aging_module_code,
            'MODULE': None
        }
        print("payload before: ", payload)
        details = BuiltIn().get_variable_value("&{amdetails_put}")
        print(details)
        if details:
            payload.update((k, v) for k, v in details.items())
        print("Payload after: ", payload)
        payload = json.dumps(payload)
        return payload
