import json
from robot.api.deco import keyword
import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class AttributeModulePost(object):

    @keyword('user creates attribute module using ${data_source} data')
    def user_creates_attribute_module(self, data_source):
        url = "{0}module-data/module".format(END_POINT_URL)
        payload = self.attribute_module_payload(data_source)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body = response.json()
        print("payload", payload)
        try:
            print("Result: ", response.json())
            BuiltIn().set_test_variable("${res_body}", response.json())
            BuiltIn().set_test_variable("${attribute_module_id}", body['ID'])
            BuiltIn().set_test_variable("${attribute_module_Code}", body['MODULE_CD'])
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def attribute_module_payload(self, data_source):
        payload = {
            "MODULE_CD": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "MODULE": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
        }

        if data_source == 'given':
            details = BuiltIn().get_variable_value("&{AMdetails}")
            payload.update((k, v) for k, v in details.items())
        BuiltIn().set_test_variable("${payload}", payload)
        payload = json.dumps(payload)
        print("Attribute module: ", payload)
        return payload
