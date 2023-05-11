import secrets
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.PerformanceMgmt.MustSellList import MustSellListPost

END_POINT_URL = PROTOCOL + "performance" + APP_URL

class MustSellListPut(object):
    
    @keyword('user updates created MSL with ${data_type} data')
    def user_updates_msl_with(self, data_type):
        if data_type == "invalid":
            res_bd_msl_id = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45))
        else:
            res_bd_msl_id = BuiltIn().get_variable_value("${res_bd_msl_id}")

        res_bd_msl_cd = BuiltIn().get_variable_value("${res_bd_msl_cd}")
        msl_details = BuiltIn().get_variable_value("${msl_details}")
        update_msl = {
            "ID": res_bd_msl_id,
            "MSL_CD": res_bd_msl_cd,
            "VERSION": 1
        }
        if msl_details is not None:
            msl_details.update(update_msl)
        else:
            msl_details = update_msl
        BuiltIn().set_test_variable("${msl_details}", msl_details)

        payload = MustSellListPost.MustSellListPost().payload_msl("put")
        url = "{0}msl/{1}".format(END_POINT_URL, res_bd_msl_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)