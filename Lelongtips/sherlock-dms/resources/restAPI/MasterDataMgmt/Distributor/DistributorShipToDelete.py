from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "profile-dist" + APP_URL


class DistributorShipToDelete(object):
    """ Functions to delete Distributor Ship To """

    @keyword('user deletes ship to')
    def user_deletes_ship_to(self):
        """ Function to delete ship to """
        dist_id = BuiltIn().get_variable_value("${dist_id}")
        shipto_id = BuiltIn().get_variable_value("${shipto_id}")
        url = "{0}distributors/{1}/shipto/{2}".format(END_POINT_URL, dist_id, shipto_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)


