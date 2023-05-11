from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL
SETTING_END_POINT_URL = PROTOCOL + "setting" + APP_URL
MTDT_DIST_END_POINT_URL = PROTOCOL + "metadata" + APP_URL
PS_END_POINT_URL = PROTOCOL + "product-sector" + APP_URL


class VanReplenishmentDelete(object):
    def user_deletes_created_van_replenishment(self):
        van_rep_id = BuiltIn().get_variable_value("${van_rep_id}")
        url = "{0}van-replenishment/{1}".format(INVT_END_POINT_URL, van_rep_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code
