import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class AssetConditionGet(object):

    @keyword("user retrieves asset condition listing")
    def user_retrieves_asset_condition_listing(self):
        url = "{0}trade-asset/asset-condition".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${ac_ls}", response.json())
        return str(response.status_code), response.json()

    @keyword("user retrieves asset condition details")
    def user_retrieves_asset_condition_details(self):
        ac_id = BuiltIn().get_variable_value("${ac_id}")
        if not ac_id:
            self.user_retrieves_asset_condition_listing()
            ac_ls = BuiltIn().get_variable_value("${ac_ls}")
            rand_ac = secrets.choice(ac_ls)
            ac_id = rand_ac['ID']

        url = "{0}trade-asset/asset-condition/{1}".format(END_POINT_URL, ac_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${ac_details}", response.json())
        return str(response.status_code), response.json()
