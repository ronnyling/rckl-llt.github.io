from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn


PROMO_END_POINT_URL = PROTOCOL + "promotion" + APP_URL


class PromoDelete(object):

    def user_deletes_promotion(self):
        promo_id = BuiltIn().get_variable_value("${promo_id}")
        url = "{0}promotion/{1}".format(PROMO_END_POINT_URL, promo_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, '')
        body_result = response.json()
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        print("Delete promotion respond:", body_result)