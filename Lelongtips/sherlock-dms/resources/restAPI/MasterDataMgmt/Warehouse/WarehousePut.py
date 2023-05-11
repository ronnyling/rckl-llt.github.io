from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Warehouse import WarehousePost
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword


END_POINT_URL = PROTOCOL + "setting" + APP_URL


class WarehousePut(object):
    """ Functions to update warehouse """

    @keyword('user updates warehouse with ${data_type} data')
    def user_updates_warehouse_with(self, data_type):
        """ Function to update warehouse using fixed/random data """
        res_bd_warehouse_flag = BuiltIn().get_variable_value("${res_bd_warehouse_flag}")
        if res_bd_warehouse_flag == 'NON_PRIME':
            res_bd_warehouse_id = BuiltIn().get_variable_value("${res_bd_np_warehouse_id}")
        else:
            res_bd_warehouse_id = BuiltIn().get_variable_value("${res_bd_warehouse_id}")
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/warehouse/{2}".format(END_POINT_URL, distributor_id, res_bd_warehouse_id)
        payload = WarehousePost.WarehousePost().payload_warehouse("update")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            res_bd_warehouse_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_warehouse_id}", res_bd_warehouse_id)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
