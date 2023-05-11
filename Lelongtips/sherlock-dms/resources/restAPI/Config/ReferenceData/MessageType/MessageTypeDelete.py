from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class MessageTypeDelete(object):

    def user_deletes_message_type_with_created_data(self):
        message_id = BuiltIn().get_variable_value("${message_id}")
        url = "{0}message-type/{1}".format(END_POINT_URL, message_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)