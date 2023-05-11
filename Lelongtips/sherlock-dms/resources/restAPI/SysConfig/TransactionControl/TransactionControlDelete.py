from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common.APIMethod import APIMethod
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL
module1 = "configure-transaction-control"

class TransactionControlDelete(object):

    @keyword('user deletes created transaction control')
    def user_deletes_created_transaction_control(self):
        transaction_id = BuiltIn().get_variable_value("${transaction_id}")
        url = "{0}setting-routetransactioncontrol/{1}/{2}".format(END_POINT_URL, module1, transaction_id)
        print("Delete url :", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
