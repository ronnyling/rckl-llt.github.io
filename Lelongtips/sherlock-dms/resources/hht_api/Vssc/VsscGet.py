""" Python File related to HHT VSSC API """
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL
from resources.restAPI.Common import APIMethod
from resources.Common import Common
import json

APP_URL = '-svc-qa.cfapps.jp10.hana.ondemand.com/api/v1.0/'
VSSC_END_POINT_URL = PROTOCOL + "vs-scorecard"

class VsscGet:
    """ Functions related to HHT VSSC GET/SYNC Request """

    @keyword("user retrieves VS Score Card using ${user_file}")
    def get_vs_score_card(self, user_file):
        url = "{0}comm/vs-scorecard".format(VSSC_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves VS Dynamic Call Card using ${user_file}")
    def get_vss_dynamic_call_card(self, user_file):
        url = "{0}comm/vs-dynamic-call-card".format(VSSC_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves VS Score Card Detail using ${user_file}")
    def get_vs_score_card_detail(self, user_file):
        url = "{0}comm/vs-scorecard-detail".format(VSSC_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves VS Customer using ${user_file}")
    def get_vs_customer(self, user_file):
        url = "{0}comm/vs-cust".format(VSSC_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves VS MSL Product Category using ${user_file}")
    def get_vs_msl_prod_category(self, user_file):
        url = "{0}comm/vs-msl-product-category".format(VSSC_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves VS MSL using ${user_file}")
    def get_vs_msl(self, user_file):
        url = "{0}comm/vs-msl".format(VSSC_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves VS Merchandising Audit using ${user_file}")
    def get_vs_merc_audit(self, user_file):
        url = "{0}comm/vs-merc-audit".format(VSSC_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves VS Scorecard History using ${user_file}")
    def get_vs_score_card_hist(self, user_file):
        url = "{0}comm/vs-scorecard-history".format(VSSC_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)