""" Python File related to HHT Merchandising API """
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.Common import Common
import json

APP_URL_1_1 = '-svc-qa.cfapps.jp10.hana.ondemand.com/api/v1.1/'
MERCHANDISING_END_POINT_URL = PROTOCOL + "merchandising"

class MerchandisingGet:
    """ Functions related to HHT Merchandising GET/SYNC Request """

    @keyword("user retrieves Merchandising activity using ${user_file}")
    def get_merchandising_act(self, user_file):
        url = "{0}comm/merc-activity-base".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("User retrieves Merchandising activities using given access")
    def retrieves_merchandising_activities_by_given_access(self, user_role, expected_status_code):
        BuiltIn().run_keyword('user retrieves token access as ' + user_role)
        BuiltIn().run_keyword('user retrieves Merchandising activity')
        BuiltIn().run_keyword('expected return status code ' + expected_status_code)

    @keyword("user retrieves Merchandising activity history using ${user_file}")
    def get_merchandising_act_history(self, user_file):
        url = "{0}comm/merc-activity-hist".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("User retrieves Merchandising activity history using given access")
    def retrieves_merchandising_act_hist_by_given_access(self, user_role, expected_status_code):
        BuiltIn().run_keyword('user retrieves token access as ' + user_role)
        BuiltIn().run_keyword('user retrieves Merchandising activity history')
        BuiltIn().run_keyword('expected return status code ' + expected_status_code)

    @keyword("user retrieves Merch Product Group using ${user_file}")
    def get_merchandising_prod_group(self, user_file):
        url = "{0}comm/merc-prod-group".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Merch Store Space using ${user_file}")
    def get_merchandising_store_space(self, user_file):
        url = "{0}comm/merc-store-space".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Merch Store Space Level using ${user_file}")
    def get_merchandising_store_space_level(self, user_file):
        url = "{0}comm/merc-store-space-level".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Merch Route Activity using ${user_file}")
    def get_merchandising_route_activity(self, user_file):
        url = "{0}comm/merc-route-activity".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Merch Customer Assignment using ${user_file}")
    def get_merchandising_cust_assignment(self, user_file):
        url = "{0}comm/merc-cust-assignment".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Merch Audit using ${user_file}")
    def get_merchandising_audit(self, user_file):
        url = "{0}comm/merc-audit".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Merch Audit Customer using ${user_file}")
    def get_merchandising_audit_cust(self, user_file):
        url = "{0}comm/merc-audit-cust".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Merch Audit Attribute using ${user_file}")
    def get_merchandising_audit_attribute(self, user_file):
        url = "{0}comm/merc-audit-attribute".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Merch Distribution Check using ${user_file}")
    def get_merchandising_audit_distributor_check(self, user_file):
        url = "{0}comm/merc-audit-dist-check".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Merch Audit Price using ${user_file}")
    def get_merchandising_audit_price(self, user_file):
        url = "{0}comm/merc-audit-price".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Merch Audit Facing using ${user_file}")
    def get_merchandising_audit_facing(self, user_file):
        url = "{0}comm/merc-audit-facing".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Merch Audit Plano using ${user_file}")
    def get_merchandising_audit_plano(self, user_file):
        url = "{0}comm/merc-audit-plano".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Merch Audit Promo using ${user_file}")
    def get_merchandising_audit_promo(self, user_file):
        url = "{0}comm/merc-audit-promo".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Transaction Merch Price using ${user_file}")
    def get_merchandising_price(self, user_file):
        url = "{0}comm/txn-merc-price".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Transaction Merch Price Product using ${user_file}")
    def get_merchandising_price_prod(self, user_file):
        url = "{0}comm/txn-merc-price-prd".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Merc Checklist Header using ${user_file}")
    def get_merchandising_checklist_header(self, user_file):
        url = "{0}comm/merc-checklist-header".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Merc Checklist Details using ${user_file}")
    def get_merchandising_checklist_details(self, user_file):
        url = "{0}comm/merc-checklist-details".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Merc Checklist Customer using ${user_file}")
    def get_merchandising_checklist_cust(self, user_file):
        url = "{0}comm/merc-checklist-customer".format(MERCHANDISING_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqmerchandiser':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)