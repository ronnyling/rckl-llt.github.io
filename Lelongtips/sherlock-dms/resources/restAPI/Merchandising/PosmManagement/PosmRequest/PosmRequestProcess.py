from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Config.ReferenceData.ReasonType import ReasonTypeGet
from resources.restAPI.TaskList.TaskListPost import TaskListPost
import json

END_POINT_URL = PROTOCOL + "posm-management" + APP_URL
WORKFLOW_END_POINT_URL = PROTOCOL + "workflow" + APP_URL


class PosmRequestProcess(object):

    @keyword('user ${action} posm request')
    def user_approve_posm_request(self, action):
        request_id = BuiltIn().get_variable_value("${request_id}")
        task_id = self.get_request()
        TaskListPost().claim_workflow_task(task_id)
        if action == "rejects":
            url = "{0}posm-request/action/reject".format(END_POINT_URL)
            payload = self.reject_payload(request_id)
        else:
            url = "{0}posm-request/action/SAVE_AND_APPROVE/{1}".format(END_POINT_URL, request_id)
            payload = BuiltIn().get_variable_value("${request_payload}")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, json.dumps(payload))
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${request_no}", body_result[0]['TXN_NO'])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def get_request(self):
        url = "{0}task".format(WORKFLOW_END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            task_id = body_result[0]['ID']
            print("200 : ", task_id)
            BuiltIn().set_test_variable("${task_id}", task_id)

        print("Not 200 : ", task_id)
        return task_id

    def claim_request(self):
        task_id = BuiltIn().get_variable_value("${task_id}")
        url = "{0}task/{1}/claim".format(WORKFLOW_END_POINT_URL, task_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)

    def reject_payload(self, request_id):
        reject_details = BuiltIn().get_variable_value("${reject_details}")
        ReasonTypeGet.ReasonTypeGet().user_gets_reason_by_using_code(reject_details['REASON'], "POSM_REQ_REJ")
        reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        payload = {
            "TXN_IDS": [
                request_id
            ],
            "REJECT_REASON_ID": reason_id
        }
        return payload

