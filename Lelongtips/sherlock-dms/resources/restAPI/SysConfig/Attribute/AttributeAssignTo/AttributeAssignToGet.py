from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class AttributeAssignToGet(object):

    def user_gets_all_attribute_assign_to_data(self):
        url = "{0}module-data/attribute-assignment".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_attribute_assign_to(self, type):
        att_filter = {"ASSIGNED_TO": {"$eq": type}}
        att_filter = json.dumps(att_filter)
        url = "{0}module-data/attribute-assignment?filter={1}".format(END_POINT_URL, att_filter)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve attribute assign to"
        body_result = response.json()
        assign_to_id = body_result[0]['ID']
        BuiltIn().set_test_variable("${assign_to_id}", assign_to_id)
        return assign_to_id
