from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn

PROMO_END_POINT_URL = PROTOCOL + "promotion" + APP_URL


class PromoGet(object):

    PROMO_ID = "${promo_id}"

    @keyword('user retrieves promotion by id')
    def get_promotion(self):
        promo_id = BuiltIn().get_variable_value(self.PROMO_ID)
        url = "{0}promotion/{1}".format(PROMO_END_POINT_URL, promo_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${promo_response}", body_result)
            promotion_id = body_result['ID']
            assert promotion_id == promo_id, "Retrieved wrong promotion"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return body_result
