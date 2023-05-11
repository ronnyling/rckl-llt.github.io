
import datetime
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "setting" + APP_URL
NOW = datetime.datetime.now()


class GracePeriodGet:

    @keyword("user retrieves ${cond} grace period")
    def user_retrieves_grace_period(self, cond):
        if cond == "all":
            url = "{0}grace-period".format(END_POINT_URL)
        else:
            grace_period_id = BuiltIn().get_variable_value("${grace_period_id}")
            url = "{0}grace-period/{1}".format(END_POINT_URL, grace_period_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        if response.status_code == 200:
            BuiltIn().set_test_variable("${res_bd_grace_period}", response.json())
        BuiltIn().set_test_variable("${status_code}", response.status_code)



