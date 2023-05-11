from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
import secrets
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "dynamic-hierarchy" + APP_URL


class StructureGet(object):
    HIER_ID = "${hier_id}"
    HIER_RS_BD = "${hier_rs_bd}"

    @keyword('user retrieves ${cond} hierarchy structure')
    def user_retrieves_hierarchy_structure(self, cond):
        if cond == "invalid":
            hier_id = COMMON_KEY.generate_random_id("0")
        else:
            hier_id = BuiltIn().get_variable_value(self.HIER_ID)
        url = "{0}structure/hier/{1}".format(END_POINT_URL, hier_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            BuiltIn().set_test_variable(self.HIER_RS_BD, response.json())
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword('user retrieves ${product_or_customer} hierarchy structure with ${cond} data')
    def user_retrieves_product_or_cust_hierarchy_structure(self, cust_or_prd, cond):
        if cond == "invalid":
            hier_id = COMMON_KEY.generate_random_id("0")
        else:
            hier_id = BuiltIn().get_variable_value(self.HIER_ID)
        url = "{0}structure/hier/{1}/flat-hier".format(END_POINT_URL, hier_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            BuiltIn().set_test_variable(self.HIER_RS_BD, response.json())
        BuiltIn().set_test_variable("${status_code}", response.status_code)


    @keyword('user get hierarchy structure node details')
    def user_get_hierarchy_structure_node_details(self):
        geo_hier_id = BuiltIn().get_variable_value("${geo_hier_id}")
        url = "{0}hierarchy/hier/{1}/sales/00".format(END_POINT_URL, geo_hier_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        return response.json()

    def user_get_prd_or_or_cust_hierearchy_info(self):
        hier_id = BuiltIn().get_variable_value(self.HIER_ID)
        tree_id = BuiltIn().get_variable_value("${tree_id}")
        url = "{0}hierarchy/hier/{1}/tree/{2}/view".format(END_POINT_URL, hier_id, tree_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            BuiltIn().set_test_variable("${tree_view_bd}", response.json())
        return response.json()

    @keyword('user get hierarchy structure info by hierarchy id')
    def user_get_hierarchy_structure_info_by_hierarchy_id(self):
        hier_id = BuiltIn().get_variable_value(self.HIER_ID)
        url = "{0}structure/hier/{1}".format(END_POINT_URL, hier_id)
        response_dict = self.send_request(url)
        BuiltIn().set_test_variable("${response_dict}", response_dict)
        return response_dict

    @keyword('user get hierarchy id by giving hierarchy structure name ${name}')
    def user_get_hierid_from_hierarchy_structure_name(self, name):
        hier_name = name
        url = "{0}structure/list".format(END_POINT_URL)
        response_dict = self.send_request(url)
        for each in response_dict:
            if each.get('treeDes') == hier_name:
                BuiltIn().set_test_variable(self.HIER_ID, each.get('id'))
                print("Hierarchy structure ID: ", each.get('id'))
                return each.get('id')

    def send_request(self, url):
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        response_dict = {}
        if response.status_code == 200:
            response_dict = json.loads(response.text)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return response_dict

    def get_levels_from_structure(self, level_name, cond):
        response_dict = BuiltIn().get_variable_value("${response_dict}")
        levels = response_dict.get('levels')    # the levels is an other array of dictionary within response dictionary.
        if level_name == 'random':
            choice = secrets.choice(levels)
            return choice['treeId']
        else:
            for each in levels:
                if cond == 'id':
                    self.search_level_by_id(each, level_name)
                else:
                   self.search_level_by_name(each, level_name)

    def search_level_by_name(self, each, level_name):
        if each.get('name') == level_name:
            BuiltIn().set_test_variable("${tree_id}", each.get('treeId'))
            return each.get('treeId')

    def search_level_by_id(self, each, level_name):
        if each.get('treeId') == level_name:
            BuiltIn().set_test_variable("${tree_name}", each.get('name'))
            return each.get('name')
    def get_prd_hierarchy(self):
        url = "{0}structure/active/Product".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return response.json()

    @keyword("get hierarchy structure by Field:${field} Value:${Value}")
    def get_hierarchy_structure_by_field_and_value(self, field, value):
        filter_hierarchy = {field: {"$eq": value}}
        filter_hierarchy = json.dumps(filter_hierarchy)
        url = "{0}structure/list?filter={1}".format(END_POINT_URL, filter_hierarchy)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve hierarchy"
        body_result = response.json()
        choice = secrets.choice(body_result)
        BuiltIn().set_test_variable("${rs_bd_hier_struct}", choice)
        BuiltIn().set_test_variable(self.HIER_ID, choice['id'])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return choice

    @keyword('user retrieves ${level} hierarchy with ${code} code')
    def user_retrieves_hierarchy_level_with_name(self, level, code):
        hier_details = BuiltIn().get_variable_value(self.HIER_RS_BD)
        if level == 'Category':
            node = 'NODE_NAME1'
            id = "LEVEL1_ID"
        elif level == 'Brand':
            node = 'NODE_NAME2'
            id = "LEVEL2_ID"
        elif level == 'Variant':
            node = 'NODE_NAME3'
            id = "LEVEL3_ID"
        else:
            node = 'NODE_NAME4'
            id = "LEVEL4_ID"
        for item in hier_details:
            if code == item[node]:
                BuiltIn().set_test_variable("${res_bd_node_id}", item[id])
                break

    def user_node_to_assign_for_customer(self):
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        url = "{0}customer/{1}/nodes-to-assign".format(END_POINT_URL, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        return response.json()

    def user_nodes_for_customer(self):
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        url = "{0}customer/{1}/nodes".format(END_POINT_URL, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        return response.json()