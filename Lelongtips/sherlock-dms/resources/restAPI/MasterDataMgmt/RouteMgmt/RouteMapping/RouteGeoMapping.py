import json, datetime
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import  APIMethod
from resources.restAPI.Config.AppSetup import GamificationGet
from resources.restAPI.MasterDataMgmt.Promo import PromoAssignPost
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
END_POINT_URL = PROTOCOL + "dynamic-hierarchy" + APP_URL

NOW = datetime.datetime.now()

class RouteGeoMapping(object):
    """ Functions to retrieve route record """
    ROUTE_ID = "${res_bd_route_id}"

    @keyword("user maps ${RouteORDist} to Level=${level}, Node=${node}")
    def user_map_route_to_geo_tree(self, route_or_dist, level, node):
        """ Function to retrieve all  available  route record """
        route_id = BuiltIn().get_variable_value(self.ROUTE_ID)
        url = "{0}{1}/{2}/nodes".format(END_POINT_URL, route_or_dist, route_id)
        payload = self.route_geo_mapping_payload(route_or_dist,level, node)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print("payload = " + str(payload))
        if response.status_code == 200:
            body_result = response.json()
            print("body_result = " + str(body_result))
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def route_geo_mapping_payload(self, route_or_dist, level, node):
        GamificationGet.GamificationGet().user_retrieves_option_values_geo_level_leaderboard(level)
        geo_res = StructureGet().user_get_hierarchy_structure_node_details()[0]
        PromoAssignPost.PromoAssignPost().get_geo_details_by_level_desc(node, geo_res)
        node_id = BuiltIn().get_variable_value("${DISTCAT_VALUE_ID}")
        if route_or_dist == 'route':
            st_date = str((NOW + datetime.timedelta(days=0)).strftime("%Y-%m-%d"))
            payload = [
                {
                    "NODE_ID": node_id,
                    "START_DATE": st_date,
                    "END_DATE": "2999-01-01"
                }
            ]
        else:
            dist_id = BuiltIn().get_variable_value("${distributor_id}")
            payload = [
                {
                  "NODE_ID": node_id,
                  "DIST_ID": dist_id
                }
            ]
        payload = json.dumps(payload)
        return payload






