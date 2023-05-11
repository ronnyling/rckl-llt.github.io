from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "price" + APP_URL


class PriceGroupDelete:

    def user_deletes_price_group(self):
        pg_id = BuiltIn().get_variable_value("${price_group_id}")
        url = "{0}price/{1}".format(END_POINT_URL, pg_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        assert response.status_code == 200, "Unable to delete price group"
        print(response.status_code)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
