from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import secrets
import json
import ast
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class DimensionUnitPost(object):

    @keyword('user creates ${status} dimension unit with ${data_type} data')
    def user_creates_dimension_unit_with_data(self, status, data_type):
        url = "{0}module-data/dimension-unit".format(END_POINT_URL)
        payload = self.payload_dimension()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            response_dict = json.loads(response.text)
            print("Result: ", response_dict)
            BuiltIn().set_test_variable("${dimension_id}", response_dict['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return payload

    def payload_dimension(self):    #make use of random string values with specified word limit,
        # will be replaced by data from &{dimension_unit_details} if it is not null
        payload = \
            {

                'DIMENSION_CD': ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                'DIMENSION_DESC': ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
                'CONV_FACTOR_M': secrets.choice(range(1, 360))
            }

        details = BuiltIn().get_variable_value("&{dimension_unit_details}")
        if details:
            payload.update((k, v) for k, v in details.items())

        payload = json.dumps(payload)
        BuiltIn().set_test_variable("${payload}", payload)
        print("Dimension Unit Payload: ", payload)
        return payload
