from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
END_POINT_URL = PROTOCOL+"merchandising"+APP_URL

class StoreSpaceDelete:
    STORE_ID = "${res_bd_store_space_id}"
    STORE_LEVEL_ID = "${res_bd_store_space_level_id}"
    def user_deletes_created_store_space(self):
        res_bd_store_space_id = BuiltIn().get_variable_value(self.STORE_ID)
        url = "{0}merchandising/merc-store-space/{1}".format(END_POINT_URL, res_bd_store_space_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        assert response.status_code == 200, "Store Space not deleted"

    def user_deletes_created_store_space_level(self):
        res_bd_store_space_id = BuiltIn().get_variable_value(self.STORE_ID)
        res_bd_store_space_level_id = BuiltIn().get_variable_value(self.STORE_LEVEL_ID)
        url = "{0}merchandising/merc-store-space/{1}/merc-store-space-level/{2}".format(END_POINT_URL, res_bd_store_space_id,res_bd_store_space_level_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        assert response.status_code == 200, "Store Space Level not deleted"