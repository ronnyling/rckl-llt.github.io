import json
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "setting" + APP_URL

class BankPut(object):

    @keyword("user update created bank")
    def update_bank(self):
        bank_id = BuiltIn().get_variable_value("${bank_id}")
        url = "{0}bank/{1}".format(END_POINT_URL, bank_id)
        newdict = BuiltIn().get_variable_value("&{res_body}")
        details = BuiltIn().get_variable_value("${bank_update_details}")
        if details:
            newdict.update((k, v) for k, v in details.items())
        payload = json.dumps(newdict)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code
