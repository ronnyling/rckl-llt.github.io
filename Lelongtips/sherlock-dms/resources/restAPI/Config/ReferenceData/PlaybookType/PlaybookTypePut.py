from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.ReferenceData.PlaybookType.PlaybookTypePost import PlaybookTypePost
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from setup.hanaDB import HanaDB

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class PlaybookTypePut(object):

    @keyword('user updates playbook type with ${type} data')
    def user_updates_playbook_type_with(self, type):
        playbook_id = BuiltIn().get_variable_value("${playbook_id}")
        playbook_cd = BuiltIn().get_variable_value("${playbook_cd}")
        url = "{0}playbook-type/{1}".format(END_POINT_URL, playbook_id)
        details = BuiltIn().get_variable_value("${playbook_details}")
        update_playbook = {
            "ID": playbook_id,
            "PLAYBOOK_TYPE_CD": playbook_cd,
            "VERSION": 1
        }
        if details is not None:
            details.update(update_playbook)
        else:
            details = update_playbook
        BuiltIn().set_test_variable("${playbook_details}", details)
        payload = PlaybookTypePost().payload_playbook(type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().user_validates_database_data("playbook-type", body_result)
            # HanaDB.HanaDB().disconnect_from_database()
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
