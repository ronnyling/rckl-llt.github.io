import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class AssetMasterGet(object):

    @keyword("user retrieves asset master listing")
    def user_retrieves_asset_master_listing(self):
        url = "{0}trade-asset/asset-master".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${am_ls}", response.json())
        return str(response.status_code), response.json()

    @keyword("user retrieves asset master details")
    def user_retrieves_asset_master_details(self):
        am_id = BuiltIn().get_variable_value("${am_id}")
        if not am_id:
            self.user_retrieves_asset_master_listing()
            am_ls = BuiltIn().get_variable_value("${am_ls}")
            rand_am = secrets.choice(am_ls)
            am_id = rand_am['ID']

        url = "{0}trade-asset/asset-master/{1}".format(END_POINT_URL, am_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${am_details}", response.json())
        return str(response.status_code), response.json()
