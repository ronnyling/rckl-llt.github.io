import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "performance" + APP_URL

class MustSellListGet(object):

    @keyword('user retrieves all MSL data')
    def user_retrieves_all_msl(self):
        url = "{0}msl".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves MSL using ${type} id')
    def user_gets_msl_by_id(self, type):
        if type == "valid":
            res_bd_msl_id = BuiltIn().get_variable_value("${res_bd_msl_id}")
        else:
            res_bd_msl_id = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45))
        url = "{0}msl/{1}".format(END_POINT_URL, res_bd_msl_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_msl_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword('user retrieves MSL by ${type} assignment')
    def user_gets_msl_by_assignment(self, type):

        res_bd_msl_id = BuiltIn().get_variable_value("${res_bd_msl_id}")
        if type == "product":
            url = "{0}msl/{1}/msl-prd-hier".format(END_POINT_URL, res_bd_msl_id)
        elif type == "distributor":
            url = "{0}msl/{1}/msl-geo-node".format(END_POINT_URL, res_bd_msl_id)
        elif type == "route":
            url = "{0}msl/{1}/msl-route-optype".format(END_POINT_URL, res_bd_msl_id)
        elif type == "customer":
            url = "{0}msl/{1}/msl-cust-hier".format(END_POINT_URL, res_bd_msl_id)
        else:
            url = "{0}msl/{1}/msl-cust-attr".format(END_POINT_URL, res_bd_msl_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print ("result" , body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)