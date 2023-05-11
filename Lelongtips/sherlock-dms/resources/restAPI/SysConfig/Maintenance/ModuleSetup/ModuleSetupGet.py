""" Python file related to module setup API """
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL_METADATA_MODULE = PROTOCOL + "metadata" + APP_URL + "metadata-module"
END_POINT_URL_MODULES = PROTOCOL + "metadata" + APP_URL + "modules"


class ModuleSetupGet:
    """ Functions related to module setup GET request """

    @keyword("user retrieves ${data_type} module setup")
    def user_retrieves_module_setup(self, data_type):
        """ Functions to retrieve all/created/fixed module setup """
        url = END_POINT_URL_METADATA_MODULE

        if data_type == "created":
            module_setup_id = BuiltIn().get_variable_value("${module_setup_id}")
            url = "{0}/{1}".format(END_POINT_URL_METADATA_MODULE, module_setup_id)
        elif data_type == "fixed":
            module_logical_id = BuiltIn().get_variable_value("${module_logical_id}")
            url = "{0}/{1}".format(END_POINT_URL_MODULES, module_logical_id)

        print("GET URL", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

        try:
            body_result = response.json()
            print("Result: ", body_result)

            if data_type == "fixed":
                module_setup_id = body_result[0]["ID"]
                BuiltIn().set_test_variable("${module_setup_id}", module_setup_id)

        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)

    def retrieves_variable_value(self, data_type, variable_name, url):
        """ Functions to retrieve for fields and template api """
        if data_type == "created":
            common_id = BuiltIn().get_variable_value(variable_name)
            url = "{0}/{1}".format(url, common_id)

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