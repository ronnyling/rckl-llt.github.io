""" Python file related to module setup API """
import json
import secrets
import re

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.SysConfig.Maintenance.ModuleSetup import RelationshipsGet

END_POINT_URL = PROTOCOL + "metadata" + APP_URL + "metadata-module"


class RelationshipsPost:
    """ Functions related to relationships in module setup POST request """

    @keyword("user creates relationships in ${sequence} module setup using ${data_type} data")
    def user_creates_relationships_in_module_setup_using_data(self, sequence, data_type):
        """ Functions to create relationships in module setup using random/fixed data """

        digit = re.findall(r'\d+', sequence)[0]
        specific_module_setup_id = "{0}module_setup_id_{1}{2}".format("${", digit, "}")
        module_setup_id = BuiltIn().get_variable_value(specific_module_setup_id)
        specific_module_logical_id = "{0}module_logical_id_{1}{2}".format("${", digit, "}")
        module_logical_id = BuiltIn().get_variable_value(specific_module_logical_id)
        url = "{0}/{1}/metadata-relationship".format(END_POINT_URL, module_setup_id)

        if data_type == "fixed":
            fixed_data = BuiltIn().get_variable_value("${RelationshipsDetails}")
            payload = self.create_payload_relationships(module_logical_id, fixed_data)
        else:
            payload = self.create_payload_relationships(module_logical_id, fixed_data=None)

        print("POST URL", url)
        print("POST Payload", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

        try:
            body_result = response.json()
            print("Result: ", body_result)
            specific_relationships_id = "{0}relationships_id_{1}{2}".format("${", digit, "}")
            BuiltIn().set_test_variable(specific_relationships_id, body_result['ID'])
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)

    def create_payload_relationships(self, module_logical_id, fixed_data):
        """ Functions to create payload for relationships in module setup """
        payload = {
            "TARGET_MODULE": module_logical_id,
            "TYPE": secrets.choice(['1', '2', '3', '4']),
            # "TYPE": secrets.choice(["Child", "Contains", "Multiple", "Child_Contains"]),
            "ORDER_SEQ": secrets.choice(range(1, 10))
        }

        if fixed_data:
            payload.update((k, v) for k, v in fixed_data.items())

        payload = json.dumps(payload)

        return payload

    @keyword("user verified relationships in ${sequence} module setup is created")
    def user_verified_relationships_in_module_setup_is_created(self, sequence):
        """ Functions to verified if fixed data relationships created in module setup """
        fixed_data = BuiltIn().get_variable_value("${RelationshipsDetails}")
        data_type = fixed_data["TYPE"]
        order_seq = fixed_data["ORDER_SEQ"]
        RelationshipsGet.RelationshipsGet().user_retrieves_relationships_in_module_setup("fixed", sequence)

        status_code = BuiltIn().get_variable_value("${status_code}")

        if status_code == 200:
            body_result = BuiltIn().get_variable_value("${body_result}")
            for dic in body_result:
                if dic["TYPE"] == data_type and dic["ORDER_SEQ"] == order_seq:
                    return
        self.user_creates_relationships_in_module_setup_using_data(sequence, "fixed")
