from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
import secrets
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from setup.hanaDB import HanaDB

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class PlaybookTypePost(object):

    @keyword('user creates playbook type with ${type} data')
    def user_creates_playbook_type_with(self, type):
        url = "{0}playbook-type".format(END_POINT_URL)
        payload = self.payload_playbook(type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print("Playbook respond: ", response.text)
        if response.status_code == 201:
            body_res = response.json()
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().user_validates_database_data("playbook-type", body_res)
            # HanaDB.HanaDB().disconnect_from_database()
            BuiltIn().set_test_variable("${playbook_cd}", body_res['PLAYBOOK_TYPE_CD'])
            BuiltIn().set_test_variable("${playbook_id}", body_res['ID'])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def payload_playbook(self, type):
        payload = {
            "PLAYBOOK_TYPE_CD": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
            "PLAYBOOK_TYPE_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(40)),
            "PLAYBOOK_PRD_HIER_REQ": secrets.choice(['0', '1'])
        }
        if type == 'existing':
            payload['PLAYBOOK_TYPE_CD'] = BuiltIn().get_variable_value("${playbook_cd}")
        details = BuiltIn().get_variable_value("${playbook_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Playbook Payload: ", payload)
        return payload
