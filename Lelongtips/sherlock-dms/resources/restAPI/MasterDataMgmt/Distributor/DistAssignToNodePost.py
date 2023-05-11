from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.AppSetup import GamificationGet
from resources.restAPI.MasterDataMgmt.Promo import PromoAssignPost
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
import json

END_POINT_URL = PROTOCOL + "dynamic-hierarchy" + APP_URL


class DistAssignToNodePost(object):
    DIST_ID = "${distributor_id}"
    def user_assign_dist_to_node(self, level, node):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributor/{1}/nodes".format(END_POINT_URL, dist_id)
        common = APIMethod.APIMethod()
        self.dist_geo_node_id(level, node)
        payload = self.dist_assign_to_node_payload(dist_id)
        response = common.trigger_api_request("PUT", url, payload)
        print("payload", response.json())
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def dist_geo_node_id(self, level, node):
        GamificationGet.GamificationGet().user_retrieves_option_values_geo_level_leaderboard(level)
        geo_res = StructureGet().user_get_hierarchy_structure_node_details()[0]
        PromoAssignPost.PromoAssignPost().get_geo_details_by_level_desc(node, geo_res)

    def dist_assign_to_node_payload(self, dist_id):
        geo_id = BuiltIn().get_variable_value("${DISTCAT_VALUE_ID}")
        payload = [
            {
                "NODE_ID": geo_id,
                "DIST_ID": dist_id
            }
        ]
        payload = json.dumps(payload)
        return payload