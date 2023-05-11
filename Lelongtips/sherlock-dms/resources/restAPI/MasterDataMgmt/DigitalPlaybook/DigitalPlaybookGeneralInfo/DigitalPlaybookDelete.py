from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "message" + APP_URL


class DigitalPlaybookDelete(object):
    """Function to delete playbook"""

    def user_deletes_playbook_with_created_data(self):
        playbook_id = BuiltIn().get_variable_value("${playbook_id}")
        url = "{0}playbk-setup/{1}".format(END_POINT_URL, playbook_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
