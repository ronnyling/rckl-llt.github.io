""" Python File related to HHT Transaction API """
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.Common import Common
import json

APP_URL_1_1 = '-svc-qa.cfapps.jp10.hana.ondemand.com/api/v1.1/'
INVOICE_END_POINT_URL = PROTOCOL + "invoice"
SALESORDER_END_POINT_URL = PROTOCOL + "salesorder"
CUSTOMER_END_POINT_URL = PROTOCOL + "profile-cust"

class TransactionGet:
    """ Functions related to HHT Transaction GET/SYNC Request """

    @keyword("user retrieves invoice balance details")
    def get_invoice_balance_details(self):
        url = "{0}comm/invoice-balance-detail".format(INVOICE_END_POINT_URL + APP_URL_1_1)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves invoice balance promotion")
    def get_invoice_balance_promo(self):
        url = "{0}comm/invoice-balance-promo".format(INVOICE_END_POINT_URL + APP_URL_1_1)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves invoice balance FOC")
    def get_invoice_balance_foc(self):
        url = "{0}comm/invoice-balance-promo-foc".format(INVOICE_END_POINT_URL + APP_URL_1_1)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves invoice header using ${user_file}")
    def get_invoice_header(self, user_file):
        url = "{0}comm/invoice-header".format(INVOICE_END_POINT_URL + APP_URL_1_1)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves invoice details using ${user_file}")
    def get_invoice_details(self, user_file):
        url = "{0}comm/invoice-detail".format(INVOICE_END_POINT_URL + APP_URL_1_1)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves invoice details tax using ${user_file}")
    def get_invoice_details_tax(self, user_file):
        url = "{0}comm/invoice-detail-tax".format(INVOICE_END_POINT_URL + APP_URL_1_1)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves invoice promotion using ${user_file}")
    def get_invoice_promotion(self, user_file):
        url = "{0}comm/invoice-promo".format(INVOICE_END_POINT_URL + APP_URL_1_1)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves invoice FOC promotion using ${user_file}")
    def get_invoice_foc_promotion(self, user_file):
        url = "{0}comm/invoice-promo-foc".format(INVOICE_END_POINT_URL + APP_URL_1_1)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves invoice FOC promotion using given access")
    def retrieves_invoice_foc_promo_using_given_access(self, user_role, expected_status_code):
        BuiltIn().run_keyword('user retrieves token access as ' + user_role)
        BuiltIn().run_keyword('user retrieves invoice balance FOC')
        BuiltIn().run_keyword('expected return status code ' + expected_status_code)

    @keyword("user retrieves invoice details using given access")
    def retrieves_invoice_details_using_given_access(self, user_role, expected_status_code):
        BuiltIn().run_keyword('user retrieves token access as ' + user_role)
        BuiltIn().run_keyword('user retrieves invoice details')
        BuiltIn().run_keyword('expected return status code ' + expected_status_code)

    @keyword("user retrieves Sales Order using ${user_file}")
    def get_all_sales_order_header(self, user_file):
        url = "{0}comm/salesorder-header".format(SALESORDER_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves first ${num} Sales Order Header using ${user_file}")
    def get_first_x_sales_order_header(self, num, user_file):
        url = "{0}comm/salesorder-header/{1}".format(SALESORDER_END_POINT_URL + APP_URL, num)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves first ${num} Sales Order Detail using ${user_file}")
    def get_first_x_sales_order_detail(self, num, user_file):
        url = "{0}comm/salesorder-detail/{1}".format(SALESORDER_END_POINT_URL + APP_URL, num)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Customer Sales Order Invoice using ${user_file}")
    def get_customer_sales_order_invoice(self, user_file):
        url = "{0}comm/cust-so-inv".format(SALESORDER_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves invoice balance product using ${user_file}")
    def get_invoice_balance_product(self, user_file):
        url = "{0}comm/invoice-balance-product".format(INVOICE_END_POINT_URL + APP_URL_1_1)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves invoice balance promotion using ${user_file}")
    def get_invoice_balance_promo(self, user_file):
        url = "{0}comm/invoice-balance-promo".format(INVOICE_END_POINT_URL + APP_URL_1_1)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves invoice balance promotion FOC using ${user_file}")
    def get_invoice_balance_promo_foc(self, user_file):
        url = "{0}comm/invoice-balance-promo-foc".format(INVOICE_END_POINT_URL + APP_URL_1_1)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Customer Open Item using ${user_file}")
    def get_cust_open_item(self, user_file):
        url = "{0}comm/openitems".format(CUSTOMER_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)