from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class PromoPriorityGet(object):

    def user_retrieves_all_promotion_sequence(self):
        url = "{0}promotion-sequence".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            promo_priority = response.json()[0]['PROMO_PRIORITY']
            BuiltIn().set_test_variable('${promo_priority}', promo_priority)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_promotion_sequence_by_id(self):
        sequence_id = BuiltIn().get_variable_value("${sequence_id}")
        url = "{0}promotion-sequence/{1}".format(END_POINT_URL, sequence_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            promo_seq_cd = response.json()['PROMO_SEQ_CD']
            assert BuiltIn().get_variable_value("${promo_seq_cd}") == promo_seq_cd, "Promo sequence retrieved incorrectly"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
