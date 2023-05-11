from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import secrets
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class MessageTypePost(object):

    @keyword('user creates message type with random data')
    def user_creates_message_with(self):
        url = "{0}message-type".format(END_POINT_URL)
        payload = self.payload_message()
        payload = json.dumps(payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_res = response.json()
            BuiltIn().set_test_variable("${message_id}", body_res['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_message(self):
        status = 'M'
        payload = {
            "MSG_TYPE_CD": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
            "MSG_TYPE_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(40)),
            "MSG_TYPE" : status
        }
        print(payload)

        return payload