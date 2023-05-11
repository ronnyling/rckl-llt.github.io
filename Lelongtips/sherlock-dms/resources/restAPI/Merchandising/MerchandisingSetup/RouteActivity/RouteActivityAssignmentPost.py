import json
import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.AppSetup.GamificationGet import GamificationGet
from resources.restAPI.MasterDataMgmt.Promo.PromoAssignPost import PromoAssignPost
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

CODETABLE_END_POINT_URL = PROTOCOL + "codetable" + APP_URL
END_POINT_URL = PROTOCOL + "merchandising" + APP_URL
TRANSACTION_END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class RouteActivityAssignmentPost(object):

    @keyword('user add activity assignment for route activity')
    def add_assignment(self):
        activity_id = BuiltIn().get_variable_value("${res_bd_route_activity_id}")
        payload = self.assignment_payload()
        transaction_id = self.get_transaction_id()
        BuiltIn().set_test_variable("${transaction_id}", transaction_id)
        url = "{0}merchandising/merc-route-activity/{1}/transaction-list/{2}/merc-cust-assignment".\
            format(END_POINT_URL, activity_id, transaction_id)
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("Body Result: ", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def get_visit_frequency(self):
        url = "{0}codetable/VISIT_FREQUENCY".format(CODETABLE_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        body_result = response.json()
        visit_freq = secrets.choice(list(body_result))
        return visit_freq

    def get_tree_and_node_id(self):
        StructureGet().user_get_hierid_from_hierarchy_structure_name("General Customer Hierarchy")
        hier_structure_details = StructureGet().user_get_hierarchy_structure_info_by_hierarchy_id()
        tree_id = hier_structure_details['levels'][1]['treeId']
        BuiltIn().set_test_variable("${tree_id}", tree_id)
        cust_hier_info = StructureGet().user_get_prd_or_or_cust_hierearchy_info()
        random_cust_hier = secrets.choice(list(cust_hier_info))
        node_id = random_cust_hier['nodeId']
        BuiltIn().set_test_variable("${node_id}", node_id)

    def get_transaction_id(self):
        url = TRANSACTION_END_POINT_URL + "module-data/transaction-list?filter={%22MERC_IND%22:{%22$eq%22:%22true%22}}"
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        body_result = response.json()
        rand_txn = secrets.choice(list(body_result))
        return rand_txn['ID']

    def assignment_payload(self):
        self.get_tree_and_node_id()
        payload = [
            {
                "LEVEL_ID": BuiltIn().get_variable_value("${tree_id}"),
                "CUST_GROUP_ID": BuiltIn().get_variable_value("${node_id}"),
                "VISIT_FREQUENCY": self.get_visit_frequency(),
                "DURATION": secrets.randbelow(100)
            }
        ]
        payload = json.dumps(payload)
        return payload

    @keyword('user assigns route activity to all route under Level:${Level}, Node:${Node}')
    def user_creates_route_activity_assignment(self, level, node):
        activity_id = BuiltIn().get_variable_value("${res_bd_route_activity_id}")
        payload = self.route_assignment_payload(level, node)
        print("payload is = ", payload)
        url = "{0}merchandising/merc-route-activity/{1}/merc-dist-route-assign". \
            format(END_POINT_URL, activity_id)
        print("url is = ", url)
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("response", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def route_assignment_payload(self, level, node):
        GamificationGet().user_retrieves_option_values_geo_level_leaderboard(level)
        geo_res = StructureGet().user_get_hierarchy_structure_node_details()[0]
        PromoAssignPost().get_geo_details_by_level_desc(node, geo_res)
        ass_entity_id = BuiltIn().get_variable_value("${DISTCAT_ID}")
        ass_entity_value_id = BuiltIn().get_variable_value("${DISTCAT_VALUE_ID}")
        payload = {
            "DIST_ASSIGN": {
                "RA_ASS_HDR": {
                    "ASS_ALL": False
                },
                "RA_ASS_DTL": [{
                    "ASS_ENTITY_ID": ass_entity_id,
                    "ASS_ENTITY_VALUE_ID": ass_entity_value_id
                }]
            },
            "DIST_EXCLUDE": [],
            "ROUTE_ASSIGN": {
                "RA_ASS_HDR": {
                    "ASS_ALL": True
                },
                "RA_ASS_DTL": []
            }
        }
        payload = json.dumps(payload)
        return payload

