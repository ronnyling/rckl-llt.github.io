import json

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import secrets

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ChecklistResultGet(object):
    CHECKLIST_ID = "${rand_checklist_id}"

    @keyword('user retrieves all checklist results')
    def user_retrieves_all_checklist_result(self):
        url = "{0}merchandising/txn-merc-checklist-result".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            if len(body_result) > 1:
                rand_so = secrets.randbelow(len(body_result))
            else:
                rand_so = 0
            BuiltIn().set_test_variable(self.CHECKLIST_ID, body_result[rand_so]["ID"])
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable("${checklist_res_bd}", body_result)
            print(body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves checklist with status ${status}')
    def user_retrieves_checklist_with_status(self,status):
        filter_status = {"STATUS_DESC": {"$lk": status}}
        filter_status = json.dumps(filter_status)
        url = "{0}merchandising/txn-merc-checklist-result/?filter=[{1}]".format(END_POINT_URL, filter_status)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${checklist_res_bd}", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves checklist result by id')
    def user_retrieves_checklist_result_by_id(self):
        checklist_id = BuiltIn().get_variable_value("${rand_checklist_id}")
        url = "{0}merchandising/txn-merc-checklist-result/{1}".format(END_POINT_URL, checklist_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${checklist_details}", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves checklist activity details')
    def user_retrieves_checklist_activity_details(self):
        checklist_id = BuiltIn().get_variable_value(self.CHECKLIST_ID)
        url = "{0}merchandising/txn-merc-checklist-result/{1}/txn-merc-checklist-result-prd".format(END_POINT_URL, checklist_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${checklist_details}", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

