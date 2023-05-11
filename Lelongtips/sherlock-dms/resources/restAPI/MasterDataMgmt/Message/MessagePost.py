from resources.restAPI import PROTOCOL, APP_URL
from setup.hanaDB import HanaDB
from resources.restAPI.Common import APIMethod, TokenAccess, APIAssertion
from resources.restAPI.Config.ReferenceData.MessageType import MessageTypePost
from resources.restAPI.SysConfig.Maintenance.ModuleSetup import FieldsGet
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from faker import Faker
import secrets
import string
import json
import datetime
fake = Faker()
today = datetime.datetime.now()

END_POINT_URL = PROTOCOL + "message" + APP_URL


class MessagePost(object):
    """ Functions to create message """

    @keyword('user creates message as ${user} and send to ${assign} with ${data_type} data')
    def user_creates_message_with_data(self, user, assign, data_type):
        """ Function to create message using fixed/random data """
        url = "{0}msg-setup".format(END_POINT_URL)
        payload = self.payload_message(user, assign, data_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            res_bd_msg_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_msg_id}", res_bd_msg_id)
            BuiltIn().set_test_variable("${res_bd_msg}", body_result)
            # res_bd_msg_id = str(res_bd_msg_id).replace(":", "").replace("-", "")
            # HanaDB.HanaDB().connect_database_to_environment()
            # msg_result = HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM MSG_SETUP where ID = '{0}'"
            #                                                             .format(res_bd_msg_id), 1)
            # HanaDB.HanaDB().disconnect_from_database()
            # assert msg_result, "Record not found in database"
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_message(self, user, assign, data_type):
        """ Function for message payload content """
        op_type_set = {
            "Vansales": "V",
            "Presales": "O",
            "Merchandiser": "M",
            "HQ Merchandiser": "H",
            "HQ Salesman": "Q"
        }
        user_set = {
            "Distributor": "D",
            "Route": "R"
        }
        send_to = None
        op_type = None
        assign_split = assign.split(":")
        if user == 'HQ':
            send_to = user_set[assign_split[0]]
            op_type = []
        if send_to == 'R':
            op_type_split = assign_split[1].split(",")
            for type in op_type_split:
                op_type.append(op_type_set[type])
        msg_type_id = BuiltIn().get_variable_value("${message_id}")
        start_date = today + + datetime.timedelta(days=2)
        end_date = today + + datetime.timedelta(days=10)
        payload = {
            'VERSION': 1,
            'ID': None,
            'SUBJECT': "Message Subject {0}".format(today),
            'SEND_TO': send_to,
            'OP_TYPE': op_type,
            'TYPE': msg_type_id,
            'START_DT': str(start_date.strftime("%Y-%m-%d")),
            'END_DT': str(end_date.strftime("%Y-%m-%d")),
            'CONTENT': (fake.sentence()[:500]),
            'ACTION': "create",
            'DIST_ASS_ALL': False,
            'ROUTE_ASS_ALL': False,
            'MSG_PRIORITY': secrets.choice(["alert", "high-priority", "medium-priority"]),
            "LINKS": [
                {
                    "ACTION": "create",
                    "URL": "https://" + fake.word() + ".com",
                    "URL_DESC": fake.word(),
                    'VERSION': 1
                }
            ],
            "ATTACHMENTS": []
        }
        if data_type == 'InvalidSubject':
            payload['SUBJECT'] = ''.join(secrets.choice(string.ascii_letters) for _ in range(101))
        if data_type == 'InvalidContent':
            payload['CONTENT'] = ''.join(secrets.choice(string.ascii_letters) for _ in range(501))
        various_type = {
            "ppt": "application/vnd.ms-powerpoint",
            "pdf": "application/pdf",
            "mp4": "video/mp4",
            "jpg": "image/jpeg",
            "png": "image/png"
        }
        file_type = BuiltIn().get_variable_value("${file_type}")
        if file_type is not None:
            rand_file = FieldsGet.FieldsGet().user_retrieves_random_attachment_from_objectstore \
                ("msg-setup", "attachment", file_type)
            file_name = rand_file.replace('/objectstore-svc/api/v1.0/storage/msg-setup/attachment/', '')
            if not file_name:
                file_name = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(10)) + "." + file_type
            try:
                type_input = various_type[file_type]
            except Exception as e:
                print(e.__class__, "occured")
                type_input = "video/" + file_type

            file_data = {
                "URL": rand_file,
                "FILE_NAME": file_name,
                "NAME": file_name,
                "FILE_SIZE": ''.join(secrets.choice(string.digits) for _ in range(2)),
                "FILE_TYPE": type_input,
                "ACTION": "create",
                'VERSION': 1
            }
            payload["ATTACHMENTS"].append(file_data)

        details = BuiltIn().get_variable_value("${msg_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Message Payload: ", payload)
        return payload

    def user_creates_prerequisite_for_message(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        MessageTypePost.MessageTypePost().user_creates_message_with()
        APIAssertion.APIAssertion().expected_return_status_code("201")
