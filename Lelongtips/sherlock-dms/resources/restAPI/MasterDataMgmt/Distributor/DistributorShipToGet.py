import secrets

from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
import json

from resources.restAPI.MasterDataMgmt.Distributor.DistributorShipToPost import DistributorShipToPost
END_POINT_URL = PROTOCOL + "profile-dist" + APP_URL


class DistributorShipToGet(object):

    @keyword('user retrieves shipto details')
    def user_retrieves_all_shipto(self):
        dist_id = BuiltIn().get_variable_value("${dist_id}")
        url = "{0}distributors/{1}/shipto".format(END_POINT_URL, dist_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Result: ", body_result)
            shipto_id = body_result[0]['ID']
            BuiltIn().set_test_variable("${shipto_id}", shipto_id)
            BuiltIn().set_test_variable("${shipto_ls}", body_result)
            print("shiptoID from distget: ", shipto_id)
            return str(shipto_id)

        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword('user retrieves shipto details by id')
    def user_retrieves_shipto_details(self):
        dist_id = BuiltIn().get_variable_value("${dist_id}")
        shipto_ls = BuiltIn().get_variable_value("${shipto_ls}")
        if shipto_ls is None:
            DistributorShipToPost().user_creates_ship_to_with()
            shipto_id = BuiltIn().get_variable_value("${shipto_id}")
        else:
            shipto_id = secrets.choice((shipto_ls))['ID']
        url = "{0}distributors/{1}/shipto/{2}".format(END_POINT_URL, dist_id, shipto_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Result: ", body_result)
            return str(body_result)

        BuiltIn().set_test_variable("${status_code}", response.status_code)
