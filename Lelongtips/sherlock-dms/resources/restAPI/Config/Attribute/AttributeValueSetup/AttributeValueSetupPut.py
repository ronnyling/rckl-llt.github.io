import json
import secrets

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


END_POINT_URL = PROTOCOL + "dynamic-attribute" + APP_URL


class AttributeValueSetupPut(object):

    @keyword("user update created attribute value setup")
    def update_attribute_value_setup(self):
        attribute_value_setup_id = BuiltIn().get_variable_value("${attribute_value_setup_id}")
        url = "{0}attribute-value-creation/{1}".format(END_POINT_URL, attribute_value_setup_id)

        char_num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        newdict = BuiltIn().get_variable_value("&{res_body}")
        print("Newdict: ", newdict)
        update_desc = {'Attribute Value': ''.join(secrets.choice(char_num) for _ in range(15))}
        newdict.update(update_desc)

        print("Payload for update ", newdict)
        payload = json.dumps(newdict)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code
