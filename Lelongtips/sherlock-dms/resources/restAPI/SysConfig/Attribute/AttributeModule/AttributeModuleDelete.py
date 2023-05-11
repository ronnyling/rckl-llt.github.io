from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class AttributeModuleDelete(object):
    @keyword('user deletes created attribute module')
    def user_deletes_attribute_module(self):
        attribute_module_id = BuiltIn().get_variable_value("${attribute_module_id}")
        url = "{0}module-data/module/{1}".format(END_POINT_URL, attribute_module_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response

