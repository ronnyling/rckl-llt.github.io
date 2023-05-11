import json
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.AppSetup.GamificationGet import GamificationGet
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
from resources.restAPI.MasterDataMgmt.Promo.PromoAssignPost import PromoAssignPost
from resources.restAPI.MasterDataMgmt.Customer.CustomerGet import CustomerGet
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route.RouteGet import RouteGet
from resources.restAPI.MasterDataMgmt.Distributor.DistributorGet import DistributorGet
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
CODETABLE_END_POINT_URL = PROTOCOL + "codetable" + APP_URL
END_POINT_URL = PROTOCOL + "message" + APP_URL
ASSIGNMENT_END_POINT_URL = PROTOCOL + "assignment" + APP_URL


class DigitalPlayBookAssignmentPost(object):
    dist_body_variable = "${dist_body_result}"
    assign_paylod = "${dist_assignment_payload}"
    playbook_u = "playbook.U"

    @keyword('user assigns playbook to Level:${Level}, Node:${Node}, Dist:${Dist}')
    def user_creates_playbook_assignment(self, level, node, dist):
        geo_payload = self.dist_assignment_geo_level_payload(level, node, dist)
        if dist != "Without":
            dist_payload = self.dist_assignment_dist_payload(dist)
        else:
            dist_payload = {}
        dist_assignment_payload = self.dist_assignment_payload_general(geo_payload, dist_payload)
        BuiltIn().set_test_variable(self.assign_paylod,[dist_assignment_payload])

    @keyword('user create customer assignment for playbook to ${cust_or_cust_hierarchy}')
    def user_assign_cust_or_cust_hierarchy(self, cust_or_cust_hierarchy):
        r_or_c_assignment_payload = ""
        assinged_cust_payload = None
        StructureGet().user_get_hierid_from_hierarchy_structure_name("General Customer Hierarchy")
        hier_structure_details = StructureGet().user_get_hierarchy_structure_info_by_hierarchy_id()
        cust_or_cust_hierarchy = cust_or_cust_hierarchy.split(":")
        if cust_or_cust_hierarchy[1] == "without":
            assinged_cust_payload = []
            cust_data = []
        elif cust_or_cust_hierarchy[0] == "Customer":
            cust_cd = cust_or_cust_hierarchy[1]
            CustomerGet().user_gets_cust_by_using_code(cust_cd)
            cust = BuiltIn().get_variable_value("${cust_body_result}")[0]
            BuiltIn().set_test_variable("${res_bd_cust_id}", cust['ID'])
            cust = CustomerGet().user_retrieves_cust_by_id()
            BuiltIn().set_test_variable("${distributor_id}", cust['DIST_ID'])
            DistributorGet().user_gets_distributor_by_using_id()
            dist = BuiltIn().get_variable_value(self.dist_body_variable)
            assinged_cust_payload = self.assigned_customer_payload(cust, dist)
            assinged_cust_payload = [assinged_cust_payload]
            cust_data = self.cust_data_payload(cust, "customer")
            cust_data = [cust_data]
        else:
            cust__hier_lvl_and_value = cust_or_cust_hierarchy[1].split(",")
            for item in hier_structure_details['levels']:
                if item['name'] == cust__hier_lvl_and_value[0]:
                    BuiltIn().set_test_variable("${tree_id}",  item['treeId'])
                    BuiltIn().set_test_variable("${level_val}", item['name'])
            res = StructureGet().user_get_prd_or_or_cust_hierearchy_info()
            self.search_node_from_cust_geo(res, cust__hier_lvl_and_value[1])
            cust_node_res_bd = BuiltIn().get_variable_value("${cust_node_rs_bd}")
            cust_data = self.cust_data_payload(cust_node_res_bd, "cust hierarchy")
            cust_data = [cust_data]
        r_or_c_assignment_payload = self.customer_assign_general_payload(cust_data, assinged_cust_payload)
        dist_assignment_payload = BuiltIn().get_variable_value(self.assign_paylod)
        dist_assignment_payload.append(r_or_c_assignment_payload)
        payload = json.dumps(dist_assignment_payload)
        self.user_post_for_assignment(payload)

    def search_node_from_cust_geo(self, cust_geo, cust_node_desc):
        for item in cust_geo:
            if item.get('children') is not None:
                self.search_node_from_cust_geo(item['children'], cust_node_desc)
                result = self.level_node_found(item, cust_node_desc)
                if result:
                    break
            else:
                result = self.level_node_found(item, cust_node_desc)
                if result:
                    break

    def level_node_found(self, a, b):
        if a.get("code") == b:
            BuiltIn().set_test_variable("${cust_node_rs_bd}", a)
            print("found node asd=", a)
            return True
        else:
            return False

    def user_search_node_from_customer_hierarchy(self, res, node):
        for item in res:
            if item['code'] == node:
                return item
            else:
                print("Customer Node not found")
                break

    @keyword('user assign ${route} to digital playbook')
    def user_assign_route(self, route):
        route = route.split(":")
        route_details = self.assigned_route_payload(route[1])
        route_type_data = self.route_op_data_payload(route_details["OP_TYPE"])
        r_or_c_assignment_payload = self.route_assignment_payload(route_type_data, route_details)
        dist_assignment_payload = BuiltIn().get_variable_value(self.assign_paylod)
        dist_assignment_payload.append(r_or_c_assignment_payload)
        payload = json.dumps(dist_assignment_payload)
        self.user_post_for_assignment(payload)

    def user_post_for_assignment(self, payload):
        playbook_id = BuiltIn().get_variable_value("${playbook_id}")
        url = "{0}playbk-setup/{1}/assignment".format(END_POINT_URL, playbook_id)
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        print("Payload: ", payload)
        try_count = 0
        while try_count < 50:
            try:
                try_count += 1
                response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
                print("{0}. Status Code: {1}".format(try_count, response.status_code))
                if response.status_code == 201:
                    body_result = response.json()
                    print("Response: ", body_result)
                    BuiltIn().set_test_variable("${plybk_assignment_id}", body_result[0]['Id'])
                    break
            except Exception as e:
                print(e.__class__, "occured")
        print("Total try: ", try_count)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def combine_address(self, address_rs_body):
        address = "{0} {1} {2}".format(address_rs_body['ADD1'], address_rs_body['ADD2'], address_rs_body['ADD3'])
        return address

    def assigned_customer_payload(self, cust, dist):
        payload = {
            "CUST_CD": cust['CUST_CD'],
            "CUST_NAME": cust['CUST_NAME'],
            "CUST_ADDRESS": self.combine_address(cust['ADDRESS_CD']),
            "CUST_ID": cust['ID'],
            "DIST_ID": dist['ID'],
            "DIST_ADDR": self.combine_address(dist['ADDRESS_CD']),
            "DIST_CD": dist['DIST_CD'],
            "DIST_NAME": dist['DIST_NAME']
        }
        return payload

    def cust_data_payload(self, res_body, cond):
        if cond == "customer":
            level_val = "Customer"
            level_cd = res_body['CUST_CD']
            level_desc = res_body['CUST_NAME']
            dist_cd = res_body['DIST_CD']
            dist_name = res_body['DIST_ID']['DIST_NAME']
            ass_entity_id = None
            node_id = res_body['ID']
        else:
            dist_cd = None
            dist_name = None
            level_val = BuiltIn().get_variable_value("${level_val}")
            level_cd = res_body['code']
            level_desc = res_body['desc']
            node_id = res_body['nodeId']
            ass_entity_id = BuiltIn().get_variable_value("${tree_id}")

        hier_id = BuiltIn().get_variable_value("${hier_id}")
        payload = {
                            "LEVEL_CD": level_cd,
                            "LEVEL_DESC": level_desc,
                            "LEVEL_VAL": level_val,
                            "DIST_CD": dist_cd,
                            "DIST_NAME": dist_name,
                            "ASS_CRITERIA_TYPE_ID": "A647E2BF:1A533242-6149-4A41-A9E0-F87A32E55F0F",
                            "ASS_CRITERIA_HIER_ID": hier_id,
                            "ASS_ENTITY_ID": ass_entity_id,
                            "ASS_ENTITY_VALUE_ID": node_id,
                            "ID": node_id
                        }
        return payload

    def dist_assignment_geo_level_payload(self, level, node, dist_cd):
        GamificationGet().user_retrieves_option_values_geo_level_leaderboard(level)
        geo_res = StructureGet().user_get_hierarchy_structure_node_details()[0]
        PromoAssignPost().get_geo_details_by_level_desc(node, geo_res)
        ASS_ENTITY_VALUE_ID = BuiltIn().get_variable_value("${DISTCAT_VALUE_ID}")
        ASS_ENTITY_ID = BuiltIn().get_variable_value("${DISTCAT_ID}")
        payload = {
                            "LEVEL_CD": BuiltIn().get_variable_value("${LEVEL_DESC}"),
                            "LEVEL_DESC": BuiltIn().get_variable_value("${LEVEL_DESC}"),
                            "LEVEL_VAL": BuiltIn().get_variable_value("${LEVEL_VAL}"),
                            "VISIBILITY": True,
                            "ASS_ENTITY_ID": ASS_ENTITY_ID,
                            "ASS_ENTITY_VALUE_ID": ASS_ENTITY_VALUE_ID,
                            "ID": ASS_ENTITY_VALUE_ID
                        }
        return payload

    def dist_assignment_dist_payload(self, dist_cd):
        DistributorGet().user_gets_distributor_by_using_code(dist_cd)
        DistributorGet().user_gets_distributor_by_using_id()
        dist = BuiltIn().get_variable_value(self.dist_body_variable)
        payload = {
                        "DIST_ID": dist['ID'],
                        "DIST_CD": dist['DIST_CD'],
                        "DIST_NAME": dist['DIST_NAME'],
                        "ADDRESS": self.combine_address(dist['ADDRESS_CD'])
                }
        return payload

    def dist_assignment_payload_general(self, geo_level_payload, dist_payload):
        payload = {
            "title": "Distributor Assignment",
            "component": "DistributorAssignmentComponent",
            "assignmentType": "D",
            "criteriaRelationship": "NONE",
            "stateChanged": True,
            "filter": [],
            "assignAll": False,
            "view": self.playbook_u,
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
            },
            "assignedSearchActions": [
                {
                    "title": "",
                    "name": "search",
                    "description": "Show inline filter",
                    "display_type": "list",
                    "icon": "search",
                    "behavior": "",
                    "content": {},
                    "index": "4",
                    "label": ""
                }
            ],
            "excludedSearchActions": [
                {
                    "title": "",
                    "name": "search",
                    "description": "Show inline filter",
                    "display_type": "list",
                    "icon": "search",
                    "behavior": "",
                    "content": {},
                    "index": "4",
                    "label": ""
                }
            ]
        }
        return payload

    def customer_assign_general_payload(self, cust_data, assigned_cust):
        payload = {
            "title": "Customer Assignment",
            "component": "CustomerAssignmentComponent",
            "assignmentType": "C",
            "criteriaRelationship": "AND",
            "stateChanged": True,
            "filter": [],
            "assignAll": False,
            "view": self.playbook_u,
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

    def route_op_data_payload(self, route_op_type):
        route_type = self.retrieve_route_type_details()

        payload = {
            "ID": route_op_type,
            "ASS_ROUTE_OPTYPE": route_op_type,
            "LEVEL_CD": route_op_type,
            "LEVEL_DESC": route_type[route_op_type],
            "LEVEL_VAL": "Operation Type"
        }
        return payload

    def assigned_route_payload(self, route_cd):
        RouteGet().user_gets_route_by_using_code(route_cd)
        route = BuiltIn().get_variable_value("${route_rs_bd}")
        BuiltIn().set_test_variable("${distributor_id}", route['DIST_ID'])
        DistributorGet().user_gets_distributor_by_using_id()
        dist = BuiltIn().get_variable_value(self.dist_body_variable)

        payload = {
            "ROUTE_ID": route["ID"],
            "ROUTE_CD": route["ROUTE_CD"],
            "ROUTE_NAME": route["ROUTE_NAME"],
            "DIST_ID": route['DIST_ID'],
            "DIST_ADDR": self.combine_address(dist['ADDRESS_CD']),
            "DIST_CD": dist['DIST_CD'],
            "DIST_NAME": dist['DIST_NAME'],
            "OP_TYPE": route['OP_TYPE']
        }
        return payload

    def route_assignment_payload(self, data,  route):

        payload = {
        "title": "Route Assignment",
        "component": "RouteOptypeAssignmentComponent",
        "assignmentType": "O",
        "criteriaRelationship": "NONE",
        "stateChanged": True,
        "filter": [],
        "assignAll": False,
        "view": self.playbook_u,
        "hasAllCustom": True,
        "hasExclusion": True,
        "criteria": {
            "main": {
                "data": [
                    data
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
            "data": [route]
        },
        "excluded": {
            "data": []
            }
        }
        return payload

    def retrieve_route_type_details(self):
        url = "{0}codetable/ROUTE_OPERATION_TYPE".format(CODETABLE_END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        body_result = response.json()
        return body_result
