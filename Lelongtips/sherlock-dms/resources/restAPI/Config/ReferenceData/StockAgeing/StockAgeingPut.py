from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class StockAgeingPut(object):

    @keyword("user updates the created aging period")
    def user_updates_the_created_aging_period(self):
        aging_period_id = BuiltIn().get_variable_value("${AgingPeriodID}")
        url = "{0}aging-period/{1}".format(END_POINT_URL, aging_period_id)
        payload = self.payload_ageing_period()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response)
        print("PUT Status code for Aging Period: " + str(response.status_code))
        print("response text: " + response.text)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code

    def payload_ageing_period(self):
        aging_period_code = BuiltIn().get_variable_value("${AgingPeriodCode}")
        payload = {
            'PERIOD_CD': aging_period_code,
            'PERIOD_DESC': None
        }
        print("payload before: ", payload)
        details = BuiltIn().get_variable_value("&{aging_period_details_put}")
        print(details)
        if details:
            payload.update((k, v) for k, v in details.items())
        print("Payload after: ", payload)
        payload = json.dumps(payload)
        return payload