""" Python File related to HHT Distributor API """
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.Common import TokenAccess
from resources.Common import Common
import json

APP_URL_1_0 = '-svc-qa.cfapps.jp10.hana.ondemand.com/api/v1.0/'
DISTRIBUTOR_END_POINT_URL = PROTOCOL + "profile-dist"

class DistributorGet:
    """ Functions related to HHT Distributor GET/SYNC Request """

    @keyword("user gets distributor by using code '${dist_cd}'")
    def user_gets_distributor_by_using_code(self, dist_cd):
        """ Functions to retrieve distributor id by using distributor code """
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        filter_dist = {"DIST_CD": {"$eq": dist_cd}}
        filter_dist = json.dumps(filter_dist)
        str(filter_dist).encode(encoding='UTF-8', errors='strict')
        url = "{0}distributors?filter={1}".format(DISTRIBUTOR_END_POINT_URL + APP_URL, filter_dist)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve Distributor"
        body_result = response.json()
        distributor_id = body_result[0]['ID']
        BuiltIn().set_test_variable("${distributor_id}", distributor_id)
        BuiltIn().set_test_variable("${dist_cd}", dist_cd)

    @keyword("user retrieves Distributor Details using ${user_file}")
    def get_distributor(self, user_file):
        url = "{0}comm/distributors".format(DISTRIBUTOR_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Distributor Option Details using ${user_file}")
    def get_distributor_option(self, user_file):
        url = "{0}comm/option".format(DISTRIBUTOR_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Distributor Contact Details using ${user_file}")
    def get_distributor_contact(self, user_file):
        url = "{0}comm/contact".format(DISTRIBUTOR_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Distributor ShipTo Details using ${user_file}")
    def get_distributor_shipto(self, user_file):
        url = "{0}comm/shipto".format(DISTRIBUTOR_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Distributor Geo Tree Details using ${user_file}")
    def get_distributor_geo_tree(self, user_file):
        url = "{0}comm/distributor-geotree".format(DISTRIBUTOR_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)
