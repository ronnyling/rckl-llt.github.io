from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
from resources.restAPI.Config.Attribute.AttributeValueSetup.AttributeValueSetupGet import AttributeValueSetupGet
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json

from resources.restAPI.Merchandising.MerchandisingSetup.PosmFocusCustomers.PosmFocusCustomersGet import \
    PosmFocusCustomersGet
from resources.restAPI.SysConfig.Attribute.AttributeModule.AttributeModuleGet import AttributeModuleGet

HIER_END_POINT_URL = PROTOCOL + "dynamic-hierarchy" + APP_URL
END_POINT_URL = PROTOCOL + "posm-management" + APP_URL


class PosmFocusCustomersPost(object):

    def get_tree_id_by_tree_name(self, hier_id, tree_name):
        url = "{0}structure/hier/{1}".format(HIER_END_POINT_URL, hier_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            level = body_result['levels']
            for x in level:
                if x['name'] == tree_name:
                    tree_id = x['treeId']
        return tree_id

    def gen_posm_cust_payload(self):
        PosmFocusCustomersGet().user_retrieves_posm_focus_customers()
        posm_cust_all = BuiltIn().get_variable_value("${posm_cust_all}")
        existing_cust_attr = [[i['CUST_NODE_ID'], i['POSM_ATTR_PRD_ID']] for i in posm_cust_all]
        BuiltIn().set_test_variable("${hier_id}", "5E306ADB:FD4E645E-8C4A-4071-AD96-AF031651EA9C")
        BuiltIn().set_test_variable("${tree_id}", "C209B33D:59E48E0C-E012-47C8-93C6-E2AAD0D9C914")
        StructureGet().user_get_prd_or_or_cust_hierearchy_info()
        tree_view_bd = BuiltIn().get_variable_value("${tree_view_bd}")
        cust_node_ids = []
        for node in tree_view_bd:
            if node['children'] and len(node['children']) > 0:
                for child in node['children']:
                    cust_node_ids.append(child['nodeId'])

        AttributeModuleGet().user_retrieves_all_attribute_module()
        atr_all = BuiltIn().get_variable_value("${atr_all}")
        posm_attr_id = next((i['ID']for i in atr_all if i['MODULE'] == "POSM Products"), None)

        PosmFocusCustomersGet().user_retrieve_dynamic_attribute()
        dyn_attr_ls = BuiltIn().get_variable_value("${dyn_attr_ls}")
        attr_for_posm_lvl_ids = [i['ID'] for i in dyn_attr_ls if i['MODULE'] == posm_attr_id]

        PosmFocusCustomersGet().user_retrieve_attribute_value_creation()
        attr_val_ls = BuiltIn().get_variable_value("${attr_val_ls}")
        assignment_found = None
        for cust_node in cust_node_ids:
            for i in attr_for_posm_lvl_ids:
                assignment_found = next((j['ID'] for j in attr_val_ls if j['ATTRIBUTE'] == i), None)
                if assignment_found is not None:
                    existing_attr_ids = [i[1] for i in existing_cust_attr if i[0] == cust_node]
                    if assignment_found not in existing_attr_ids:
                        PosmFocusCustomersGet().user_retrieves_posm_focus_customers_by_id(cust_node)
                        posm_cust_details = BuiltIn().get_variable_value("${posm_cust_details}")
                        assigned_cust_posm = [i['POSM_ATTR_PRD_ID'] for i in posm_cust_details]
                        if assignment_found not in assigned_cust_posm:
                            posm_lvl_id = i
                            posm_attr_prd_id = assignment_found
                            cust_node_id = cust_node
                            break
            if assignment_found is not None:
                break

        payload = [
            {
                "POSM_ATTR_PRD_ID": posm_attr_prd_id,
                "CUST_NODE_ID": cust_node_id,
                "POSM_LVL_ID": posm_lvl_id
            }
        ]
        return payload

    @keyword('user adds posm focus customers using ${data} data')
    def user_adds_posm_focus_customers(self, data):
        payload = self.gen_posm_cust_payload()
        url = "{0}posm-focused-customers-assignment".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${bd_res}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
