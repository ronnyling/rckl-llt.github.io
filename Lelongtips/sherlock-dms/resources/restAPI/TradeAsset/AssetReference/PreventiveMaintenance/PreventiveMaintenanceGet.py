import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class PreventiveMaintenanceGet(object):

    @keyword("user retrieves preventive maintenance listing")
    def user_retrieves_preventive_maintenance_listing(self):
        url = "{0}trade-asset/preventive-maintenance".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${pm_ls}", response.json())
        return str(response.status_code), response.json()

    @keyword("user retrieves preventive maintenance details")
    def user_retrieves_preventive_maintenance_details(self):
        pm_id = BuiltIn().get_variable_value("${pm_id}")
        if not pm_id:
            self.user_retrieves_preventive_maintenance_listing()
            pm_ls = BuiltIn().get_variable_value("${pm_ls}")
            rand_pm = secrets.choice(pm_ls)
            pm_id = rand_pm['ID']

        url = "{0}trade-asset/preventive-maintenance/{1}".format(END_POINT_URL, pm_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${pm_details}", response.json())
        return str(response.status_code), response.json()
