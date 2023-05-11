from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class PosmFocusCustomersDelete(object):

    @keyword('user deletes posm focus customers')
    def user_deletes_posm_focus_customers(self):
        pfc_bd_res = BuiltIn().get_variable_value("${bd_res}")
        url = "{0}module-data/posm-focused-customers/{1}".format(END_POINT_URL, pfc_bd_res[0]['ID'])
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
