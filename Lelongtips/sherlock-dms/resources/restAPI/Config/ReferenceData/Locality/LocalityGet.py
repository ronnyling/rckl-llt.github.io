import json

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "metadata" + APP_URL
END_POINT_URL_NEW = PROTOCOL + "setting" + APP_URL


class LocalityGet(object):
    """ Functions to retrieve locality records """

    def user_gets_all_localities_data(self):
        """ Function to retrieve all locality data """
        url = "{0}module-data/address-city".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${locality_br}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_gets_locality_by_using_id(self):
        """ Function to retrieve locality data by using id """
        res_bd_locality_id = BuiltIn().get_variable_value("${res_bd_locality_id}")
        url = "{0}module-data/address-city/{1}".format(END_POINT_URL, res_bd_locality_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_locality_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_gets_all_localities_data_new(self):
        """ Function to retrieve all locality data """
        body_result = None
        url = "{0}address-city".format(END_POINT_URL_NEW)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${locality_br}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return body_result
