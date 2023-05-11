from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.Merchandising.MerchandisingSetup.StoreSpace import StoreSpacePost

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL

class StoreSpacePut(object):
    STORE_SPACE_DETAILS="${store_space_details}"
    STORE_ID = "${res_bd_store_space_id}"

    @keyword('user updates store space with ${data_type} data')
    def user_updates_store_space_with(self, data_type):
        res_bd_store_space_id = BuiltIn().get_variable_value("${res_bd_store_space_id}")
        url = "{0}merchandising/merc-store-space/{1}".format(END_POINT_URL, res_bd_store_space_id)
        payload = StoreSpacePost.StoreSpacePost().payload_store(data_type)
        details = BuiltIn().get_variable_value(self.STORE_SPACE_DETAILS)
        if details:
            payload.update((k, v) for k, v in details.items())
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)


