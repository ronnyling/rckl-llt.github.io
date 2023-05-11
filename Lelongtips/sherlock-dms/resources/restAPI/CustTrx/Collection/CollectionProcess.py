import json

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from resources.Common import Common
from robot.api.deco import keyword
from setup.hanaDB import HanaDB

END_POINT_URL = PROTOCOL + "collection" + APP_URL


class CollectionProcess(object):
    """ Functions to process Collection"""

    @keyword('user processes ${type} collection by id')
    def user_processes_collection_by_id(self, type):
        """ Function to process collection """
        if type == "processed":
            dist_id = BuiltIn().get_variable_value("${distributor_id}")
        else:
            res_bd_inv = BuiltIn().get_variable_value("${res_bd_invoice_body_result}")
            dist_id = res_bd_inv['TXN_HEADER']['DIST_ID']
        created_col = BuiltIn().get_variable_value("${created_col}")
        col_id = created_col['COL_ID']
        col_id = Common().convert_string_to_id(col_id)
        headers = {
            'np-session': "27ea0ccb:688a61a9-80e1-4c6f-bae6-d2a6d28ceee6"
        }
        url = "{0}distributors/{1}/process-customer-collections".format(END_POINT_URL, dist_id)
        common = APIMethod.APIMethod()
        payload = [{"COLLECTION_ID": col_id}]
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload, **headers)

        if response.status_code == 202:
            body_result = response.json()
            print(body_result)
            query = "select CAST(ID as VARCHAR) from TXN_COLHDR where ID = '{0}'".format(Common().convert_id_to_string(col_id))
            HanaDB.HanaDB().connect_database_to_environment()
            HanaDB.HanaDB().check_if_exists_in_database_by_query(query)
            HanaDB.HanaDB().disconnect_from_database()
            BuiltIn().set_test_variable("${col_id}", col_id)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)


