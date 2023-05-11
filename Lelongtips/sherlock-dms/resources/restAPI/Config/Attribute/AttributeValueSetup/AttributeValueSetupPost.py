import json
import secrets

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI.Config.Attribute.AttributeCreation import AttributeCreationGet
from resources.restAPI.SysConfig.Maintenance.LOB import LobGet
from resources.restAPI.SysConfig.Attribute.AttributeModule import AttributeModuleGet

END_POINT_URL = PROTOCOL + "dynamic-attribute" + APP_URL


class AttributeValueSetupPost(object):
    @keyword('user creates attribute value setup using ${data} data')
    def user_creates_attribute_value_setup(self, data):
        url = "{0}attribute-value-creation".format(END_POINT_URL)

        payload = self.attribute_value_setup_payload(data)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body = response.json()
            BuiltIn().set_test_variable("${res_body}", body)
            print("body", body)
            BuiltIn().set_test_variable("${attribute_value_setup_id}", body['attributeId'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @staticmethod
    def attribute_value_setup_payload(data):
        char_num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        AttributeModuleGet.AttributeModuleGet().user_retrieves_attribute_module_by_id("valid")
        module = BuiltIn().get_variable_value("&{att_module_res_body}")
        module_id = module["ID"]

        def_lob_id = LobGet.LobGet().user_retrieves_lob(True)
        attribute = AttributeCreationGet.AttributeCreationGet().user_gets_attribute_creation_by(module_id, def_lob_id)[0]

        payload = {
            "ATTRIBUTE_CODE": ''.join(secrets.choice(char_num) for _ in range(20)),
            "ATTRIBUTE_VALUE": ''.join(secrets.choice(char_num) for _ in range(20)),
            "DEFAULT_VALUE": "1",
            "MODULE_SELECTION": module,
            "ATTRIBUTE": attribute
        }
        print("Attribute: ", attribute)
        print("Payload Att Value Setup: ", payload)

        if data == 'fix':
            details = BuiltIn().get_variable_value("&{attribute_value_setup_details}")
            payload.update((k, v) for k, v in details.items())
        BuiltIn().set_test_variable("${payload}", payload)
        dump_payload = json.dumps(payload)
        return dump_payload
