from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class ReasonWarehouseGet(object):
    """ Functions to retrieve warehouse assign to reason """

    def user_retrieves_reason_warehouse(self):
        """ Functions to retrieve all warehouse assigned """
        res_bd_reason_type_id = BuiltIn().get_variable_value("${res_bd_reason_type_id}")
        res_bd_reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}setting-reasontype/{1}/setting-reason/{2}/setting-reason-whs" \
            .format(END_POINT_URL, res_bd_reason_type_id, res_bd_reason_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        print("RESPONSE IS ,", response.json())
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            for x in body_result:
                if x["DIST_ID"] == dist_id:
                    BuiltIn().set_test_variable("${WAREHOUSE_ID}", x['WAREHOUSE_ID'])
                    BuiltIn().set_test_variable("${WAREHOUSE_ID_NP}", x['WAREHOUSE_ID_NP'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_gets_reason_warehouse_by_using_id(self):
        """ Function to retrieve reason warehouse data by using id """
        res_bd_reason_type_id = BuiltIn().get_variable_value("${res_bd_reason_type_id}")
        res_bd_reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        res_bd_reason_wh_id = BuiltIn().get_variable_value("${res_bd_reason_wh_id}")
        url = "{0}setting-reasontype/{1}/setting-reason/{2}/setting-reason-whs/{3}" \
            .format(END_POINT_URL, res_bd_reason_type_id, res_bd_reason_id, res_bd_reason_wh_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_reason_wh_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)
