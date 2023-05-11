from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL
from resources.restAPI.Common import APIMethod
from resources.Common import Common

APP_URL_1_1 = '-svc-intg.cfapps.jp10.hana.ondemand.com/api/v1.1/'
FEATURE_SETUP_END_POINT_URL = PROTOCOL + "setting"


class FeatureSetupGet:
    """ Functions related to HHT FeatureSetup GET/SYNC Request """

    @keyword("user retrieves feature setup")
    def get_feature_setup(self):
        url = "{0}comm/feature-setup".format(FEATURE_SETUP_END_POINT_URL + APP_URL_1_1)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

