from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class PromoPriorityDelete(object):

    def user_deletes_promotion_sequence(self,):
        sequence_id = BuiltIn().get_variable_value("${sequence_id}")
        url = "{0}promotion-sequence/{1}".format(END_POINT_URL, sequence_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
