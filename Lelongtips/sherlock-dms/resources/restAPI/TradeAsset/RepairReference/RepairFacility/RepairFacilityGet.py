import secrets

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class RepairFacilityGet(object):

    @keyword("user retrieves repair facility listing")
    def user_retrieves_repair_facility_listing(self):
        url = "{0}trade-asset/repair-facility".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${rf_ls}", response.json())
        return str(response.status_code), response.json()

    @keyword("user retrieves repair facility details")
    def user_retrieves_repair_facility_details(self):
        rf_id = BuiltIn().get_variable_value("${rf_id}")
        if not rf_id:
            self.user_retrieves_repair_facility_listing()
            rf_ls = BuiltIn().get_variable_value("${rf_ls}")
            rand_rf = secrets.choice(rf_ls)
            rf_id = rand_rf['ID']

        url = "{0}trade-asset/repair-facility/{1}".format(END_POINT_URL, rf_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${rf_details}", response.json())
        return str(response.status_code), response.json()
