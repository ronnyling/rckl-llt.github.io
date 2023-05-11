from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json

END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class HsnGet(object):

    @keyword('user retrieves ${cond} hsn')
    def user_get_hsn(self, cond):
        if cond == 'all':
            url = "{0}hsn-master".format(END_POINT_URL)
        else:
            sac_id = BuiltIn().get_variable_value("${sac_id}")
            url = "{0}hsn-master/{1}".format(END_POINT_URL, sac_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_get_hsn_by_code(self, hsn_cd):
        filter_ts = {"HSN_CODE": {"$eq": hsn_cd}}
        filter_ts = json.dumps(filter_ts)
        url = "{0}hsn-master?filter={1}".format(END_POINT_URL, filter_ts)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        assert response.status_code == 200, "Unable to retrieve hsn"
        body_result = response.json()[0]
        return body_result
