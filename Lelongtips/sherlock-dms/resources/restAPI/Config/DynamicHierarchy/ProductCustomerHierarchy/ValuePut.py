from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "dynamic-hierarchy" + APP_URL


class ValuePut(object):

    @keyword('user deletes node value')
    def user_deletes_node_value(self):
        hier_id = BuiltIn().get_variable_value("${hier_id}")  # get the hierarchy structure from StructureGet class
        node_id = BuiltIn().get_variable_value("${node_id}")  # get specified node ID to remove
        url = "{0}hierarchy/hier/{1}/nodes".format(END_POINT_URL, hier_id)
        payload = {"nodes": [node_id]}
        payload = json.dumps(payload)
        print("payload:", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
