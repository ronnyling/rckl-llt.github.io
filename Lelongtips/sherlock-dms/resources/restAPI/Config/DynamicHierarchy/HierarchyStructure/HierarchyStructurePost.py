from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import json, secrets
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "dynamic-hierarchy" + APP_URL


class HierarchyStructurePost(object):

    @keyword('user creates ${prime_flag} hierarchy structure with ${cond} data')
    def user_creates_hierarchy_structure(self, prime_flag, cond):
        levels = self.level_hier_payload()
        payload = self.general_hier_structure_payload(prime_flag, levels)
        url = "{0}structure/structure".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 200:
            response_dict = json.loads(response.text)
            BuiltIn().set_test_variable("${hier_id}", response.json()['hierId'])
            print("Result: ", response_dict)
        BuiltIn().set_test_variable("${status_code}", response.status_code)


    def general_hier_structure_payload(self, prime_flag, levels):

        first_hier_lvl = BuiltIn().get_variable_value("${1st_hier_lvl}")
        if levels is None:
            lvl = {"level" : 1}
            first_hier_lvl.update(lvl)
            levels = first_hier_lvl
        payload = {
                "hierDesc": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                "primeFlag": prime_flag,
                "lob": '',
                "hierStructure": "DA3255893A192C00F0000002C1E25A00",
                "levels": [levels]
            }
        general_hier_details = BuiltIn().get_variable_value("${general_hier_details}")
        if general_hier_details is not None:
            payload.update((k, v) for k, v in general_hier_details.items())
        payload = json.dumps(payload)
        return payload

    def level_hier_payload(self):
        level = {
            "treeId": None,
            "name": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "metadataMappingId": "None",
            "salesOfficeTypeId": "None",
            "IS_UNDER_DIST": secrets.choice([True, False]),
            "fieldDisplayId": "None"
        }
        hier_lvl_details = BuiltIn().get_variable_value("${hier_lvl_details}")
        if hier_lvl_details is not None:
            level.update((k, v) for k, v in hier_lvl_details.items())
        BuiltIn().set_test_variable("${1st_hier_lvl}", level)
        return level
