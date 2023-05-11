from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL
from resources.restAPI.Common import APIMethod
from resources.Common import Common

APP_URL_1_0 = '-svc-intg.cfapps.jp10.hana.ondemand.com/api/v1.0/'
END_POINT_URL = PROTOCOL + "salesorder"
MOBILE_END_POINT_URL = PROTOCOL + "mobile-comm-general"
MOBILE_SCHEMA_END_POINT_URL = PROTOCOL + "mobile-comm-schema"


class SamplingGet:
    """ Functions related to HHT Sampling GET/SYNC Request """

    @keyword("user retrieves sampling order header")
    def get_sampling_order_header(self):
        url = "{0}comm/salesorder-header/6".format(END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves sampling order detail")
    def g_sampling_order_detail(self):
        url = "{0}comm/salesorder-detail/6".format(END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves sampling order and invoice product history")
    def get_sampling_order_detail(self):
        url = "{0}comm/view/cust-txn-hist-prod".format(MOBILE_END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves sampling return invoice list")
    def get_sampling_return_invoice_list(self):
        url = "{0}modules/invoice-header".format(MOBILE_SCHEMA_END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)
