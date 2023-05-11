from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import secrets
from robot.libraries.BuiltIn import BuiltIn


END_POINT_URL = PROTOCOL + "dynamic-hierarchy" + APP_URL


class ValueGet(object):

    def get_all_values_from_hierarchy_tree(self):
        hier_id = BuiltIn().get_variable_value("${hier_id}")
        tree_id = BuiltIn().get_variable_value("${tree_id}")
        url = "{0}hierarchy/hier/{1}/tree/{2}".format(END_POINT_URL, hier_id, tree_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${hier_value_res_bd}", response.json())

    def get_value_by_random_data(self):
        res_bd = BuiltIn().get_variable_value("${hier_value_res_bd}")
        return secrets.choice(res_bd)['nodeId']
