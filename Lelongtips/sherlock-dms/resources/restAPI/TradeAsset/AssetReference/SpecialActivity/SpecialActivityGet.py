import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class SpecialActivityGet(object):

    @keyword("user retrieves special activity listing")
    def user_retrieves_special_activity_listing(self):
        url = "{0}trade-asset/special-activity".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${sa_ls}", response.json())
        return str(response.status_code), response.json()

    @keyword("user retrieves special activity details")
    def user_retrieves_special_activity_details(self):
        sa_id = BuiltIn().get_variable_value("${sa_id}")
        if not sa_id:
            self.user_retrieves_special_activity_listing()
            sa_ls = BuiltIn().get_variable_value("${sa_ls}")
            rand_pm = secrets.choice(sa_ls)
            sa_id = rand_pm['ID']

        url = "{0}trade-asset/special-activity/{1}".format(END_POINT_URL, sa_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${sa_details}", response.json())
        return str(response.status_code), response.json()
