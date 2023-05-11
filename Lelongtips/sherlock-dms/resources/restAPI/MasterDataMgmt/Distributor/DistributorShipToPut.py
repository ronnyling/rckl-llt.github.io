from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.Distributor.DistributorShipToPost import DistributorShipToPost

END_POINT_URL = PROTOCOL + "profile-dist" + APP_URL


class DistributorShipToPut(object):
    """ Functions to update Distributor Ship To """

    @keyword('user updates ship to with ${type} data')
    def user_updates_ship_to_with(self, type):
        """ Function to update ship to with random/fixed data"""
        dist_id = BuiltIn().get_variable_value("${dist_id}")
        shipto_id = BuiltIn().get_variable_value("${shipto_id}")
        url = "{0}distributors/{1}/shipto/{2}".format(END_POINT_URL, dist_id, shipto_id)
        payload = DistributorShipToPost().payload("update")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${shipto_id}", body_result['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)


