""" Python file related to module setup API """
import json
import string
import secrets

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "metadata" + APP_URL + "metadata-module"


class TemplatePost:
    """ Functions related to fields in module setup POST request """

    @keyword("user creates template in module setup using ${data_type} data")
    def user_creates_fields_in_module_setup_using_data(self, data_type):
        """ Functions to create fields in module setup using random/fixed data """

        module_setup_id = BuiltIn().get_variable_value("${module_setup_id}")
        module_logical_id = BuiltIn().get_variable_value("${module_logical_id}")
        url = "{0}/{1}/metadata-template".format(END_POINT_URL, module_setup_id)

        if data_type == "fixed":
            fixed_data = BuiltIn().get_variable_value("${TemplateDetails}")
            payload = self.create_payload_template(module_logical_id, fixed_data)
        else:
            payload = self.create_payload_template(module_logical_id, fixed_data=None)

        print("POST URL", url)
        print("POST Payload", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

        try:
            body_result = response.json()
            print("Result: ", body_result)
            BuiltIn().set_test_variable("${module_template_id}", body_result['ID'])
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)

    def create_payload_template(self, module_logical_id, fixed_data, **template_details):
        """ Functions to create payload for template in module setup """
        template_details = json.dumps(template_details)
        payload = {
            'MODULE_ID': module_logical_id,
            "TYPE": ''.join(secrets.choice(string.ascii_letters) for _ in range(10)),
            'DESCRIPTION': ''.join(secrets.choice(string.digits + string.ascii_letters) for _ in range(10)),
            'CONTENT': "[{0}]".format(template_details)
        }

        if fixed_data:
            payload.update((k, v) for k, v in fixed_data.items())

        payload = json.dumps(payload)

        return payload
