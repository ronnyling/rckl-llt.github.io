from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import json
import secrets
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure import StructureGet

END_POINT_URL = PROTOCOL + "dynamic-hierarchy" + APP_URL


class ValuePost(object):

    @keyword('user sends details to create new hierarchy node value from data')
    def user_sends_details_to_create_new_hierarchy_node_value_from_data(self):
        details = BuiltIn().get_variable_value("&{hierarchy_details}")
        hier_id = BuiltIn().get_variable_value("${hier_id}")    # get the hierarchy structure from StructureGet class
        response_dict = StructureGet.StructureGet().user_get_hierarchy_structure_info_from_data()
        tree_id = StructureGet.StructureGet().get_levels_from_structure(response_dict, details.get('ParentLevel'))  # return a selected Level/Tree ID associated with this hierarchy structure

        url = "{0}hierarchy/hier/{1}/node/add".format(END_POINT_URL, hier_id)
        payload = self.payload_structure(tree_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            response_dict = json.loads(response.text)
            print("Result: ", response_dict)
            node_id = response_dict.get('nodeId')
            BuiltIn().set_test_variable("${node_id}", node_id)

    def payload_structure(self, tree_id=None):
        block = \
            {
                "parentId": "00",
                "nodeName": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                "desc": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            }

        details = BuiltIn().get_variable_value("&{hierarchy_details}")
        if details:
            for k, v in details.items():
                if v == "" or type(v) is int:  # set random for empty or int cells
                    details[k] = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))

            block.update((k.split('-')[1], v) for k, v in details.items() if "Value-" in k if v)  # only update payload if data input is not null and contain the keyword

        if tree_id is not None:
            block.update({"parentId": tree_id})

        payload = json.dumps(block)
        print("Payload: ", payload)
        return payload
