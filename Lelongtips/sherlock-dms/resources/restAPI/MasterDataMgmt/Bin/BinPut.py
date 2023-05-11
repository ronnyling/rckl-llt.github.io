import secrets, json
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Bin import BinPost
END_POINT_URL = PROTOCOL + "setting" + APP_URL

class BinPut(object):

    @keyword('user updates bin with ${data_type} data')
    def user_updates_bin_with(self, data_type):
        res_bd_bin_id = BuiltIn().get_variable_value("${res_bd_bin_id}")
        res_bd_bin_cd = BuiltIn().get_variable_value("${res_bd_bin_cd}")
        bin_details = BuiltIn().get_variable_value("${bin_details}")
        update_bin = {
            "ID": res_bd_bin_id,
            "BIN_CODE": res_bd_bin_cd
        }
        if bin_details is not None:
            bin_details.update(update_bin)
        else:
            bin_details = update_bin
        BuiltIn().set_test_variable("${bin_details}", bin_details)
        payload = BinPost.BinPost().payload_bin()
        url = "{0}warehouse-bin/{1}".format(END_POINT_URL, res_bd_bin_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)


