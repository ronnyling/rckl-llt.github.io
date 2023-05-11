from resources.restAPI import PROTOCOL, APP_URL
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod, TokenAccess
from resources.restAPI.SysConfig.Maintenance.WorkFlow.WorkFlowGet import WorkFlowGet
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
from robot.libraries.BuiltIn import BuiltIn
import json


END_POINT_URL = PROTOCOL + "setting" + APP_URL


class WorkFlowPut(object):

    @keyword("user updates ${wf_code} workflow to Auto:${on_or_off}, Hierarchy:${hier} , Level:${lvl}")
    def user_updates_work_flow(self, code, cond, hierarchy, level):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("sysimp")
        WorkFlowGet().user_retrieves_work_flow_by_code(code)
        WorkFlowGet().user_retrieves_work_flow("id")
        work_flow_id = BuiltIn().get_variable_value("${work_flow_id}")
        url = "{0}workflow-configuration/{1}".format(END_POINT_URL, work_flow_id)
        common = APIMethod.APIMethod()
        payload = self.user_set_work_flow_as_auto_or_manual(cond, hierarchy, level)
        print("yoyo", payload)
        response = common.trigger_api_request("PUT", url, payload)
        assert response.status_code == 200, "Unable to update work flow"

    def user_set_work_flow_as_auto_or_manual(self, on_or_off, hierarchy, level):
        payload = self.work_flow_payload(on_or_off, hierarchy, level)
        payload = json.dumps(payload)
        return payload


    def work_flow_payload(self, cond, hierarchy, level):

        if cond == "on":
            payload = {
                "APPROVE_USER": None,
                "APPROVE_USER_LENGTH": 1,
                "AUTO_APPROVE": "Y",
            }
        else:
            StructureGet().user_get_hierid_from_hierarchy_structure_name(hierarchy)
            StructureGet().user_get_hierarchy_structure_info_by_hierarchy_id()
            response_dict = BuiltIn().get_variable_value("${response_dict}")
            print("res dict = ", response_dict)
            work_flow_res_bd = BuiltIn().get_variable_value("${work_flow_res_bd}")
            wf_bussiness_rule = work_flow_res_bd['WORKFLOW-BUSINESS-RULE'][0]
            for item in response_dict['levels']:
                if item['name'] == level:
                    level_id = item['treeId']
            payload = {

                "APPROVE_USER": [
                                    {
                                        "APPROVAL_SEQ":"1",
                                        "HIER_TYPE":response_dict['hierStruct'],
                                        "HIER_DESC":response_dict['hierId'],
                                        "LEVEL": level_id
                                    }
                                 ],
                "AUTO_APPROVE": "N",
            }
        wf_bussiness_rule.update((k, v) for k, v in payload.items())
        return work_flow_res_bd