from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class SpecialActivityDelete(object):
    @keyword("user deletes special activity")
    def user_deletes_special_activity(self):
        sa_id = BuiltIn().get_variable_value("${sa_id}")
        url = "{0}trade-asset/special-activity/{1}".format(END_POINT_URL, sa_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code), response.json()
