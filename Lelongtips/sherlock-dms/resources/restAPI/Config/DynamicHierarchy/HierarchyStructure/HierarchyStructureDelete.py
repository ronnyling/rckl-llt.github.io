from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "dynamic-hierarchy" + APP_URL


class HierarchyStructureDelete(object):

    @keyword('user deletes ${cond} hierarchy structure')
    def user_deletes_hierarchy_structure(self, cond):
        if cond == "invalid":
            hier_id = COMMON_KEY.generate_random_id("0")
        else:
            hier_id = BuiltIn().get_variable_value("${hier_id}")
        url = "{0}structure/hier/{1}".format(END_POINT_URL, hier_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        if response.status_code == 200:
            response_dict = json.loads(response.text)
            print("Result: ", response_dict)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
