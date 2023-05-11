from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import secrets
END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class WeightUnitPut(object):

    @keyword("user updates the created Weight Unit")
    def user_updates_the_created_weight_unit(self):
        weight_id = BuiltIn().get_variable_value("${WeightID}")
        url = "{0}module-data/weight-unit/{1}".format(END_POINT_URL, weight_id)
        payload = self.payload_weight()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response)
        print("PUT Status code for Weight Unit: " + str(response.status_code))
        print("response text: " + response.text)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code

    def payload_weight(self):
        payload = \
        {
            'WEIGHT_CD': ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            'WEIGHT_DESC': ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
            'CONV_FACTOR_KG': secrets.choice(range(1, 360))
        }
        print("payload before: ", payload)
        details = BuiltIn().get_variable_value("&{weight_unit_details_put}")
        print(details)
        if details:
            payload.update((k, v) for k, v in details.items())
        print("Payload after: ", payload)
        payload = json.dumps(payload)
        return payload
