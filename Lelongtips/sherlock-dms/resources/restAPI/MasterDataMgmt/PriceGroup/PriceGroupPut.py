import json

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.PriceGroup import PriceGroupPost
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "price" + APP_URL


class PriceGroupPut:

    @keyword("user updates price group with ${data_type} data")
    def user_updates_price_group(self, data_type):
        pg_id = BuiltIn().get_variable_value("${price_group_id}")
        url = "{0}price/{1}".format(END_POINT_URL, pg_id)
        payload = PriceGroupPost.PriceGroupPost().payload_pricegroup_general_info()
        details = BuiltIn().get_variable_value("${update_price_group_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print(payload)
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        print(response.text)
        print("PUT Status code for updating the details for a given price group general is" + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code)