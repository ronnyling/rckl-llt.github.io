from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "product" + APP_URL


class UomDelete(object):
    """ Functions for Uom deletion """

    def user_deletes_uom_with_created_data(self):
        """ Function to delete uom with valid data """
        res_bd_uom_id = BuiltIn().get_variable_value("${res_bd_uom_id}")
        url = "{0}uom-setting/{1}".format(END_POINT_URL, res_bd_uom_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
