from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "dynamic-attribute" + APP_URL


class AttributeValueSetupDelete(object):

    @keyword('user deletes created attribute value setup')
    def user_deletes_attribute_value_setup(self):
        attribute_value_setup_id = BuiltIn().get_variable_value("${attribute_value_setup_id}")
        url = "{0}attribute-value-creation/{1}".format(END_POINT_URL, attribute_value_setup_id)
        print("Delete URL: ", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
