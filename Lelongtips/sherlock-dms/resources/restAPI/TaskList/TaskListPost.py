from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL


END_POINT_URL = PROTOCOL + "workflow" + APP_URL


class TaskListPost(object):

    def claim_workflow_task(self, task_id):
        url = "{0}task/{1}/claim".format(END_POINT_URL, task_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)

    def release_workflow_task(self, task_id):
        url = "{0}task/{1}/release".format(END_POINT_URL, task_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)

