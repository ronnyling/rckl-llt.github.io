from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from robot.api.deco import keyword
import datetime
NOW = datetime.datetime.now()
PROMO_END_POINT_URL = PROTOCOL + "promotion" + APP_URL


class PromoAssignGet(object):

    @keyword("user retrieves data assigned to promotion")
    def get_assign_promotion(self):
        promo_id = BuiltIn().get_variable_value("${promo_id}")
        url = "{0}promotion/{1}/assignment".format(PROMO_END_POINT_URL, promo_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        print("Response", response)
        assert response.status_code == 200, "Unable to retrieve Promo Assignment"
        promo_assign_id = response.json()['ID']
        return response.status_code, promo_assign_id


