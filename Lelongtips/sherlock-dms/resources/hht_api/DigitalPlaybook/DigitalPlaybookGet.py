from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL
from resources.restAPI.Common import APIMethod
from resources.Common import Common

APP_URL_1_0 = '-svc-intg.cfapps.jp10.hana.ondemand.com/api/v1.0/'
PLAYBOOK_END_POINT_URL = PROTOCOL + "message"


class DigitalPlaybookGet:
    """ Functions related to HHT Playbook GET/SYNC Request """

    @keyword("user retrieves playbook")
    def get_playbook(self):
        url = "{0}comm/playbk-setup".format(PLAYBOOK_END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves playbook content")
    def get_playbook_content(self):
        url = "{0}comm/playbk-setup-content".format(PLAYBOOK_END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves playbook assignment")
    def get_playbook_assignment(self):
        url = "{0}comm/playbk-cust".format(PLAYBOOK_END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves playbook content history")
    def get_playbook_content_history(self):
        url = "{0}comm/playbk-history".format(PLAYBOOK_END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)
