import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL
PRFL_DIST_END_POINT_URL = PROTOCOL + "profile-dist" + APP_URL

class BinTransferGet(object):

    def user_retrieves_bin_transfer_listing(self):
        url = "{0}inventory-bin-transfer".format(INVT_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${bin_trsf_ls}", response.json())
        return response.status_code

    def user_retrieves_bin_transfer_details(self):
        bin_trsf_id = BuiltIn().get_variable_value("${bin_trsf_id}")
        if bin_trsf_id is None:
            self.user_retrieves_bin_transfer_listing()
            bin_trsf_ls = BuiltIn().get_variable_value("${bin_trsf_ls}")
            rand = secrets.choice(bin_trsf_ls)
            rand_bin_trsf_id = rand['TXN_ID']
            bin_trsf_id = rand_bin_trsf_id
            BuiltIn().set_test_variable("${bin_trsf_id}", bin_trsf_id)

        url = "{0}inventory-bin-transfer/{1}".format(INVT_END_POINT_URL, bin_trsf_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${bin_trsf_details}", response.json())
        print(response.status_code)
        return response.status_code
