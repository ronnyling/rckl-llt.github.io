from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
import json

PROMO_END_POINT_URL = PROTOCOL + "promotion" + APP_URL


class PromoBudgetGet(object):

    def user_gets_promotion_budget(self):
        promo_id = BuiltIn().get_variable_value("${promo_id}")
        url = "{0}promotion/{1}/budget".format(PROMO_END_POINT_URL, promo_id)
        payload = self.get_budget_payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        assert response.status_code == 200, "Unable to retrieve Promo Budget"
        body_result = response.json()
        print("Response result: ", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return body_result

    def get_budget_payload(self):
        payload = {
            "MODE": "edit"
        }
        payload = json.dumps(payload)
        return payload
