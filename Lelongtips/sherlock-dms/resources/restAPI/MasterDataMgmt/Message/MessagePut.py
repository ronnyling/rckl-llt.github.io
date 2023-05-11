from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Message import MessagePost
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from faker import Faker
fake = Faker()

END_POINT_URL = PROTOCOL + "message" + APP_URL


class MessagePut(object):
    """ Functions to updates message """

    @keyword('user updates message as ${user} and send to ${assign} with ${data_type} data')
    def user_updates_message_with_data(self, user, assign, data_type):
        """ Function to update message using fixed/random data """
        msg_id = BuiltIn().get_variable_value("${res_bd_msg_id}")
        msg_details = BuiltIn().get_variable_value("${msg_details}")
        if msg_details is None:
            msg_details = {"ID": msg_id, 'ACTION': "update"}
        else:
            msg_details.update({"ID": msg_id, 'ACTION': "update"})

        res_bd_msg = BuiltIn().get_variable_value("${res_bd_msg}")
        update_action = BuiltIn().get_variable_value("${link_action}")
        posted_link = res_bd_msg['LINKS']
        posted_attachment = res_bd_msg['ATTACHMENTS']
        if len(posted_link) != 0 and update_action is not None:
            msg_details['LINKS'] = [
                {
                    "ID": posted_link[0]['ID'],
                    "MSG_SETUP_ID": msg_id,
                    "ACTION": update_action,
                    "URL": posted_link[0]['URL'],
                    "URL_DESC": posted_link[0]['URL_DESC'],
                    'VERSION': 1
                }
            ]
        if len(posted_attachment) != 0 and update_action is not None:
            msg_details['ATTACHMENTS'] = [
                {
                    "ID": posted_attachment[0]['ID'],
                    "MSG_SETUP_ID": msg_id,
                    "ACTION": update_action,
                    "URL": posted_attachment[0]['URL'],
                    "FILE_NAME": posted_attachment[0]['FILE_NAME'],
                    "FILE_TYPE": posted_attachment[0]['FILE_TYPE'],
                    "FILE_SIZE": str(posted_attachment[0]['FILE_SIZE']),
                    'VERSION': 1
                }
            ]
        BuiltIn().set_test_variable("${msg_details}", msg_details)
        url = "{0}msg-setup/{1}".format(END_POINT_URL, msg_id)
        payload = MessagePost.MessagePost().payload_message(user, assign, data_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
