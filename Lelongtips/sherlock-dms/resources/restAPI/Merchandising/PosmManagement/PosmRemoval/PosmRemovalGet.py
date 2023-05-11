from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "posm-management" + APP_URL
DT_FORMAT = "%Y-%m-%dT00:00:00.000Z"

class PosmRemovalGet(object):

    @keyword('user retrieves ${cond} posm removal')
    def user_retrieves_all_posm_removal(self, cond):
        if cond == "all":
            url = "{0}posm-removal".format(END_POINT_URL)
        else:
            posm_removal_id = BuiltIn().get_variable_value("${direct_removal_id}")
            url = "{0}posm-removal/{1}".format(END_POINT_URL, posm_removal_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)