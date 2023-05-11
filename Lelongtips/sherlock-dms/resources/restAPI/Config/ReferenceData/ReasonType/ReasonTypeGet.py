from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import TokenAccess, APIMethod
import json

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class ReasonTypeGet(object):
    """ Functions to retrieve reason type record """

    @keyword("user retrieves reason type '${reason_type}'")
    def user_retrieves_reason_type(self, reason_type):
        """ Functions to retrieve reason type id by using reason description """
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        filter_reason = {"REASON_TYPE_DESC":{"$eq":reason_type}}
        filter_reason = json.dumps(filter_reason)
        str(filter_reason).encode(encoding='UTF-8', errors='strict')
        url = "{0}module-data/setting-reasontype?filter={1}".format(END_POINT_URL, filter_reason)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve Reason Type"
        body_result = response.json()
        res_bd_reason_type_id = body_result[0]['ID']
        BuiltIn().set_test_variable("${res_bd_reason_type_id}", res_bd_reason_type_id)

    @keyword("user gets reason by using code '${reason_cd}' and '${reason_type}'")
    def user_gets_reason_by_using_code(self, reason_cd, reason_type):
        """ Functions to retrieve reason id & reason type by using reason code """
        self.user_retrieves_reason_type_by_code(reason_type)
        reason_type = BuiltIn().get_variable_value('${res_bd_reason_type_id}')
        filter_reason = {"REASON_CD":{"$eq":reason_cd}}
        filter_reason = json.dumps(filter_reason)
        str(filter_reason).encode(encoding='UTF-8', errors='strict')
        url = "{0}module-data/setting-reasontype/{1}/setting-reason?filter={2}".format(END_POINT_URL, reason_type, filter_reason)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve Reason "
        body_result = response.json()
        reason_id = body_result[0]['ID']
        BuiltIn().set_test_variable("${res_bd_reason_id}", reason_id)
        BuiltIn().set_test_variable("${reason_cd}", reason_cd)
        return reason_id

    @keyword("user retrieves reason type by code: ${reason_type}")
    def user_retrieves_reason_type_by_code(self, code):
        """ Functions to retrieve reason type id by using reason description """
        filter_reason = {"REASON_TYPE_CD": {"$eq": code}}
        filter_reason = json.dumps(filter_reason)
        str(filter_reason).encode(encoding='UTF-8', errors='strict')
        url = "{0}module-data/setting-reasontype?filter={1}".format(END_POINT_URL, filter_reason)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve Reason Type"
        body_result = response.json()
        res_bd_reason_type_id = body_result[0]['ID']
        BuiltIn().set_test_variable("${res_bd_reason_type_id}", res_bd_reason_type_id)