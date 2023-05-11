from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ProgramGroupDelete(object):
    @keyword('user deletes program group details')
    def user_deletes_program_group_details(self):
        tpg_id = BuiltIn().get_variable_value("${tpg_id}")
        url = "{0}trade-program-group/{1}".format(END_POINT_URL, tpg_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
