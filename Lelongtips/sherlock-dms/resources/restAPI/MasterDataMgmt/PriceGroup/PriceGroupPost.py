import json
import secrets

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "price" + APP_URL


class PriceGroupPost:

    @keyword("user creates price group with ${data_type} data")
    def user_creates_price_group(self, data_type):
        url = "{0}price".format(END_POINT_URL)
        payload = self.payload_pricegroup_general_info()
        payload = json.dumps(payload)
        print(payload)
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        print("POST Status code for price group general is " + str(response.status_code))
        print(response.text)
        if response.status_code != 201:
            return str(response.status_code), "", response.text
        else:
            body_result = response.json()
            print(body_result)
            BuiltIn().set_test_variable("${price_group_id}", body_result['ID'])
            BuiltIn().set_test_variable("${status_code}", response.status_code)
            return str(response.status_code)

    def payload_pricegroup_general_info(self):
        details = BuiltIn().get_variable_value("${price_group_details}")
        own_prod = secrets.choice([True, False])
        if own_prod is False:
            price_type = 'DirectPriceUpload'
        else:
            price_type = secrets.choice(['DirectPriceUpload', 'Derived', 'Integration'])
        payload = {
            'PRICE_GRP_CD': ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
            'PRICE_GRP_DESC': ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(50)),
            'PRICE_IS_DEFAULT': False,
            'PRICE_STATUS': secrets.choice([True, False]),
            'PRICE_LOB': None,
            'BATCH_MANAGED': secrets.choice([True, False]),
            'PRICE_TYPE': price_type,
            'PICK_DEF_PRC_GRP': secrets.choice([True, False]),
            'DEF_PRC_GRP': ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
            "OWN_PROD": True,
            "PRIME_FLAG": secrets.choice(["NON_PRIME"])
        }
        if details:
            payload.update((k, v) for k, v in details.items())
        if payload["PRIME_FLAG"] == "NON_PRIME":
            payload["PRICE_TYPE"] = secrets.choice(['DirectPriceUpload', 'Derived'])
        return payload
