""" Python file related to template in module setup API """

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL_METADATA_MODULE = PROTOCOL + "metadata" + APP_URL + "metadata-module"


class TemplateGet:
    """ Functions related to template in module setup GET request """

    @keyword("user retrieves ${data_type} template in module setup")
    def user_retrieves_template_in_module_setup(self, data_type):
        """ Functions to retrieve all/created template in module setup """
        module_setup_id = BuiltIn().get_variable_value("${module_setup_id}")
        url = "{0}/{1}/metadata-template".format(END_POINT_URL_METADATA_MODULE, module_setup_id)

        if data_type == "created":
            template_id = BuiltIn().get_variable_value("${module_template_id}")
            url = "{0}/{1}".format(url, template_id)

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
