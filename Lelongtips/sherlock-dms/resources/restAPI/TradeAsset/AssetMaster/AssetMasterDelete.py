from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class AssetMasterDelete(object):
    @keyword("user deletes asset master")
    def user_deletes_asset_master(self):
        am_id = BuiltIn().get_variable_value("${am_id}")
        url = "{0}trade-asset/asset-master/{1}".format(END_POINT_URL, am_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code), response.json()
