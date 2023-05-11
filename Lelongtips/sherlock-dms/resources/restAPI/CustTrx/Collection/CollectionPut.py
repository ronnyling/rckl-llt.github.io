import json

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.CustTrx.Collection.CollectionPost import CollectionPost
from resources.Common import Common
from setup.hanaDB import HanaDB


END_POINT_URL = PROTOCOL + "collection" + APP_URL


class CollectionPut(object):
    """ Functions to update Collection"""

    @keyword('user updates collection with ${type} data')
    def user_updates_collection(self, type):
        """ Function to update collection with random/fixed data"""
        created_col = BuiltIn().get_variable_value("${created_col}")
        col_id = created_col['COL_ID']
        cust_id = created_col['CUST_ID']
        route_id = created_col['ROUTE_ID']
        prime_flag = created_col['PRIME_FLAG']
        payload = CollectionPost().get_collection_payload(cust_id, route_id, prime_flag, "")
        url = "{0}update-customer-collection/{1}".format(END_POINT_URL, Common().convert_string_to_id(col_id))
        common = APIMethod.APIMethod()
        headers = {
            'np-session': "27ea0ccb:688a61a9-80e1-4c6f-bae6-d2a6d28ceee6"
        }
        response = common.trigger_api_request("PUT", url, json.dumps(payload), **headers)
        if response.status_code == 202:
            body_result = response.json()
            print("Body Result = ", body_result)
            query = "select * from TXN_COLHDR where ID ={0}".format(col_id)
            HanaDB.HanaDB().connect_database_to_environment()
            HanaDB.HanaDB().check_if_exists_in_database_by_query(query)
            HanaDB.HanaDB().disconnect_from_database()
        BuiltIn().set_test_variable("${status_code}", response.status_code)

