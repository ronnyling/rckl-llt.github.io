from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "message" + APP_URL


class MessageGet(object):
    """ Functions to retrieve message records """

    def user_gets_all_message_data(self):
        """ Function to retrieve all message record """
        url = "{0}msg-setup".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response

    def user_gets_message_by_using_id(self):
        """ Function to retrieve message given id """
        res_bd_msg_id = BuiltIn().get_variable_value("${res_bd_msg_id}")
        url = "{0}msg-setup/{1}".format(END_POINT_URL, res_bd_msg_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_msg_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response

    @keyword('user gets all message to validate ${data_type}')
    def user_gets_all_message_to_validate(self, data_type):
        if data_type == 'url':
            check_field = "LINKS"
        else:
            check_field = "ATTACHMENTS"
        response = self.user_gets_all_message_data()
        if response.status_code == 200:
            body_result = response.json()
            for i in range(0, len(body_result)):
                assert check_field in body_result[i], "URL/ATTACHMENT Key not found in payload"

    @keyword('user gets message by id to validate ${data_type}')
    def user_gets_message_by_id_to_validate(self, data_type):
        if data_type == 'url':
            check_field = "LINKS"
        else:
            check_field = "ATTACHMENTS"
        response = self.user_gets_message_by_using_id()
        res_bd_msg = BuiltIn().get_variable_value("${res_bd_msg}")
        if response.status_code == 200:
            body_result = response.json()
            assert res_bd_msg[check_field] == body_result[check_field], "URL/ATTACHMENT Key not found in payload"
