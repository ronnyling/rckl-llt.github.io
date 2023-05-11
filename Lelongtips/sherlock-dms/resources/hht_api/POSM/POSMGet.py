""" Python File related to HHT POSM API """
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL
from resources.restAPI.Common import APIMethod
import json

APP_URL = '-svc-qa.cfapps.jp10.hana.ondemand.com/api/v1.0/'
POSM_END_POINT_URL = PROTOCOL + "posm-management"

class POSMGet:
    """ Functions related to HHT POSM GET/SYNC Request """

    @keyword("user retrieves POSM Focused Customer using ${user_file}")
    def get_posm_focused_customer(self, user_file):
        url = "{0}comm/posm-focused-customers".format(POSM_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value('${distributor_id}')}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword("user retrieves POSM Customer using ${user_file}")
    def get_posm_customer(self, user_file):
        url = "{0}comm/customer-posm".format(POSM_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value('${distributor_id}')}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable("${status_code}", response.status_code)