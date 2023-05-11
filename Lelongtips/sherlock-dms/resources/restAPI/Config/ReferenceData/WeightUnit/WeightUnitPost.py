from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import secrets
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class WeightUnitPost(object):

    @keyword('user creates ${status} weight unit with ${data_type} data')
    def user_creates_weight_unit_with_data(self, status, data_type):
        url = "{0}module-data/weight-unit".format(END_POINT_URL)
        payload = self.payload_weight()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            response_dict = json.loads(response.text)
            print("Result: ", response_dict)
            BuiltIn().set_test_variable("${weight_id}", response_dict['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return payload

    def payload_weight(self):    #make use of random string values with specified word limit,
        # will be replaced by data from &{weight_unit_details} if it is not null
        payload = \
            {

                'WEIGHT_CD': ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                'WEIGHT_DESC': ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
                'CONV_FACTOR_KG': secrets.choice(range(1, 360))
            }

        details = BuiltIn().get_variable_value("&{weight_unit_details}")
        if details:
            payload.update((k, v) for k, v in details.items())

        payload = json.dumps(payload)
        BuiltIn().set_test_variable("${payload}", payload)
        print("Weight Unit Payload: ", payload)
        return payload
