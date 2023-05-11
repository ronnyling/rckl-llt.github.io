import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class AssetTypeGet(object):

    @keyword("user retrieves trade asset type listing")
    def user_retrieves_trade_asset_type_listing(self):
        url = "{0}trade-asset/trade-asset-type".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${tat_ls}", response.json())
        return str(response.status_code), response.json()

    @keyword("user retrieves trade asset type details")
    def user_retrieves_trade_asset_type_details(self):
        tat_id = BuiltIn().get_variable_value("${tat_id}")
        if not tat_id:
            self.user_retrieves_trade_asset_type_listing()
            tat_ls = BuiltIn().get_variable_value("${tat_ls}")
            rand_tat = secrets.choice(tat_ls)
            tat_id = rand_tat['ID']

        url = "{0}trade-asset/trade-asset-type/{1}".format(END_POINT_URL, tat_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${tat_details}", response.json())
        return str(response.status_code), response.json()
