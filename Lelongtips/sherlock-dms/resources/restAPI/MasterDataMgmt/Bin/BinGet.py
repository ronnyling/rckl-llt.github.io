import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "setting" + APP_URL

class BinGet(object):

    @keyword('user retrieves all bin data')
    def user_retrieves_all_bin(self):
        url = "{0}warehouse-bin".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${whs_bin_list}", response.json())
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves bin by using ${type} id')
    def user_gets_bin_by_id(self, type):
        if type == "valid":
            res_bd_bin_id = BuiltIn().get_variable_value("${res_bd_bin_id}")
        else:
            res_bd_bin_id = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45))
        url = "{0}warehouse-bin/{1}".format(END_POINT_URL, res_bd_bin_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_bin_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)
