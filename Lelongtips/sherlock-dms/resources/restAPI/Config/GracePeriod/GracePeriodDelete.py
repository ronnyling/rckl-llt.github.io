
import datetime
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "setting" + APP_URL
NOW = datetime.datetime.now()


class GracePeriodDelete:

    @keyword("user deletes created grace period ")
    def user_deleted_grace_period(self):
        grace_period_id = BuiltIn().get_variable_value("${grace_period_id}")
        url = "{0}grace-period/{1}".format(END_POINT_URL, grace_period_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)



