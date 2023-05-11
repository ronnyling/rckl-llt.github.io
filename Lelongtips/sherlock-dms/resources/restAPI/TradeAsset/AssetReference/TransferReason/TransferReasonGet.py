from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class TransferReasonGet(object):

    @keyword("user retrieves transfer reason listing")
    def user_retrieves_transfer_reason_listing(self):
        url = "{0}trade-asset/transfer-reason".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${tr_ls}", response.json())
        return str(response.status_code), response.json()
