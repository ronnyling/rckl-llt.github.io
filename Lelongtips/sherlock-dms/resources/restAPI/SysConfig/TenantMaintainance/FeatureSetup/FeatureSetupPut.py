from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, TokenAccess
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.SysConfig.TenantMaintainance.FeatureSetup.FeatureSetupGet import FeatureSetupGet
import json


END_POINT_URL = PROTOCOL + "setting" + APP_URL


class FeatureSetupPut(object):

    @keyword('user update ${module} feature setup')
    def user_put_feature_setup(self, module):
        url = "{0}feature-setup/".format(END_POINT_URL)
        payload = self.feature_setup_payload(module.upper())
        print("payload", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        assert response.status_code == 200, "Unable to update feature setup"
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def feature_setup_payload(self, module):
        FeatureSetupGet().user_retrieves_feature_setup(module)
        module_feature_setup_rs = BuiltIn().get_variable_value("${feature_setup_res}")
        feature_details = BuiltIn().get_variable_value("${feature_details}")
        module_feature_setup_rs.update((k, v) for k, v in feature_details.items())
        FeatureSetupGet().user_retrieves_all_feature_setup()
        all_feature_setup_res = BuiltIn().get_variable_value("${all_feature_setup_res}")
        count = 0
        for item in all_feature_setup_res:
            if item['FEATURE_CODE'] == module_feature_setup_rs['FEATURE_CODE']:
                all_feature_setup_res[count] = module_feature_setup_rs
            count = count + 1
        all_feature_setup_res = json.dumps(all_feature_setup_res)
        return all_feature_setup_res

    @keyword("User sets the feature setup for ${module} to ${cond} passing with '${value}' value")
    def user_set_feature_setup_on_or_off(self, module, cond, value):
        cond = cond.upper()
        TokenAccess.TokenAccess().user_retrieves_token_access_as("sysimp")
        if cond == "ON":
            feature_details = {
                "IS_VISIBLE": True,
                "IS_PARENT": False,
                "IS_ENABLED": True
            }
        else:
            feature_details = {
                "IS_VISIBLE" : False,
                "IS_PARENT": False,
                "IS_ENABLED": False
            }
        BuiltIn().set_test_variable("${feature_details}", feature_details)
        self.user_put_feature_setup(value)


