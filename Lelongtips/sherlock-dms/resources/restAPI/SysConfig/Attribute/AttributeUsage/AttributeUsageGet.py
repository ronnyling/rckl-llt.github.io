from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class AttributeUsageGet(object):

    @keyword('user retrieves ${condition} attribute usage')
    def user_retrieves_attribute_usage_data(self, condition):
        attribute_usage_id = BuiltIn().get_variable_value("${attribute_usage_id}")
        if condition == 'created':
            url = "{0}module-data/attribute-usage/{1}".format(END_POINT_URL, attribute_usage_id)
        else:
            url = "{0}module-data/attribute-usage".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response

    def user_retrieves_attribute_usage_using(self, type):
        filter_usage = {"USAGE": {"$eq": type}}
        filter_usage = json.dumps(filter_usage)
        url = "{0}module-data/attribute-usage?filter={1}".format(END_POINT_URL, filter_usage)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve attribute usage"
        body_result = response.json()
        usage_id = body_result[0]['ID']
        BuiltIn().set_test_variable("${usage_id}", usage_id)
        return usage_id
