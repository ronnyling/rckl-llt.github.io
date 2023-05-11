import json
import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class PlaybookTypeGet(object):
    """ Functions to retrieve playbook type record """

    def user_gets_all_playbook_type_data(self):
        """ Functions to retrieve all playbook type record """
        url = "{0}playbook-type".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of Playbook Type retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_gets_playbook_type_by_using_id(self):
        """ Functions to retrieve playbook type record by using id given """
        playbook_id = BuiltIn().get_variable_value("${playbook_id}")
        url = "{0}playbook-type/{1}".format(END_POINT_URL, playbook_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == playbook_id, "ID retrieved not matched"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_gets_playbook_type_by_using_field(self, key, value):
        """ Function to retrieve playbook type using field """
        filter_reason = {key: {"$eq": value}}
        filter_reason = json.dumps(filter_reason)
        str(filter_reason).encode(encoding='UTF-8', errors='strict')
        url = "{0}playbook-type?filter={1}".format(END_POINT_URL, filter_reason)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to get playbook type by using key and value"
        body_result = response.json()
        if len(body_result) > 1:
            random_sel = secrets.choice(range(0, len(body_result)-1))
        else:
            random_sel = 0
        res_bd_playbook_type_id = body_result[random_sel]['ID']
        return res_bd_playbook_type_id

