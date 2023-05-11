from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json


END_POINT_URL = PROTOCOL + "setting" + APP_URL
METADATA_END_POINT_URL = PROTOCOL + "metadata" + APP_URL

class WorkFlowGet(object):
    WORK_FLOW = "${work_flow_id}"

    def user_retrieves_work_flow_by_code(self, code):
        work_flow_filter = {"WF_CODE": {"$eq": code}}
        work_flow_filter = json.dumps(work_flow_filter)
        url = "{0}module-data/workflow-configuration?filter={1}".format(METADATA_END_POINT_URL, work_flow_filter)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve work flow"
        body_result = response.json()
        work_flow_id = body_result[0]['ID']
        BuiltIn().set_test_variable("${work_flow_res_bd}", body_result[0])
        BuiltIn().set_test_variable(self.WORK_FLOW, work_flow_id)
        return work_flow_id

    def user_retrieves_work_flow(self, cond):
        if cond == "all":
            url = "{0}workflow-configuration".format(END_POINT_URL)
        else:
            work_flow_id = BuiltIn().get_variable_value(self.WORK_FLOW)
            url = "{0}workflow-configuration/{1}".format(END_POINT_URL, work_flow_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve work flow"
        body_result = response.json()
        work_flow_id = body_result['ID']
        BuiltIn().set_test_variable("${work_flow_res_bd}", body_result)
        BuiltIn().set_test_variable(self.WORK_FLOW, work_flow_id)
