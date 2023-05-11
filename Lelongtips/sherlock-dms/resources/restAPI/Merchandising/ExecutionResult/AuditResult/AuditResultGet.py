from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import secrets

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class AuditResultGet(object):

    @keyword('user retrieves all audit result for ${audit_type}')
    def user_retrieves_all_audit_result(self, audit_type):
        txn_type = self.retrieve_endpoint_based_on_type(audit_type)
        url = "{0}merchandising/{1}".format(END_POINT_URL, txn_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            if len(body_result) > 1:
                rand_so = secrets.randbelow(len(body_result))
            else:
                rand_so = 0
            BuiltIn().set_test_variable("${rand_audit_id}", body_result[rand_so]["ID"])
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable("${audit_res_bd}", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves audit result for ${audit_type} by id')
    def user_retrieves_audit_result_by_id(self, audit_type):
        audit_id = BuiltIn().get_variable_value("${rand_audit_id}")
        txn_type = self.retrieve_endpoint_based_on_type(audit_type)
        url = "{0}merchandising/{1}/{2}".format(END_POINT_URL, txn_type, audit_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${audit_details}", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def retrieve_endpoint_based_on_type(self, audit_type):
        if audit_type == 'facing audit':
            txn_type = 'txn-merc-facing'
        elif audit_type == 'price audit':
            txn_type = 'txn-merc-price-audit'
        elif audit_type == 'distribution check':
            txn_type = 'txn-merc-dist-check'
        elif audit_type == 'promo compliance':
            txn_type = 'txn-merc-promotion-complaince'
        return txn_type
