from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, TokenAccess
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json
import secrets
END_POINT_URL = PROTOCOL + "setting" + APP_URL
INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL

class WarehouseGet(object):
    """ Function to retrieve warehouse """
    DISTRIBUTOR_ID = "${distributor_id}"

    def user_gets_all_warehouse_data(self):
        """ Function to retrieve all warehouse record """
        distributor_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        url = "{0}distributors/{1}/warehouse".format(END_POINT_URL, distributor_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${whs_ls}", response.json())
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_gets_warehouse_by_using_id(self):
        """ Function to retrieve warehouse using given id """
        res_bd_warehouse_flag = BuiltIn().get_variable_value("${res_bd_warehouse_flag}")
        if res_bd_warehouse_flag == 'NON_PRIME':
            res_bd_warehouse_id = BuiltIn().get_variable_value("${res_bd_np_warehouse_id}")
        else:
            res_bd_warehouse_id = BuiltIn().get_variable_value("${res_bd_warehouse_id}")
        distributor_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        url = "{0}distributors/{1}/warehouse/{2}".format(END_POINT_URL, distributor_id, res_bd_warehouse_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_warehouse_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword("user gets ${wh_type} warehouse by using type")
    def user_gets_warehouse_by_using_type(self, wh_type):
        """ Function to retrieve warehouse using prime flag """
        filter_reason = {"PRIME_FLAG": {"$eq": wh_type}}
        filter_reason = json.dumps(filter_reason)
        str(filter_reason).encode(encoding='UTF-8', errors='strict')
        url = "{0}distributors/1/warehouse?filter={1}".format(END_POINT_URL, filter_reason)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to get warehouse by using type"
        body_result = response.json()
        if len(body_result) > 1:
            random_sel = secrets.choice(range(0, len(body_result)-1))
        else:
            random_sel = 0
        res_bd_wh_id = body_result[random_sel]['ID']
        return res_bd_wh_id, body_result

    @keyword("user retrieve warehouse by using code")
    def user_retrieves_warehouse_by_using_code(self, wh_code):
        """ Function to retrieve warehouse using prime flag """
        filter_reason = {"WHS_CD": {"$eq": wh_code}}
        filter_reason = json.dumps(filter_reason)
        str(filter_reason).encode(encoding='UTF-8', errors='strict')
        url = "{0}distributors/1/warehouse?filter={1}".format(END_POINT_URL, filter_reason)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve warehouse by using code"
        body_result = response.json()
        res_bd_wh_id = body_result[0]['ID']
        return res_bd_wh_id

    @keyword("user gets warehouse by ${data}")
    def user_gets_warehouse_by_using_data(self, data):
        """ Function to retrieve warehouse using prime flag """
        data = data.split(':')
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        filter_reason = {data[0]: {"$eq": data[1]}}
        filter_reason = json.dumps(filter_reason)
        str(filter_reason).encode(encoding='UTF-8', errors='strict')
        url = "{0}distributors/{1}/warehouse?filter={2}".format(END_POINT_URL, dist_id, filter_reason)
        print(url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve warehouse record"
        body_result = response.json()
        if body_result[0]['PRIME_FLAG'] == "NON_PRIME":
            BuiltIn().set_test_variable("${WAREHOUSE_ID_NP}", body_result[0]['ID'])
            print("SET",body_result[0]['ID'])
            print("", BuiltIn().get_variable_value("${WAREHOUSE_ID_NP}"))
        else:
            BuiltIn().set_test_variable("${WAREHOUSE_ID}", body_result[0]['ID'])
            print("SET",body_result[0]['ID'])
            print("", BuiltIn().get_variable_value("${WAREHOUSE_ID}"))
        return body_result[0]['ID'], body_result


    def get_warehouse_inventory(self):
        TokenAccess.TokenAccess().get_token_by_role("distadm")
        wh_id = BuiltIn().get_variable_value("${wh_id}")
        url = "{0}all-product-list/{1}/true".format(INVT_END_POINT_URL, wh_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve warehouse record"
        body_result = response.json()
        return body_result
