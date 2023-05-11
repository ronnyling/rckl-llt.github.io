from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

END_POINT_URL = PROTOCOL + "dynamic-attribute" + APP_URL


class AttributeMappingGet(object):

    def user_gets_all_attribute_mapping_data(self):
        url = "{0}attribute-mapping".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_attribute_mapping_by_module_assigned(self, status, module, usage, assign):
        att_filter = {"STATUS": {"$eq": status}, "MODULE_SELECTION": {"$eq": module}, "USAGE": {"$eq": usage},
                  "ASSIGNED_TO": {"$eq": assign}}
        att_filter = json.dumps(att_filter)
        url = "{0}attribute-mapping?filter={1}".format(END_POINT_URL, att_filter)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 201, "Unable to retrieve attribute mapping correctly"
        body_result = response.json()
        assign_to_id = body_result[0]['ID']
        BuiltIn().set_test_variable("${mapping_respond}", body_result)
        return assign_to_id
