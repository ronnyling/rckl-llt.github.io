from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import secrets

from setup.yaml import YamlDataManipulator

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL
METADATA_END_POINT_URL = PROTOCOL + "metadata" + APP_URL

ENV_DETAILS = YamlDataManipulator.YamlDataManipulator().user_retrieves_data_from_yaml("loginCredential.yaml",
                                                                                BuiltIn().get_variable_value("${ENV}"))


class AuditGet(object):

    @keyword('user retrieves all audit setup')
    def user_retrieves_all_audit_setup(self):
        url = "{0}merchandising/merc-general-info".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable("${audit_res_bd}", body_result)
            if len(body_result) > 1:
                rand_so = secrets.choice(body_result)
            else:
                rand_so = 0
            BuiltIn().set_test_variable("${rand_audit_id}", rand_so["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves audit setup by id')
    def user_retrieves_audit_by_id(self):
        user_type = "hqadm"
        username = ENV_DETAILS['Credential'][user_type].get('Username')
        self.user_retrieves_all_audit_setup()
        audit_res_bd = BuiltIn().get_variable_value("${audit_res_bd}")
        user_audit = [i for i in audit_res_bd if i['CREATED_BY'] == username]
        rand_audit = secrets.choice(user_audit)
        rand_audit_id = rand_audit['ID']
        url = "{0}merchandising/merc-general-info/{1}".format(END_POINT_URL, rand_audit_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${audit_details}", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_prod(self):
        attribute_id = BuiltIn().get_variable_value("${res_bd_node_id}")
        url = "{0}merchandising/merc-prod-group/".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
            for item in body_result:
                if item["PRDCAT_VALUE_ID"] == attribute_id:
                    BuiltIn().set_test_variable("${brand_id}",item["ID"])
                break
            BuiltIn().set_test_variable("${audit_details}", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
