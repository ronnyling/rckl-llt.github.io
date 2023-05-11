from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Config.ReferenceData.ReasonType import ReasonWarehousePost
from resources.restAPI.MasterDataMgmt.Warehouse import WarehouseGet

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class ReasonWarehousePut(object):
    """ Functions to update warehouse in reason """

    @keyword("user updates reason warehouse with ${status}")
    def user_updates_reason_warehouse(self, status):
        """ Functions to update warehouse record"""
        res_bd_reason_type_id = BuiltIn().get_variable_value("${res_bd_reason_type_id}")
        res_bd_reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        res_bd_reason_wh_id = BuiltIn().get_variable_value("${res_bd_reason_wh_id}")
        url = "{0}setting-reasontype/{1}/setting-reason/{2}/setting-reason-whs/{3}" \
            .format(END_POINT_URL, res_bd_reason_type_id, res_bd_reason_id, res_bd_reason_wh_id)
        np_warehouse = WarehouseGet.WarehouseGet().user_gets_warehouse_by_using_type("NON_PRIME")
        BuiltIn().set_test_variable("${np_warehouse}", np_warehouse[0])
        payload = ReasonWarehousePost.ReasonWarehousePost().payload_reason_wh(status, 'both')
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            res_bd_reason_wh_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_reason_wh_id}", res_bd_reason_wh_id)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
