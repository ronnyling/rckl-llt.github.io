import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ManufacturerGet(object):

    @keyword("user retrieves manufacturer listing")
    def user_retrieves_manufacturer_listing(self):
        url = "{0}trade-asset/asset-manufacturer".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${manu_ls}", response.json())
        return str(response.status_code), response.json()

    @keyword("user retrieves manufacturer details")
    def user_retrieves_manufacturer_details(self):
        manu_id = BuiltIn().get_variable_value("${manu_id}")
        if not manu_id:
            self.user_retrieves_manufacturer_listing()
            manu_ls = BuiltIn().get_variable_value("${manu_ls}")
            rand_manu = secrets.choice(manu_ls)
            manu_id = rand_manu['ID']

        url = "{0}trade-asset/asset-manufacturer/{1}".format(END_POINT_URL, manu_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${manu_details}", response.json())
        return str(response.status_code), response.json()
