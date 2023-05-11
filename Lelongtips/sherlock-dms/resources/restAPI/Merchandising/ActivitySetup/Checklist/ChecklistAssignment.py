import json
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.AppSetup.GamificationGet import GamificationGet
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
from resources.restAPI.MasterDataMgmt.DigitalPlaybook.DigitalPlaybookAssignment.DigitalPlayBookAssignmentPost import DigitalPlayBookAssignmentPost
from resources.restAPI.MasterDataMgmt.Promo.PromoAssignPost import PromoAssignPost
from resources.restAPI.MasterDataMgmt.Customer.CustomerGet import CustomerGet
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route.RouteGet import RouteGet
from resources.restAPI.MasterDataMgmt.Distributor.DistributorGet import DistributorGet
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ChecklistAssignment(object):
    dist_body_variable = "${dist_body_result}"
    assign_payload = "${dist_assignment_payload}"
    checklist_u = "ChecklistSetup.U"

    @keyword('user assigns checklist to Level:${Level}, Node:${Node}, Dist:${Dist}')
    def user_creates_checklist_assignment(self, level, node, dist):
        geo_payload = DigitalPlayBookAssignmentPost().dist_assignment_geo_level_payload(level, node, dist)

        if dist != "Without":
            dist_payload = DigitalPlayBookAssignmentPost().dist_assignment_dist_payload(dist)
        else:
            dist_payload = {}
        dist_assignment_payload = self.dist_assignment_payload_general(geo_payload, dist_payload)
        BuiltIn().set_test_variable(self.assign_payload, [dist_assignment_payload])

    @keyword('user create customer assignment for checklist to ${cust_or_cust_hierarchy}')
    def user_assign_cust(self, cust):
        c_assignment_payload = ""
        assinged_cust_payload = None
        StructureGet().user_get_hierid_from_hierarchy_structure_name("General Customer Hierarchy")
        hier_structure_details = StructureGet().user_get_hierarchy_structure_info_by_hierarchy_id()
        cust = cust.split(":")
        if cust[1] == "without":
            assinged_cust_payload = []
            cust_data = []
        elif cust[0] == "Customer":
            cust_cd = cust[1]
            CustomerGet().user_gets_cust_by_using_code(cust_cd)
            cust = BuiltIn().get_variable_value("${cust_body_result}")[0]
            BuiltIn().set_test_variable("${res_bd_cust_id}", cust['ID'])
            cust = CustomerGet().user_retrieves_cust_by_id()
            BuiltIn().set_test_variable("${distributor_id}", cust['DIST_ID'])
            DistributorGet().user_gets_distributor_by_using_id()
            dist = BuiltIn().get_variable_value(self.dist_body_variable)
            assinged_cust_payload = DigitalPlayBookAssignmentPost().assigned_customer_payload(cust, dist)
            assinged_cust_payload = [assinged_cust_payload]
            cust_data = DigitalPlayBookAssignmentPost().cust_data_payload(cust, "customer")
            cust_data = [cust_data]
        else:
            cust__hier_lvl_and_value = cust[1].split(",")
            for item in hier_structure_details['levels']:
                if item['name'] == cust__hier_lvl_and_value[0]:
                    BuiltIn().set_test_variable("${tree_id}",  item['treeId'])
                    BuiltIn().set_test_variable("${level_val}", item['name'])
            res = StructureGet().user_get_prd_or_or_cust_hierearchy_info()
            DigitalPlayBookAssignmentPost().search_node_from_cust_geo(res, cust__hier_lvl_and_value[1])
            cust_node_res_bd = BuiltIn().get_variable_value("${cust_node_rs_bd}")
            cust_data = DigitalPlayBookAssignmentPost().cust_data_payload(cust_node_res_bd, "cust hierarchy")
            cust_data = [cust_data]
        c_assignment_payload = self.customer_assign_general_payload(cust_data, assinged_cust_payload)
        dist_assignment_payload = BuiltIn().get_variable_value(self.assign_payload)
        dist_assignment_payload.append(c_assignment_payload)
        dist_assignment_payload[0]['criteria']['main']['data'][0]['LEVEL_CD'] = cust_data[0]['DIST_CD']
        payload = json.dumps(dist_assignment_payload)
        self.user_post_for_assignment(payload)

    def user_post_for_assignment(self, payload):
        checklist_id = BuiltIn().get_variable_value("${checklist_id}")
        url = "{0}checklist/{1}/assignment".format(END_POINT_URL, checklist_id)
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        print("assignment url = ", url)
        print("assignment payload = ", payload)
        if response.status_code == 201:
            body_result = response.json()
            print("Body Result: ", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def dist_assignment_payload_general(self, geo_level_payload, dist_payload):

        payload = {
            "title": "Distributor",
            "component": "DistributorAssignmentComponent",
            "assignmentType": "D",
            "criteriaRelationship": "NONE",
            "stateChanged": True,
            "assignAll": False,
            "view": self.checklist_u,
            "hasAllCustom": True,
            "hasExclusion": True,
            "criteria": {
                "main": {
                    "data": [
                        geo_level_payload
                    ]
                },
                "hierarchy": {
                    "data": []
                },
                "attribute": {
                    "data": []
                }
            },
            "assigned": {
                "data": [
                    dist_payload
                ]
            },
            "excluded": {
                "data": []
            }
        }
        return payload

    def customer_assign_general_payload(self, cust_data, assigned_cust):
        payload = {
            "title": "Merc audit cust assignmnet",
            "component": "CustomerAssignmentComponent",
            "assignmentType": "C",
            "criteriaRelationship": "AND",
            "stateChanged": True,
            "assignAll": False,
            "view": self.checklist_u,
            "hasAllCustom": True,
            "hasExclusion": True,
            "criteria": {
                "main": {
                    "data": []
                },
                "hierarchy": {
                    "data": cust_data
                },
                "attribute": {
                    "data": []
                }
            },
            "assigned": {
                "data": assigned_cust
            },
            "excluded": {
                "data": []
            }
        }
        return payload
