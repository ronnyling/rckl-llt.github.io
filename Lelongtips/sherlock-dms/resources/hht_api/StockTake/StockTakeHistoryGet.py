from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL
from resources.restAPI.Common import APIMethod
from resources.Common import Common

APP_URL_1_0 = '-svc-intg.cfapps.jp10.hana.ondemand.com/api/v1.0/'
END_POINT_URL = PROTOCOL + "mobile-comm-general"


class StockTakeHistoryGet:
    """ Functions related to HHT Stock Take GET/SYNC Request """

    @keyword("user retrieves stock take history")
    def get_stock_take_history(self):
        url = "{0}comm/view/cust-stktake-hist-loc".format(END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

