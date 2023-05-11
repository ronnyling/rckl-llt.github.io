import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class RepairReasonGet(object):

    @keyword("user retrieves repair reason listing")
    def user_retrieves_repair_reason_listing(self):
        url = "{0}trade-asset/repair-reason".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${rr_ls}", response.json())
        return str(response.status_code), response.json()

    @keyword("user retrieves repair reason details")
    def user_retrieves_repair_reason_details(self):
        rr_id = BuiltIn().get_variable_value("${rr_id}")
        if not rr_id:
            self.user_retrieves_repair_reason_listing()
            rr_ls = BuiltIn().get_variable_value("${rr_ls}")
            rand_rr = secrets.choice(rr_ls)
            rr_id = rand_rr['ID']

        url = "{0}trade-asset/repair-reason/{1}".format(END_POINT_URL, rr_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${rr_details}", response.json())
        return str(response.status_code), response.json()
