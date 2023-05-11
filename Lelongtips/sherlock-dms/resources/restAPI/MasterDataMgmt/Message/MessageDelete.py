from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod, TokenAccess, APIAssertion
from resources.restAPI.Config.ReferenceData.MessageType import MessageTypeDelete

END_POINT_URL = PROTOCOL + "message" + APP_URL


class MessageDelete(object):
    """ Functions to delete message record """

    def user_deletes_message_with_created_data(self):
        """ Function to delete message by using given id """
        res_bd_msg_id = BuiltIn().get_variable_value("${res_bd_msg_id}")
        url = "{0}msg-setup/{1}".format(END_POINT_URL, res_bd_msg_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_deletes_prerequisite_for_message(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        MessageTypeDelete.MessageTypeDelete().user_deletes_message_type_with_created_data()
        APIAssertion.APIAssertion().expected_return_status_code("200")
