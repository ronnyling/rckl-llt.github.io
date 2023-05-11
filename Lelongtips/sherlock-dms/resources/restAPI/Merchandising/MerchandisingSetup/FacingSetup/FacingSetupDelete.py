from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
END_POINT_URL = PROTOCOL+"merchandising"+APP_URL

class FacingSetupDelete:

    def user_deletes_created_product_group(self):
        res_bd_prod_group_id = BuiltIn().get_variable_value("${res_bd_prod_group_id}")
        url = "{0}merchandising/merc-prod-group/{1}".format(END_POINT_URL, res_bd_prod_group_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        assert response.status_code == 200, "Facing Setup not deleted"