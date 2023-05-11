from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
import secrets

END_POINT_URL = PROTOCOL + "performance" + APP_URL

class MustSellListDelete(object):
    STATUS_CODE = "${status_code}"
    MSL_ID = "${res_bd_msl_id}"

    @keyword('user deletes MSL using ${type} id')
    def user_deletes_msl(self, type):
        if type == "valid":
            res_bd_msl_id = BuiltIn().get_variable_value(self.MSL_ID)
        else:
            res_bd_msl_id = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45))
        url = "{0}msl/{1}".format(END_POINT_URL, res_bd_msl_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(self.STATUS_CODE, response.status_code)

    @keyword('user deletes prod hierarchy assignment in MSL')
    def user_deletes_msl_prod_hier(self):
        res_bd_msl_id = BuiltIn().get_variable_value(self.MSL_ID)
        res_bd_prod_hier_id = BuiltIn().get_variable_value("${res_bd_prod_hier_id}")
        url = "{0}msl/{1}/msl-prd-hier/{2}".format(END_POINT_URL, res_bd_msl_id, res_bd_prod_hier_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(self.STATUS_CODE, response.status_code)

    @keyword('user deletes distributor assignment in MSL')
    def user_deletes_msl_dist_asg(self):
        res_bd_msl_id = BuiltIn().get_variable_value(self.MSL_ID)
        res_bd_msl_geo_id = BuiltIn().get_variable_value("${res_bd_msl_geo_id}")
        url = "{0}msl/{1}/msl-geo-node/{2}".format(END_POINT_URL, res_bd_msl_id, res_bd_msl_geo_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(self.STATUS_CODE, response.status_code)

    @keyword('user deletes route operation assignment in MSL')
    def user_deletes_msl_route_op(self):
        res_bd_msl_id = BuiltIn().get_variable_value(self.MSL_ID)
        res_bd_msl_route_op_id = BuiltIn().get_variable_value("${res_bd_msl_route_op_id}")
        url = "{0}msl/{1}/msl-route-optype/{2}".format(END_POINT_URL, res_bd_msl_id, res_bd_msl_route_op_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(self.STATUS_CODE, response.status_code)

    @keyword('user deletes cust hierarchy in MSL')
    def user_deletes_msl_cust_hier(self):
        res_bd_msl_id = BuiltIn().get_variable_value(self.MSL_ID)
        res_bd_msl_cust_id = BuiltIn().get_variable_value("${res_bd_msl_cust_id}")
        url = "{0}msl/{1}/msl-cust-hier/{2}".format(END_POINT_URL, res_bd_msl_id, res_bd_msl_cust_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(self.STATUS_CODE, response.status_code)

    @keyword('user deletes attribute in MSL')
    def user_deletes_msl_attribute(self):
        res_bd_msl_id = BuiltIn().get_variable_value(self.MSL_ID)
        res_bd_msl_attr_id = BuiltIn().get_variable_value("${res_bd_msl_attr_id}")
        url = "{0}msl/{1}/msl-cust-attr/{2}".format(END_POINT_URL, res_bd_msl_id, res_bd_msl_attr_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(self.STATUS_CODE, response.status_code)