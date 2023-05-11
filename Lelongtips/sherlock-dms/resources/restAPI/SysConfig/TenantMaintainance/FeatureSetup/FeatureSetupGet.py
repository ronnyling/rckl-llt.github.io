from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json


END_POINT_URL = PROTOCOL + "setting" + APP_URL


class FeatureSetupGet(object):
    def user_retrieves_all_feature_setup(self):
        url = "{0}feature-setup".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve Feature Setup"
        body_result = response.json()
        BuiltIn().set_test_variable("${all_feature_setup_res}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_feature_setup(self, module):
        feature_setup_filter = {"FEATURE_CODE": {"$eq": module}}
        feature_setup_filter = json.dumps(feature_setup_filter)
        url = "{0}feature-setup?filter={1}".format(END_POINT_URL, feature_setup_filter)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve Feature Setup"
        body_result = response.json()[0]
        BuiltIn().set_test_variable("${feature_setup_res}", body_result)
