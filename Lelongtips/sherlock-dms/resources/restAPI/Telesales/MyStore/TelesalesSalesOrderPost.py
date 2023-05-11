import json

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class TelesalesSalesOrderPost(object):

    @keyword("user post ${data_type} ${data_state} sales order product list")
    def user_retrieves_master_product_hierarchy_list(self, data_type, data_state):
        details = BuiltIn().get_variable_value("${AppSetupDetails}")
        url = "{0}telesales/transaction/product".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.payload(data_type,data_state)
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload)
        body_result = response.json()
        print("Response is: ", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def payload(self, data_type, data_state):

        customer_id = BuiltIn().get_variable_value("${cust_id}")
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        route_id = BuiltIn().get_variable_value("${route_id}")
        node_id = BuiltIn().get_variable_value("${res_bd_node_id}")

        if data_state == 'invalid':
            customer_id = ""
            distributor_id = ""
            route_id = ""
            node_id = ""
        payload = {
            "CUST_ID": customer_id,
            "DIST_ID": distributor_id,
            "ROUTE_ID": route_id,
            "NODE_ID": node_id
        }
        print("PAYLOAD IS: ", payload)
        return payload
