import secrets
import json

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from setup.hanaDB import HanaDB
from resources.Common import Common

END_POINT_URL = PROTOCOL + "collection" + APP_URL


class CollectionGet(object):
    """ Functions to retrieve Collection open item """

    def user_retrieves_all_collection(self):
        """ Function to retrieve all collection """
        url = "{0}customer-collection".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_so = secrets.randbelow(len(body_result))
            else:
                rand_so = 0
            BuiltIn().set_test_variable("${rand_col_selection}", body_result[rand_so]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves collection by ${type} id')
    def user_retrieves_collection_by_id(self, type):
        """ Function to retrieve collection by using id. """
        if type == "random":
            self.user_retrieves_all_collection()
            collection_id = BuiltIn().get_variable_value("${rand_col_selection}")
        else:
            collection_id = type
        url = "{0}customer-invoices-collection/{1}".format(END_POINT_URL, collection_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        assert self.picklist_details_available(collection_id), "Picklist details not available"

    @keyword('user retrieves collection by ${key} = ${value}')
    def user_gets_collection_by_using_field(self, key, value):
        """ Function to retrieve collection using field """
        filter_reason = {key: {"$eq": value}}
        filter_reason = json.dumps(filter_reason)
        str(filter_reason).encode(encoding='UTF-8', errors='strict')
        url = "{0}customer-collection?filter={1}".format(END_POINT_URL, filter_reason)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to get collection by using key and value"
        body_result = response.json()
        if len(body_result) > 1:
            random_sel = secrets.choice(range(0, len(body_result) - 1))
        else:
            random_sel = 0
        res_bd_collection_id = body_result[random_sel]['ID']
        res_bd_cust_id = body_result[random_sel]['CUST_ID']
        res_bd_route_id = body_result[random_sel]['ROUTE_ID']
        res_bd_prime_flag = body_result[random_sel]['PRIME_FLAG']
        created_col = {
            "COL_ID": res_bd_collection_id,
            "CUST_ID": res_bd_cust_id,
            "ROUTE_ID": res_bd_route_id,
            "PRIME_FLAG": res_bd_prime_flag
        }
        BuiltIn().set_test_variable("${created_col}", created_col)
        BuiltIn().set_test_variable("${distributor_id}", self.get_distributor_id_by_collection_id(res_bd_collection_id))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return res_bd_collection_id

    def get_distributor_id_by_collection_id(self, col_id):
        query = "select CAST(DIST_ID as VARCHAR) from TXN_COLHDR where ID = '{0}'".format(
            Common().convert_id_to_string(col_id))
        HanaDB.HanaDB().connect_database_to_environment()
        dist_id = HanaDB.HanaDB().fetch_one_record(query)
        HanaDB.HanaDB().disconnect_from_database()
        return dist_id

    def picklist_details_available(self, col_id):
        """ Function to retrieve collection by using id. """
        url = "{0}picklist-details".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        body_result = response.json()
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)


        picklist_available = False
        if response.status_code == 200:
            picklist_available = True
        return picklist_available
