from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "user-info" + APP_URL

class UserGroupDelete(object):

    @keyword('user deletes created user group')
    def user_deletes_user_group(self):
        user_group_id = BuiltIn().get_variable_value("${user_group_id}")
        url = "{0}user-group/{1}".format(END_POINT_URL, user_group_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)