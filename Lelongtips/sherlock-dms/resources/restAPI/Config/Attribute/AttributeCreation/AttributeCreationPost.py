import json
import secrets

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI.SysConfig.Maintenance.LOB import LobGet
from resources.restAPI.SysConfig.Attribute.AttributeModule import AttributeModuleGet

END_POINT_URL = PROTOCOL + "dynamic-attribute" + APP_URL


class AttributeCreationPost(object):
    @keyword('user creates attribute creation using ${data} data')
    def user_creates_attribute_creation(self, data):
        url = "{0}dynamic-attribute".format(END_POINT_URL)

        payload = self.attribute_creation_payload(data)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body = response.json()
        try:
            print("Result: ", response.json())
            BuiltIn().set_test_variable("${res_body}", response.json())
            BuiltIn().set_test_variable("${attribute_creation_id}", body['attributeId'])
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)
        else:
            print("id ", body['attributeId'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @staticmethod
    def attribute_creation_payload(data):
        char_num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        LobGet.LobGet().user_retrieves_lob(True)
        lob = BuiltIn().get_variable_value("${lob_reponse_body}")[0]
        print("LOB: ", lob)
        AttributeModuleGet.AttributeModuleGet().user_retrieves_attribute_module_by_id("valid")
        module = BuiltIn().get_variable_value("&{att_module_res_body}")
        payload = {
            "ATTRIBUTE": ''.join(secrets.choice(char_num) for _ in range(15)),
            "CODE_DISPLAY": "true",
            "MODULE": module,
            "LOB": lob,
            "MANDATORY": "true",
        }
        print("Module: ", module)

        print("Payload Att Creation: ", payload)

        if data == 'fix':
            details = BuiltIn().get_variable_value("&{attribute_creation_details}")
            payload.update((k, v) for k, v in details.items())
        BuiltIn().set_test_variable("${payload}", payload)
        dump_payload = json.dumps(payload)
        return dump_payload
