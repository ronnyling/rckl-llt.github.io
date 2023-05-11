from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class MessageTypeGet(object):

    def user_gets_all_message_type_data(self):
        url = "{0}message-type".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("all message data", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_gets_message_type_by_using_id(self):
        message_id = BuiltIn().get_variable_value("${message_id}")
        url = "{0}message-type/{1}".format(END_POINT_URL, message_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("message data", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
