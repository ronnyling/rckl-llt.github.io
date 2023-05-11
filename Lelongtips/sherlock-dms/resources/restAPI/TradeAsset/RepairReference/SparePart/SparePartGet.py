import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class SparePartGet(object):

    @keyword("user retrieves spare part listing")
    def user_retrieves_spare_part_listing(self):
        url = "{0}trade-asset/spare-part".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${sp_ls}", response.json())
        return str(response.status_code), response.json()

    @keyword("user retrieves spare part details")
    def user_retrieves_spare_part_details(self):
        sp_id = BuiltIn().get_variable_value("${sp_id}")
        if not sp_id:
            self.user_retrieves_spare_part_listing()
            sp_ls = BuiltIn().get_variable_value("${sp_ls}")
            rand_sp = secrets.choice(sp_ls)
            sp_id = rand_sp['ID']

        url = "{0}trade-asset/spare-part/{1}".format(END_POINT_URL, sp_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${sp_details}", response.json())
        return str(response.status_code), response.json()
