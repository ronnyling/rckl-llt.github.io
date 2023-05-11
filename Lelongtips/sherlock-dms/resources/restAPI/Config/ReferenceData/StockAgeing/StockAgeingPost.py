from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import secrets
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL
MODULE = "aging-period"


class StockAgeingPost(object):

    @keyword('user creates valid aging period by random data')
    def user_creates_valid_aging_period_by_random_data(self):
        my_token = BuiltIn().get_variable_value("${token}")
        print(my_token)
        url = "{0}aging-period".format(END_POINT_URL)
        payload = self.payload_ageing_period()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response)
        print("POST Status code for Aging Period: " + str(response.status_code))
        print("response text= " + response.text)
        if "PERIOD_DESC" in response.text:
            data = response.json()
            print(json.dumps(data, indent=4))
            age_id = data["ID"]
            age_code = data["PERIOD_CD"]
            age_desc = data["PERIOD_DESC"]
            BuiltIn().set_test_variable("${AgingPeriodID}", age_id)
            BuiltIn().set_test_variable("${AgingPeriodCode}", age_code)
            BuiltIn().set_test_variable("${AgingPeriodDesc}", age_desc)
            print("Reponse: " + str(response.status_code))
            print(age_id, age_desc, age_code)
        BuiltIn().set_test_variable("${status_code}", str(response.status_code))

    def payload_ageing_period(self):
        payload = {
            'PERIOD_CD': ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(20)),
            'PERIOD_DESC': ''.join(secrets.choice('ABCDEFGHIJKLMNOPqrstuvwxyz1234567890@#$%^&*()') for _ in range(50))
        }
        print("payload before: ", payload)
        details = BuiltIn().get_variable_value("&{aging_period_details}")
        print(details)
        if details:
            payload.update((k, v) for k, v in details.items())
        print("Payload after: ", payload)
        payload = json.dumps(payload)
        return payload
