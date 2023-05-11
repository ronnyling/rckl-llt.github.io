from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL
from resources.restAPI.Common import APIMethod
from resources.Common import Common


APP_URL_1_0 = '-svc-intg.cfapps.jp10.hana.ondemand.com/api/v1.0/'
PICKLIST_END_POINT_URL = PROTOCOL + "picklist"
MESSAGE_END_POINT_URL = PROTOCOL + "message"
SETTING_END_POINT_URL = PROTOCOL + "setting"
PROMOTION_END_POINT_URL = PROTOCOL + "promotion"



class DeliveryRepGet:
    """ Functions related to HHT Playbook GET/SYNC Request """

    @keyword("user retrieves picklist")
    def get_picklist(self):
        url = "{0}comm/picklist".format(PICKLIST_END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves picklist cust invoice")
    def get_picklist_cust_invoice(self):
        url = "{0}comm/picklist-cust-invoice".format(PICKLIST_END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves picklist invoice")
    def get_picklist_invoice(self):
        url = "{0}comm/picklist-invoice".format(PICKLIST_END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves picklist delivery sheet")
    def get_picklist_delivery_sheet(self):
        url = "{0}comm/picklist-delivery-sheet".format(PICKLIST_END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves message")
    def get_message(self):
        url = "{0}comm/msg-setup".format(MESSAGE_END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves step of call")
    def get_steps_of_call(self):
        url = "{0}comm/steps-of-call".format(SETTING_END_POINT_URL + APP_URL_1_0)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

