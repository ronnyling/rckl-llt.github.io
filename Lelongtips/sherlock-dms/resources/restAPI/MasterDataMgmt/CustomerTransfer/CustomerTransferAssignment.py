from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
from resources.restAPI.MasterDataMgmt.Promo.PromoAssignPost import PromoAssignPost
from resources.restAPI.Config.AppSetup.GamificationGet import GamificationGet
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json

END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL


class CustomerTransferAssignment(object):

    @keyword('user assigns customer to created transfer')
    def user_assigns_customer_to_transfer(self):
        url = "{0}customer-transfer-assignment".format(END_POINT_URL)
        payload = self.assignment_payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, json.dumps(payload))
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def assignment_payload(self):
        transfer_id = BuiltIn().get_variable_value("${transfer_id}")
        assignment_details = BuiltIn().get_variable_value("${assignment_details}")
        geo_id = StructureGet().user_get_hierid_from_hierarchy_structure_name(assignment_details['GEO_TREE'])
        BuiltIn().set_test_variable("${geo_hier_id}", geo_id)
        geo_res = StructureGet().user_get_hierarchy_structure_node_details()[0]
        PromoAssignPost().get_geo_details_by_level_desc(assignment_details['FROM_NODE'], geo_res)
        from_node_id = BuiltIn().get_variable_value("${DISTCAT_VALUE_ID}")
        PromoAssignPost().get_geo_details_by_level_desc(assignment_details['TO_NODE'], geo_res)
        to_node_id = BuiltIn().get_variable_value("${DISTCAT_VALUE_ID}")
        cust_id = BuiltIn().get_variable_value("${res_bd_cust_id}")

        payload = [
            {
                "GEO_TREE_ID": geo_id,
                "CUST_ID": cust_id,
                "CUST_TRANSFER_ID": transfer_id,
                "TO_ROUTE_PLAN_ID": "",
                "FROM_ROUTE_PLAN_ID": "",
                "FROM_NODE_ID": from_node_id,
                "TO_NODE_ID": to_node_id
            }
        ]
        return payload
