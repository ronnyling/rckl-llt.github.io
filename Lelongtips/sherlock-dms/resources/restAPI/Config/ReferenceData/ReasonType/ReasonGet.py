from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import secrets
from resources.Common import Common
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "setting" + APP_URL


class ReasonGet(object):
    REASON_TYPE_ID = "${res_bd_reason_type_id}"
    """ Functions to retrieve reason record """

    def user_retrieves_all_reasons(self):
        """ Function to retrieves all reason  """
        res_bd_reason_type_id = BuiltIn().get_variable_value(self.REASON_TYPE_ID)
        url = "{0}setting-reasontype/{1}/setting-reason".format(END_POINT_URL, res_bd_reason_type_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result), "", str(body_result))
            rand_id = secrets.choice(body_result)
            rand_reason = rand_id['ID']
            BuiltIn().set_test_variable("${rand_reason}", rand_reason)
            BuiltIn().set_test_variable("${rsn_ls}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword('user retrieves reason using ${type} id')
    def user_retrieves_reason_by_id(self,type):
        if type == "invalid":
            res_bd_reason_id = Common().generate_random_id("0")
        else:
            res_bd_reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        res_bd_reason_type_id = BuiltIn().get_variable_value(self.REASON_TYPE_ID)
        url = "{0}setting-reasontype/{1}/setting-reason/{2}".format(END_POINT_URL, res_bd_reason_type_id,res_bd_reason_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        body_result = None
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_reason_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return body_result

    def user_retrieves_all_reasons_for_all_operations(self):
        """ Function to retrieves all reason  """
        res_bd_reason_type_id = BuiltIn().get_variable_value(self.REASON_TYPE_ID)
        url = "{0}setting-reasontype/".format(END_POINT_URL, res_bd_reason_type_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable("${rsn_all_ops_ls}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
