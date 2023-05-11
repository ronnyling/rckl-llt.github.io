from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
import json
import datetime
NOW = datetime.datetime.now()
PROMO_END_POINT_URL = PROTOCOL + "promotion" + APP_URL

class PromoApprove(object):

    @keyword("Approve Promotion")
    def approve_promotion(self):
        promo_id = BuiltIn().get_variable_value("${promo_id}")
        approve_payload = self.approve_payload(promo_id)
        url = "{0}promotion/{1}/approve".format(PROMO_END_POINT_URL, promo_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, approve_payload)
        print("Response", response)
        assert response.status_code == 200, "Unable to Approve Promo"
        return response.status_code

    def approve_payload(self,promo_id):

        payload = {
            "ID": promo_id,
            "NOTES": None,
            "action": "update"
        }

        payload = json.dumps(payload)
        return payload

