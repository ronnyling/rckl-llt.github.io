import secrets

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class AssetMovementGet(object):
    @keyword("user retrieves asset movement listing")
    def user_retrieves_asset_movement_listing(self):
        url = "{0}trade-asset/asset-movement".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${amm_ls}", response.json())
        return str(response.status_code), response.json()

    @keyword("user retrieves asset movement details")
    def user_retrieves_asset_movement_details(self):
        amm_id = BuiltIn().get_variable_value("${amm_id}")
        if not amm_id:
            self.user_retrieves_asset_movement_listing()
            amm_ls = BuiltIn().get_variable_value("${amm_ls}")
            rand_amm = secrets.choice(amm_ls)
            amm_id = rand_amm['ID']

        url = "{0}trade-asset/asset-movement/{1}".format(END_POINT_URL, amm_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${amm_details}", response.json())
        return str(response.status_code), response.json()

    def user_retrieves_movement_asset_master(self):
        url = "{0}trade-asset/movement-asset-master".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${mam_ls}", response.json())
        return str(response.status_code), response.json()

    def user_retrieves_movement_reasons(self):
        url = "{0}trade-asset/asset-movement-reasons".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${mr_ls}", response.json())
        return str(response.status_code), response.json()
