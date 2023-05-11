from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI.Config.Attribute.AttributeCreation.AttributeCreationGet import AttributeCreationGet

END_POINT_URL = PROTOCOL + "dynamic-attribute" + APP_URL


class AttributeCreationDelete(object):

    @keyword('user deletes created attribute creation')
    def user_deletes_attribute_creation(self):
        attribute_creation_id = BuiltIn().get_variable_value("${attribute_creation_id}")
        url = "{0}dynamic-attribute/{1}".format(END_POINT_URL, attribute_creation_id)
        print("Delete URL: ", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
