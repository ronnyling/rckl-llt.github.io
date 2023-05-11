from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class WarehouseDelete(object):
    """ Functions to delete warehouse """

    @keyword('user deletes warehouse with ${data_type} data')
    def user_deletes_warehouse_with_data(self, data_type):
        """ Function to delete warehouse using given id """
        res_bd_warehouse_id = BuiltIn().get_variable_value("${res_bd_warehouse_id}")
        if data_type == "invalid":
            res_bd_warehouse_id = BuiltIn().get_variable_value("${invalid_warehouse_id}")
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/warehouse/{2}".format(END_POINT_URL, distributor_id, res_bd_warehouse_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
