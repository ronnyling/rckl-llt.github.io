import json
import secrets

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


END_POINT_URL = PROTOCOL + "dynamic-attribute" + APP_URL


class AttributeCreationPut(object):

    @keyword("user update created attribute creation")
    def update_attribute_creation(self):
        attribute_creation_id = BuiltIn().get_variable_value("${attribute_creation_id}")
        url = "{0}dynamic-attribute/{1}".format(END_POINT_URL, attribute_creation_id)

        char_num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        newdict = BuiltIn().get_variable_value("&{res_body}")
        print("Newdict: ", newdict)
        update_desc = {'ATTRIBUTE': ''.join(secrets.choice(char_num) for _ in range(15))}
        newdict.update(update_desc)

        print("Payload for update ", newdict)
        payload = json.dumps(newdict)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code
