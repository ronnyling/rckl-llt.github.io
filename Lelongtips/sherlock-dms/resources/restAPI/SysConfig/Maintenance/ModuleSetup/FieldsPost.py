""" Python file related to module setup API """
import json
import secrets
import string

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "metadata" + APP_URL + "metadata-module"


class FieldsPost:
    """ Functions related to fields in module setup POST request """

    @keyword("user creates fields in module setup using ${data_type} data")
    def user_creates_fields_in_module_setup_using_data(self, data_type):
        """ Functions to create fields in module setup using random/fixed data """

        module_setup_id = BuiltIn().get_variable_value("${module_setup_id}")
        module_logical_id = BuiltIn().get_variable_value("${module_logical_id}")
        url = "{0}/{1}/metadata-field".format(END_POINT_URL, module_setup_id)

        if data_type == "fixed":
            fixed_data = BuiltIn().get_variable_value("${FieldsDetails}")
            payload = self.create_payload_fields(module_logical_id, fixed_data)
        else:
            payload = self.create_payload_fields(module_logical_id, fixed_data=None)

        print("POST URL", url)
        print("POST Payload", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

        try:
            body_result = response.json()
            print("Result: ", body_result)
            BuiltIn().set_test_variable("${module_fields_id}", body_result['ID'])
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)

    def create_payload_fields(self, module_logical_id, fixed_data):
        """ Functions to create payload for fields in module setup """
        alphabet = string.digits + string.ascii_letters
        random_char = ''.join(secrets.choice(alphabet) for _ in range(5))
        selected_type = secrets.choice(["text", "boolean", "id", "integer", "date"])
        if selected_type == "text":
            display_type = secrets.choice(
                ["checkbox", "custom", "datefield", "dropdown", "hidden", "lookup", "numberfield", "radiobutton",
                 "template", "textareafield", "textfield", "timefield", "toggle"])
        elif selected_type == "integer":
            display_type = secrets.choice(["custom", "numberfield", "hidden"])
        elif selected_type == "boolean":
            display_type = secrets.choice(["custom", "checkbox", "toggle", "hidden"])
        elif selected_type == "date":
            display_type = secrets.choice(["custom", "datefield", "hidden"])
        elif selected_type in ["multilanguage", "auto-increment"]:
            display_type = secrets.choice(["custom", "textfield", "hidden"])
        elif selected_type == "relationship":
            display_type = secrets.choice(["custom", "dropdown", "hidden", "lookup", "radiobutton", "template"])
        elif selected_type == "multiple":
            display_type = secrets.choice(["custom", "lookup", "multidd", "multiselect", "hidden"])
        elif selected_type == "id":
            display_type = secrets.choice(["textfield", "hidden"])

        alphabet = string.ascii_uppercase
        payload = {
            'MODULE_ID': module_logical_id,
            'LABEL': ''.join(random_char),
            'DESCRIPTION': ''.join(random_char),
            'FIELD': ''.join(secrets.choice(alphabet) for _ in range(10)),
            'TYPE': selected_type,
            'DISPLAY_TYPE': display_type,
            'ORDER_SEQ': secrets.choice(range(1, 10)),
            'VALIDATION': None,
            'FILTERABLE': None,
            'REF_LOGICAL_ID': None,
            'REF_DISPLAY_FIELD': None,
        }

        if fixed_data:
            payload.update((k, v) for k, v in fixed_data.items())

        payload = json.dumps(payload)

        return payload
