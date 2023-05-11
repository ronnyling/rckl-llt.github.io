""" Python file related to module setup API """
import json
import secrets
import string
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.SysConfig.Maintenance.ModuleSetup import ModuleSetupGet
from resources.Common import Common

END_POINT_URL = PROTOCOL + "metadata" + APP_URL + "metadata-module"


class ModuleSetupPost:
    """ Functions related to module setup POST request """
    MODULE_LOGICAL_ID = "${module_logical_id}"
    TEST = "test{0}"

    @keyword("user creates module setup using ${data_type} data")
    def user_creates_module_setup_using_data(self, data_type):
        """ Functions to create module setup using random/fixed data """
        url = END_POINT_URL

        payload = self.create_payload_module_setup(fixed_data=None)

        if data_type == "fixed":
            fixed_data = BuiltIn().get_variable_value("${ModuleSetupDetails}")
            module_logical_id = fixed_data["LOGICAL_ID"]
            BuiltIn().set_test_variable(self.MODULE_LOGICAL_ID, module_logical_id)
            common = ModuleSetupGet.ModuleSetupGet()
            common.user_retrieves_module_setup("fixed")
            status_code = BuiltIn().get_variable_value(Common.STATUS_CODE)

            if status_code == 200:
                BuiltIn().set_test_variable(Common.STATUS_CODE, 201)
                return
            payload = self.create_payload_module_setup(fixed_data)

        print("POST URL", url)
        print("POST Payload", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

        try:
            body_result = response.json()
            print("Result: ", body_result)
            BuiltIn().set_test_variable("${module_setup_id}", body_result['ID'])
            BuiltIn().set_test_variable(self.MODULE_LOGICAL_ID, body_result['LOGICAL_ID'])
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)

    def create_payload_module_setup(self, fixed_data):
        """ Functions to create payload for module setup """
        alphabet = string.digits + string.ascii_letters
        random_char = ''.join(secrets.choice(alphabet) for _ in range(5))
        payload = {
            'TENANT_ID': None,
            'LOGICAL_ID': self.TEST.format(random_char),
            'TITLE': self.TEST.format(random_char),
            'DESCRIPTION': self.TEST.format(random_char),
            'SERVICE_PARAMETERS': "[\"module-data\"]",
            'SERVICE_NAME': "metadata-svc",  # metadata-svc is a generic service for new module
            'SERVICE_VERSION': "1.0",  # 1.0 is a generic version for new module
            'VERSION': secrets.choice(range(1, 10)),
            'TYPE': 'D'
        }

        if fixed_data:
            payload.update((k, v) for k, v in fixed_data.items())

        payload = json.dumps(payload)

        return payload

    @keyword("user creates total ${total_number} module setup using ${data_type} data")
    def user_creates_total_module_setup_using_data(self, total_number, data_type):
        """ Functions to create more than one module setup using random/fixed data """
        for number in range(1, int(total_number)+1):
            self.user_creates_module_setup_using_data(data_type)
            try:
                module_setup_id = BuiltIn().get_variable_value("${module_setup_id}")
                specific_module_setup_id = "{0}module_setup_id_{1}{2}".format("${", number, "}")
                BuiltIn().set_test_variable(specific_module_setup_id, module_setup_id)
                module_logical_id = BuiltIn().get_variable_value(self.MODULE_LOGICAL_ID)
                specific_module_logical_id = "{0}module_logical_id_{1}{2}".format("${", number, "}")
                BuiltIn().set_test_variable(specific_module_logical_id, module_logical_id)
            except Exception as e:
                print(e.__class__, "occured")
                print("Unable to create module setup!")
