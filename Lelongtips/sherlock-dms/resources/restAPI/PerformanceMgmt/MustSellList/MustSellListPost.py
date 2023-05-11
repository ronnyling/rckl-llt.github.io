import secrets, json
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from datetime import datetime, timedelta
from resources.restAPI.Config.AppSetup import ReportGet
from resources.restAPI.Config.AppSetup.AppSetupGet import AppSetupGet
from resources.restAPI.Config.Attribute.AttributeCreation.AttributeCreationGet import AttributeCreationGet
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
from resources.restAPI.Config.DynamicHierarchy.ProductCustomerHierarchy.ValueGet import ValueGet
from resources.restAPI.MasterDataMgmt.DigitalPlaybook.DigitalPlaybookAssignment import DigitalPlayBookAssignmentPost
from resources.restAPI.MasterDataMgmt.Promo import PromoBuyTypeGet
END_POINT_URL = PROTOCOL + "performance" + APP_URL

class MustSellListPost(object):
    MSL_ID = "${res_bd_msl_id}"
    STATUS_CODE = "${status_code}"
    BODY_RESULT = "${body_result}"
    TREE_ID = "${tree_id}"
    HIER_ID = "${hier_id}"

    @keyword('user creates MSL with ${data_type} data')
    def user_creates_msl_with(self, data_type):
        url = "{0}msl".format(END_POINT_URL)
        payload = self.payload_msl("post")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${res_bd_msl_payload}", body_result)
            BuiltIn().set_test_variable("${res_bd_msl_id}", body_result["ID"])
            BuiltIn().set_test_variable("${res_bd_msl_cd}", body_result["MSL_CD"])
        BuiltIn().set_test_variable(self.STATUS_CODE, response.status_code)

    @keyword('user assigns product hierarchy to MSL')
    def user_assigns_msl_with_product(self):
        res_bd_msl_id = BuiltIn().get_variable_value(self.MSL_ID)
        url = "{0}msl/{1}/msl-prd-hier".format(END_POINT_URL, res_bd_msl_id)
        payload = self.payload_prod()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${res_bd_prod_hier_payload}", body_result)
            BuiltIn().set_test_variable("${res_bd_prod_hier_id}", body_result[0]["ID"])
        BuiltIn().set_test_variable(self.STATUS_CODE, response.status_code)

    @keyword('user assigns distributor to MSL')
    def user_assigns_msl_with_distributor(self):
        res_bd_msl_id = BuiltIn().get_variable_value(self.MSL_ID)
        url = "{0}msl/{1}/msl-geo-node".format(END_POINT_URL, res_bd_msl_id)
        payload = self.payload_geo()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${res_bd_dist_payload}", body_result)
            BuiltIn().set_test_variable("${res_bd_msl_geo_id}", body_result[0]["ID"])
        BuiltIn().set_test_variable(self.STATUS_CODE, response.status_code)

    @keyword('user assigns route to MSL')
    def user_assigns_msl_with_route(self):
        res_bd_msl_id = BuiltIn().get_variable_value(self.MSL_ID)
        url = "{0}msl/{1}/msl-route-optype".format(END_POINT_URL, res_bd_msl_id)
        payload = self.payload_route()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${res_bd_route_payload}", body_result)
            BuiltIn().set_test_variable("${res_bd_msl_route_op_id}", body_result[0]["ID"])
        BuiltIn().set_test_variable(self.STATUS_CODE, response.status_code)

    @keyword('user assigns customer to MSL')
    def user_assigns_msl_with_customer(self):
        res_bd_msl_id = BuiltIn().get_variable_value(self.MSL_ID)
        url = "{0}msl/{1}/msl-cust-hier".format(END_POINT_URL, res_bd_msl_id)
        payload = self.payload_customer()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${res_bd_customer_payload}", body_result)
            BuiltIn().set_test_variable("${res_bd_msl_cust_id}", body_result[0]["ID"])
        BuiltIn().set_test_variable(self.STATUS_CODE, response.status_code)

    @keyword('user assigns attribute to MSL')
    def user_assigns_msl_with_attribute(self):
        res_bd_msl_id = BuiltIn().get_variable_value(self.MSL_ID)
        url = "{0}msl/{1}/msl-cust-attr".format(END_POINT_URL, res_bd_msl_id)
        payload = self.payload_attribute()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${res_bd_attr_payload}", body_result)
            BuiltIn().set_test_variable("${res_bd_msl_attr_id}", body_result[0]["ID"])
        BuiltIn().set_test_variable(self.STATUS_CODE, response.status_code)

    def payload_msl(self, action_type):
        today_date = datetime.now()
        td1 = timedelta(days=2)
        td2 = timedelta(days=7)
        START_DT = (today_date + td1).strftime('%Y-%m-%d')
        END_DT = (today_date + td2).strftime('%Y-%m-%d')
        payload = {
            "STATUS": secrets.choice([True, False]),
            "START_DT": START_DT,
            "END_DT": END_DT,
            "MSL_DESC":''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
            "TYPE":"M"
        }

        details = BuiltIn().get_variable_value("${msl_details}")

        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("MSL Payload: ", payload)
        return payload

    def payload_prod(self):
        StructureGet().user_get_hierid_from_hierarchy_structure_name("General Product Hierarchy")
        hier_structure_details = StructureGet().user_get_hierarchy_structure_info_by_hierarchy_id()
        hier_id = hier_structure_details['hierId']
        AppSetupGet().user_retrieves_details_of_application_setup()
        body_res = BuiltIn().get_variable_value(self.BODY_RESULT)
        tree_id = body_res['MDSE_PROD_HIERARCHY_LEVEL']
        BuiltIn().set_test_variable(self.TREE_ID, tree_id)
        ValueGet().get_all_values_from_hierarchy_tree()
        node_id = ValueGet().get_value_by_random_data()
        payload = [
                {
                    "ASS_ENTITY_ID": tree_id,
                    "ASS_ENTITY_VALUE_ID": node_id,
                    "ASS_TYPE_ID": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_prod_assign_type("Hierarchy")['ID'],
                    "PRD_HIER_ID": hier_id
                }
        ]
        details = BuiltIn().get_variable_value("${prod_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Product Payload: ", payload)
        return payload

    def payload_geo(self):
        ReportGet.ReportGet().user_retrieves_geo_hier_id()
        StructureGet().user_get_hierid_from_hierarchy_structure_name("General Geo Hierarchy")
        body_result = StructureGet().user_get_hierarchy_structure_node_details()
        print("GEO Rep: ", body_result)
        print("Total number of records retrieved are ", len(body_result[0]['children']))
        if len(body_result[0]['children']) > 1:
            rand_cld = secrets.choice(range(0, len(body_result[0]['children'])))
        else:
            rand_cld = 0
        BuiltIn().set_test_variable(self.HIER_ID, body_result[0]['children'][rand_cld]["nodeId"])
        BuiltIn().set_test_variable(self.TREE_ID, body_result[0]['children'][rand_cld]["treeId"])
        hier_id = BuiltIn().get_variable_value(self.HIER_ID)
        tree_id = BuiltIn().get_variable_value(self.TREE_ID)
        payload = [
                {
                    "HIER_TREE_ID":tree_id,
                    "HIER_NODE_ID":hier_id
                }
        ]
        details = BuiltIn().get_variable_value("${geo_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Dist Geo Payload: ", payload)
        return payload

    def payload_route(self):
        body_result = DigitalPlayBookAssignmentPost.DigitalPlayBookAssignmentPost().retrieve_route_type_details()
        print("Route: ", body_result)
        print("Total number of records retrieved are ", len(body_result))
        if len(body_result) > 1:
            rand_rt= secrets.choice(range(0, len(body_result)))
        else:
            rand_rt= 0
        op_type = list(body_result.keys())
        BuiltIn().set_test_variable("${op_id}", op_type[rand_rt])
        op_id = BuiltIn().get_variable_value("${op_id}")
        payload = [
                {
                    "ROUTE_OP_TYPE":op_id,
                }
        ]
        details = BuiltIn().get_variable_value("${route_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Route Payload: ", payload)
        return payload

    def payload_customer(self):
        StructureGet().user_get_hierid_from_hierarchy_structure_name("General Customer Hierarchy")
        hier_structure_details = StructureGet().user_get_hierarchy_structure_info_by_hierarchy_id()
        hier_id = hier_structure_details['hierId']
        AppSetupGet().user_retrieves_details_of_application_setup()
        body_res = BuiltIn().get_variable_value(self.BODY_RESULT)
        tree_id = body_res['MDSE_CUST_HIERARCHY_LEVEL']
        BuiltIn().set_test_variable(self.TREE_ID, tree_id)
        ValueGet().get_all_values_from_hierarchy_tree()
        node_id = ValueGet().get_value_by_random_data()
        payload = [
                {
                    "ASS_ENTITY_ID": tree_id,
                    "ASS_ENTITY_VALUE_ID": node_id,
                    "ASS_TYPE_ID":PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_cust_assign_type("Hierarchy"),
                    "CUST_HIER_ID": hier_id
                }
        ]
        details = BuiltIn().get_variable_value("${customer_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Customer Payload: ", payload)
        return payload

    def payload_attribute(self):

        AttributeCreationGet().user_retrieves_all_attribute_creation()
        tree_id = BuiltIn().get_variable_value("${attribute_creation_id}")
        AttributeCreationGet().user_retrieves_active_attribute()
        body_result = BuiltIn().get_variable_value(self.BODY_RESULT)
        node_id = body_result[0]['ID']
        payload = [
                {
                    "ASS_ENTITY_ID": tree_id,
                    "ASS_ENTITY_VALUE_ID": node_id,
                    "ASS_TYPE_ID": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_cust_assign_type("Attribute"),
                    "CUST_HIER_ID": None
                }
        ]
        details = BuiltIn().get_variable_value("${attribute_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Attribute Payload: ", payload)
        return payload