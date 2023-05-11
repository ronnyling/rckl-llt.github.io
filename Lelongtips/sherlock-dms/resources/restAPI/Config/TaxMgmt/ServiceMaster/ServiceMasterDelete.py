from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class ServiceMasterDelete(object):

    @keyword('user deletes ${con} service master')
    def user_del_service_master(self, cond):
        sac_id = BuiltIn().get_variable_value("${sac_id}")
        url = "{0}sac-master/{1}".format(END_POINT_URL, sac_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)


