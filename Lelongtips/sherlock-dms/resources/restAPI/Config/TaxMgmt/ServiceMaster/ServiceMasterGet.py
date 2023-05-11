from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json

END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class ServiceMasterGet(object):

    @keyword('user retrieves ${cond} service master')
    def user_get_service_master(self, cond):
        if cond == 'all':
            url = "{0}sac-master".format(END_POINT_URL)
        else:
            sac_id = BuiltIn().get_variable_value("${sac_id}")
            url = "{0}sac-master/{1}".format(END_POINT_URL, sac_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_get_service_master_by_code(self, svc_cd):
        filter_ts = {"SVC_CD": {"$eq": svc_cd}}
        filter_ts = json.dumps(filter_ts)
        url = "{0}sac-master?filter={1}".format(END_POINT_URL, filter_ts)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        assert response.status_code == 200, "Unable to retrieve service"
        body_result = response.json()[0]
        return body_result

    def user_get_service_master_by_service_code_cd(self, sac_cd):
        filter_ts = {"SAC_CD": {"$eq": sac_cd}}
        filter_ts = json.dumps(filter_ts)
        url = "{0}sac-master?filter={1}".format(END_POINT_URL, filter_ts)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        assert response.status_code == 200, "Unable to retrieve service"
        body_result = response.json()[0]
        return body_result
