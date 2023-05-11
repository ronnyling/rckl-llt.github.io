from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import TokenAccess, APIMethod
from setup.hanaDB import HanaDB
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Config.ReferenceData.ReasonType import ReasonTypeGet
from resources.restAPI.Config.ReferenceData.ReasonType import ReasonPost
from resources.restAPI.MasterDataMgmt.Warehouse import WarehouseGet
import json

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class ReasonWarehousePost(object):
    """ Functions to assign warehouse to reason """

    @keyword('user assigns ${type} warehouse to reason')
    def user_assigns_warehouse_to_reason(self, type):
        """ Functions to assign warehouse using given/random reason"""
        res_bd_reason_type_id = BuiltIn().get_variable_value("${res_bd_reason_type_id}")
        res_bd_reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        url = "{0}setting-reasontype/{1}/setting-reason/{2}/setting-reason-whs" \
            .format(END_POINT_URL, res_bd_reason_type_id, res_bd_reason_id)
        payload = self.payload_reason_wh("", type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            res_bd_reason_wh_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_reason_wh_id}", res_bd_reason_wh_id)
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().user_validates_database_data("setting-reason-whs", body_result)
            # HanaDB.HanaDB().disconnect_from_database()
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_reason_wh(self, status, type):
        """ Functions for reason payload content """
        np_warehouse = None
        prime_warehouse = BuiltIn().get_variable_value("${prime_warehouse}")
        if type != 'Prime':
            np_warehouse = BuiltIn().get_variable_value("${np_warehouse}")
        payload = {
            "WAREHOUSE_ID": prime_warehouse,
            "WAREHOUSE_ID_NP": np_warehouse
        }

        if status == 'invalid warehouse':
            payload['WAREHOUSE_ID'] = np_warehouse
            payload['WAREHOUSE_ID_NP'] = prime_warehouse
        payload = json.dumps(payload)
        print("Reason Warehouse Payload: ", payload)
        return payload

    @keyword("user creates prerequisite for reason '${reason_type}'")
    def user_creates_prerequisite_for_reason(self, reason_type):
        """ Functions for creating/retrieving data for warehouse reason assignment """
        ReasonTypeGet.ReasonTypeGet().user_retrieves_reason_type(reason_type)
        ReasonPost.ReasonPost().user_creates_reason_with("random")
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        prime_warehouse = WarehouseGet.WarehouseGet().user_gets_warehouse_by_using_type("PRIME")
        np_warehouse = WarehouseGet.WarehouseGet().user_gets_warehouse_by_using_type("NON_PRIME")
        BuiltIn().set_test_variable("${prime_warehouse}", prime_warehouse[0])
        BuiltIn().set_test_variable("${np_warehouse}", np_warehouse[0])
