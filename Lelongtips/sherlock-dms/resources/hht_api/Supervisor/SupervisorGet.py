from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL
from resources.restAPI.Common import APIMethod
from resources.Common import Common

APP_URL_1_0 = '-svc-intg.cfapps.jp10.hana.ondemand.com/api/v1.0/'
END_POINT_URL = PROTOCOL + "customer-transfer"
MOBILE_END_POINT_URL = PROTOCOL + "mobile-comm-general"


class SupervisorGet:
    """ Functions related to HHT Supervisor GET/SYNC Request """

    @keyword("user retrieves route compliance exception")
    def get_route_compliance_exception(self):
        url = "{0}comm/supervisor-route-exception".format(END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves salesman no sales outlet")
    def get_salesman_no_sales_outlet(self):
        url = "{0}comm/view/supervisor-kpi-nosales-route".format(MOBILE_END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves salesman stale value")
    def get_salesman_stale_value(self):
        url = "{0}comm/view/supervisor-kpi-stale-route".format(MOBILE_END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves salesman average unique sku")
    def get_salesman_average_unique_sku(self):
        url = "{0}comm/view/supervisor-kpi-average-sku-route".format(MOBILE_END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves team weekly performance")
    def get_team_weekly_performance(self):
        url = "{0}comm/view/supervisor-kpi-team-week-perf".format(MOBILE_END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)
