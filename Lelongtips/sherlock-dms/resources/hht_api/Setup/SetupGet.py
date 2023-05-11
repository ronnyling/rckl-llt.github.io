""" Python File related to HHT Setup API """
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.Common import Common
import json

APP_URL_1_1 = '-svc-qa.cfapps.jp10.hana.ondemand.com/api/v1.1/'
SETTING_END_POINT_URL = PROTOCOL + "setting"
MOBILE_COMM_END_POINT_URL = PROTOCOL + "mobile-comm-general"
INVENTORY_END_POINT_URL = PROTOCOL + "inventory"
MESSAGE_END_POINT_URL = PROTOCOL + "message"

class SetupGet:
    """ Functions related to HHT Setup GET/SYNC Request """

    @keyword("user retrieves Step Of Call Setup using ${user_file}")
    def get_soc_setup(self, user_file):
        url = "{0}comm/steps-of-call".format(SETTING_END_POINT_URL + APP_URL_1_1)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves promotion sequence using ${user_file}")
    def get_settings_promotion_sequence(self, user_file):
        url = "{0}comm/promotion-sequence".format(SETTING_END_POINT_URL + APP_URL_1_1)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves activity assignment using ${user_file}")
    def get_activity_assignment(self, user_file):
        url = "{0}comm/activity-assignment".format(SETTING_END_POINT_URL + APP_URL_1_1)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Merchandising Step of Call using ${user_file}")
    def get_merch_step_of_call(self, user_file):
        url = "{0}comm/merc-steps-of-call".format(SETTING_END_POINT_URL + APP_URL_1_1)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves aging term using ${user_file}")
    def get_aging_term(self, user_file):
        url = "{0}aging-term".format(SETTING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves setting invoice term using ${user_file}")
    def get_setting_invoice_term(self, user_file):
        url = "{0}setting-invoice-term".format(SETTING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)
        BuiltIn().set_test_variable("${invoice_term_ls}", response.json())

    @keyword("user retrieves setting invoice term detail using ${user_file}")
    def get_comm_setting_invoice_term_detail(self, user_file):
        url = "{0}comm/setting-invoice-term-detail".format(SETTING_END_POINT_URL + APP_URL_1_1)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves invoice term details")
    def get_setting_invoice_term_detail(self):
        url = "{0}invoice-term-detail".format(SETTING_END_POINT_URL + APP_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves bank setting using ${user_file}")
    def get_bank_setting(self, user_file):
        url = "{0}bank".format(SETTING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves van setting")
    def get_van_setting(self):
        url = "{0}comm/setting-van".format(SETTING_END_POINT_URL + APP_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves warehouse setting using ${user_file}")
    def get_warehouse_setting(self, user_file):
        url = "{0}comm/warehouse".format(INVENTORY_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves warehouse product stock using ${user_file}")
    def get_warehouse_product_stock(self, user_file):
        url = "{0}comm/warehouse-product-stock".format(INVENTORY_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves message setup")
    def get_message_setup(self):
        url = "{0}comm/msg-setup".format(MESSAGE_END_POINT_URL + APP_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves message assignment")
    def get_message_assginment(self):
        url = "{0}comm/msg-assignment".format(MESSAGE_END_POINT_URL + APP_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves application setup")
    def get_app_setup(self):
        url = "{0}setup-apps".format(MOBILE_COMM_END_POINT_URL + APP_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves application setup reference")
    def get_app_setup_reference(self):
        url = "{0}setup-reference".format(MOBILE_COMM_END_POINT_URL + APP_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves application setup parameter")
    def get_app_setup_parameter(self):
        url = "{0}setup-params".format(MOBILE_COMM_END_POINT_URL + APP_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)



    @keyword("user retrieves tenant logo using ${user_file}")
    def get_tenant_logo(self, user_file):
        url = "{0}comm/attachment/application-setup".format(SETTING_END_POINT_URL + APP_URL_1_1)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves route distributor warehouse using ${user_file}")
    def get_route_distributor_warehouse(self, user_file):
        url = "{0}comm/route-distributor-warehouse".format(INVENTORY_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

