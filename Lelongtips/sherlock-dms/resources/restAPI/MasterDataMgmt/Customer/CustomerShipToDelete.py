from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL

CUST_END_POINT_URL = PROTOCOL + "profile-cust" + APP_URL


class CustomerShipToDelete(object):

    @keyword('user deletes ship to details')
    def user_deletes_ship_to_with(self):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        cust_id = BuiltIn().get_variable_value("${res_bd_cust_id}")
        if cust_id is None:
            cust_id = BuiltIn().get_variable_value("${cust_id}")
        ship_to_id = BuiltIn().get_variable_value("${ship_to_id}")
        url = "{0}distributors/{1}/customer/{2}/cust-shipto/{3}".format(CUST_END_POINT_URL, dist_id, cust_id, ship_to_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        assert response.status_code == 200
        BuiltIn().set_test_variable("${status_code}", response.status_code)
