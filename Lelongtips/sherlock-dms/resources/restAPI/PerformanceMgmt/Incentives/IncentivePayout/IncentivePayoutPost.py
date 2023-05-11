import datetime
import json
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "performance" + APP_URL

class IncentivePayoutPost(object):
    @keyword('user posts for incentive payout')
    def user_posts_for_incentive_payout(self):
        url = "{0}incentives-with-payout".format(END_POINT_URL)
        payload = self.gen_inc_payout_payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, json.dumps(payload))
        print("payload = ", str(json.dumps(payload)))
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable('${inc_payout_br}', body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def gen_inc_payout_payload(self):
        next_month = (datetime.datetime.today() + datetime.timedelta(days=31))
        payload = {
            "YEAR": next_month.strftime('%Y'),
            "MTH_FROM": next_month.strftime('%m'),
            "MTH_TO": next_month.strftime('%m')
        }
        return payload
