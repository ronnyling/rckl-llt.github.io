from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class VanGet(object):
    """ Functions to retrieve van records """

    def user_gets_all_van_data(self):
        """ Function to retrieve all van record """
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/setting-van".format(END_POINT_URL, distributor_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_gets_van_by_using_id(self):
        """ Function to retrieve van given id """
        res_bd_van_id = BuiltIn().get_variable_value("${res_bd_van_id}")
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/setting-van/{2}".format(END_POINT_URL, distributor_id, res_bd_van_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${van_get_body_results}", body_result)
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_van_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_gets_van_id_by_using_code(self, dist_id, van_cd):
        """Function to retrieve van given id by using code"""
        filter_van = {"VAN_CD": {"$eq": van_cd}}
        filter_van = json.dumps(filter_van)
        str(filter_van).encode(encoding='UTF-8', errors='strict')
        url = "{0}distributors/{1}/setting-van?filter={2}".format(END_POINT_URL, dist_id, filter_van)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Van ID not retrieved"
        if response.status_code == 200:
            body_result = response.json()
            van_id = body_result[0]["ID"]
        return van_id
