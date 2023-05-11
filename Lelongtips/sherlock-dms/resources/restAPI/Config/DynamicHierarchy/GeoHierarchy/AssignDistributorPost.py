from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
import json
import datetime
from resources.restAPI.Config.AppSetup import GamificationGet
from resources.restAPI.MasterDataMgmt.Promo import PromoAssignPost
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet

END_POINT_URL = PROTOCOL + "dynamic-hierarchy" + APP_URL
HIER_ID = '5E306ADB:D11CA545-5DC8-4F11-B6D5-7A0594BEE179'
    # geo hierarchy automation is not done yet, so using hard coded for now


class AssignDistributorPost(object):
    """ Function to assign route/salesperson to geo tree """

    def user_add_dist_to_geotree(self):
        """ Function to assign route to geo tree """
        url = "{0}hierarchy/hier/{1}/sales/00/node/add".format(END_POINT_URL, HIER_ID)
        payload = self.payload_assign_distributor()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body_result = response.json()
        node_id = body_result['nodeId']
        BuiltIn().set_test_variable("${node_id}", node_id)



    def payload_assign_distributor(self):
        """ Function for geo tree assignment payload content """
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        node_id = BuiltIn().get_variable_value("${DISTCAT_VALUE_ID}")
        payload = {
            "parentId": node_id,
            "desc": dist_id,
            "roleId": "00"
        }
        payload = json.dumps(payload)
        print("Assigned Distributor Payload: ", payload)
        return payload

    def user_assign_dist_user_to_geotree(self):
        """ Function to assign user to geo tree """
        dist_cd = BuiltIn().get_variable_value("${dist_cd}")
        GamificationGet.GamificationGet().user_retrieves_option_values_geo_level_leaderboard("Sales Office")
        geo_res = StructureGet().user_get_hierarchy_structure_node_details()[0]
        PromoAssignPost.PromoAssignPost().get_geo_details_by_level_desc(dist_cd, geo_res)
        node_id = BuiltIn().get_variable_value("${DISTCAT_VALUE_ID}")
        url = "{0}assign-user/assigned/{1}".format(END_POINT_URL, node_id)
        payload = self.payload_assign_user()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_assign_user(self):
        """ Function for geo tree assignment payload content """
        start_dt = datetime.datetime.today() + datetime.timedelta(days=1)
        end_dt = datetime.datetime.today() + datetime.timedelta(days=36)
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        payload = {
            "START_DATE": start_dt.strftime("%Y-%m-%d"),
            "END_DATE": end_dt.strftime("%Y-%m-%d"),
            "SELECTED_IDS": [
                dist_id,
            ]
        }
        payload = json.dumps(payload)
        print("Assigned User Payload: ", payload)
        return payload
