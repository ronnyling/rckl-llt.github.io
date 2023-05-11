import secrets

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ModelGet(object):

    @keyword("user retrieves model listing")
    def user_retrieves_manufacturer_listing(self):
        url = "{0}trade-asset/asset-model".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${model_ls}", response.json())
        return str(response.status_code), response.json()

    @keyword("user retrieves model details")
    def user_retrieves_manufacturer_details(self):
        model_id = BuiltIn().get_variable_value("${model_id}")
        if not model_id:
            self.user_retrieves_manufacturer_listing()
            model_ls = BuiltIn().get_variable_value("${model_ls}")
            rand_model = secrets.choice(model_ls)
            model_id = rand_model['ID']

        url = "{0}trade-asset/asset-model/{1}".format(END_POINT_URL, model_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${model_details}", response.json())
        return str(response.status_code), response.json()
