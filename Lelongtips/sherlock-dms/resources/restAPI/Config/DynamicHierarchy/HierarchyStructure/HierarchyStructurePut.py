from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
import json, secrets
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.HierarchyStructurePost import HierarchyStructurePost
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "dynamic-hierarchy" + APP_URL


class HierarchyStructurePut(object):

    @keyword('user updates ${prime_flag} hierarchy structure with ${cond} data')
    def user_updates_hierarchy_structure(self, hier_cond, data_cond):
        if hier_cond == "invalid":
            hier_id = COMMON_KEY.generate_random_id("0")
        else:
            hier_id = BuiltIn().get_variable_value("${hier_id}")

        url = "{0}structure/hier/{1}".format(END_POINT_URL, hier_id)
        common = APIMethod.APIMethod()
        payload = self.updates_payload()
        print("payload =", payload)
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            response_dict = json.loads(response.text)
            print("Result: ", response_dict)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def updates_payload(self):
        hier_rs_bd = BuiltIn().get_variable_value("${hier_rs_bd}")
        hier_rs_bd['hierStructure'] = hier_rs_bd['hierStruct']
        del hier_rs_bd['hierStruct']
        general_hier_details = BuiltIn().get_variable_value("${update_hier_details}")
        if general_hier_details is not None:
            hier_rs_bd.update((k, v) for k, v in general_hier_details.items())
        hier_rs_bd = json.dumps(hier_rs_bd)
        return hier_rs_bd