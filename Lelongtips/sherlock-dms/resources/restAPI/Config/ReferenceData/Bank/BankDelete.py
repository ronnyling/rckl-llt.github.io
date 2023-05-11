from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class BankDelete(object):

    @keyword('user deletes created bank')
    def user_deletes_bank(self):
        bank_id = BuiltIn().get_variable_value("${bank_id}")
        url = "{0}bank/{1}".format(END_POINT_URL, bank_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
