""" Python file related to relationships in module setup API """
import re

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL_METADATA_MODULE = PROTOCOL + "metadata" + APP_URL + "metadata-module"
END_POINT_URL_MODULES = PROTOCOL + "metadata" + APP_URL + "modules"


class RelationshipsGet:
    """ Functions related to relationships in module setup GET request """

    @keyword("user retrieves ${data_type} relationships in ${sequence} module setup")
    def user_retrieves_relationships_in_module_setup(self, data_type, sequence):
        """ Functions to retrieve all/created relationships in module setup """
        digit = re.findall(r'\d+', sequence)[0]
        specific_module_setup_id = "{0}module_setup_id_{1}{2}".format("${", digit, "}")
        print("specific_module_setup_id", specific_module_setup_id)
        module_setup_id = BuiltIn().get_variable_value(specific_module_setup_id)
        url = "{0}/{1}/metadata-relationship".format(END_POINT_URL_METADATA_MODULE, module_setup_id)

        if data_type == "created":
            specific_relationships_id = "{0}relationships_id_{1}{2}".format("${", digit, "}")
            relationships_id = BuiltIn().get_variable_value(specific_relationships_id)
            url = "{0}/{1}".format(url, relationships_id)

        print("GET URL", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

        try:
            body_result = response.json()
            BuiltIn().set_test_variable("${body_result}", body_result)
            print("Result: ", body_result)
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)
