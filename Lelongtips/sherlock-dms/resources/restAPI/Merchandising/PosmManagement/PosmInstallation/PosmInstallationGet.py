from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "posm-management" + APP_URL
DT_FORMAT = "%Y-%m-%dT00:00:00.000Z"


class PosmInstallationGet(object):

    @keyword('user retrieves ${cond} posm installation')
    def user_retrieves_posm_installation(self, cond):
        if cond == "all":
            url = "{0}posm-new-installation".format(END_POINT_URL)
        else:
            posm_install_id = BuiltIn().get_variable_value("${direct_install_id}")
            url = "{0}posm-new-installation/{1}".format(END_POINT_URL,posm_install_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)