import json
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
from resources.restAPI.MasterDataMgmt.Customer.CustomerGet import CustomerGet
from resources.restAPI.MasterDataMgmt.Distributor.DistributorGet import DistributorGet
from resources.restAPI.MasterDataMgmt.DigitalPlaybook.DigitalPlaybookAssignment.DigitalPlayBookAssignmentPost import DigitalPlayBookAssignmentPost
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
CODETABLE_END_POINT_URL = PROTOCOL + "codetable" + APP_URL
END_POINT_URL = PROTOCOL + "promotion" + APP_URL


class SamplingAssignment(object):
    dist_body_variable = "${dist_body_result}"
    assign_payload = "${dist_assignment_payload}"
    sample_u = "sample.U"

    @keyword('user retrieves sampling assignment')
    def user_retrieves_sampling_assignment(self):
        sampling_id = BuiltIn().get_variable_value("${sampling_id}")
        url = "{0}sample/{1}/assignment".format(END_POINT_URL, sampling_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        try_count = 0
        while try_count < 50:
            try:
                try_count += 1
                response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
                print("{0}. Status Code: {1}".format(try_count, response.status_code))
                if response.status_code == 200:
                    body_result = response.json()
                    print("Body Result: ", body_result)
                    break
            except Exception as e:
                print(e.__class__, "occured")
            print("Total try: ", try_count)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword('user assigns sampling to Level:${Level}, Node:${Node}, Dist:${Dist}')
    def user_creates_sampling_assignment(self, level, node, dist):
        dist_data = DigitalPlayBookAssignmentPost().dist_assignment_geo_level_payload(level, node, dist)
        if dist is not "Without":
            assigned_dist = DigitalPlayBookAssignmentPost().dist_assignment_dist_payload(dist)
        else:
            assigned_dist = {}
        d_assignment_payload = self.dist_assignment_payload(dist_data, assigned_dist)
        BuiltIn().set_test_variable(self.assign_payload, [d_assignment_payload])

    @keyword('user create customer assignment for sampling to ${cust_or_cust_hierarchy}')
    def user_assign_cust_or_cust_hierarchy(self, cust_or_cust_hierarchy):
        assigned_cust_payload = None
        StructureGet().user_get_hierid_from_hierarchy_structure_name("General Customer Hierarchy")
        hier_structure_details = StructureGet().user_get_hierarchy_structure_info_by_hierarchy_id()
        cust_or_cust_hierarchy = cust_or_cust_hierarchy.split(":")
        if cust_or_cust_hierarchy[1] == "without":
            assigned_cust_payload = []
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
            assigned_cust_payload = DigitalPlayBookAssignmentPost().assigned_customer_payload(cust, dist)
            assigned_cust_payload = [assigned_cust_payload]
            cust_data = DigitalPlayBookAssignmentPost().cust_data_payload(cust, "customer")
            cust_data = [cust_data]
        else:
            cust__hier_lvl_and_value = cust_or_cust_hierarchy[1].split(",")
            for item in hier_structure_details['levels']:
                if item['name'] == cust__hier_lvl_and_value[0]:
                    BuiltIn().set_test_variable("${tree_id}",  item['treeId'])
                    BuiltIn().set_test_variable("${level_val}", item['name'])
            res = StructureGet().user_get_prd_or_or_cust_hierearchy_info()
            DigitalPlayBookAssignmentPost().search_node_from_cust_geo(res, cust__hier_lvl_and_value[1])
            cust_node_res_bd = BuiltIn().get_variable_value("${cust_node_rs_bd}")
            cust_data = DigitalPlayBookAssignmentPost().cust_data_payload(cust_node_res_bd, "cust hierarchy")
            cust_data = [cust_data]
        c_assignment_payload = self.cust_assignment_payload(cust_data, assigned_cust_payload)
        dist_assignment_payload = BuiltIn().get_variable_value(self.assign_payload)
        dist_assignment_payload.append(c_assignment_payload)
        payload = json.dumps(dist_assignment_payload)
        print("Payload is = ", payload)
        self.user_post_for_assignment(payload)

    def user_post_for_assignment(self, payload):
        sampling_id = BuiltIn().get_variable_value("${sampling_id}")
        url = "{0}sample/{1}/assignment".format(END_POINT_URL, sampling_id)
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("Body Result: ", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def dist_assignment_payload(self, dist_data, assigned_dist):
        dist_payload = {
            "title": "Distributor",
            "component": "DistributorAssignmentComponent",
            "assignmentType": "D",
            "criteriaRelationship": "NONE",
            "stateChanged": True,
            "assignAll": False,
            "view": self.sample_u,
            "hasAllCustom": True,
            "hasExclusion": True,
            "criteria": {
                "main": {
                    "data": [dist_data]
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
                    assigned_dist
                ]
            },
            "excluded": {
                "data": [
                ]
            }
        }
        return dist_payload

    def cust_assignment_payload(self, cust_data, assigned_cust):
        cust_payload = {
            "title": "Customer Assignment",
            "component": "CustomerAssignmentComponent",
            "assignmentType": "C",
            "criteriaRelationship": "AND",
            "stateChanged": True,
            "assignAll": False,
            "view": self.sample_u,
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
        return cust_payload


