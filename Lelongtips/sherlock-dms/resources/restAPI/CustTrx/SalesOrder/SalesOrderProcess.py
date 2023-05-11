import json
import time

from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from setup.hanaDB import HanaDB

END_POINT_URL = PROTOCOL + "salesorder" + APP_URL


class SalesOrderProcess(object):
    SO_ID = "${res_bd_sales_order_id}"

    def user_process_the_sales_order(self):
        url = "{0}processOrder".format(END_POINT_URL)
        payload = self.payload_process_so()
        common = APIMethod.APIMethod()
        rand_string = COMMON_KEY.generate_random_id("0")
        headers = {
            'np-session': rand_string
        }
        response = common.trigger_api_request("POST", url, payload, **headers)
        print("Process sales order and getting status code " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.text)
        if response.status_code != 202:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            message_get = body_result['message']
            assert message_get == 'request successfully processed'

    def payload_process_so(self):
        res_bd_sales_order_id = BuiltIn().get_variable_value(self.SO_ID)
        route_id = BuiltIn().get_variable_value("${route_id}")
        distributor_id = BuiltIn().get_variable_value("${dist_id}")
        customer_id = BuiltIn().get_variable_value("${cust_id}")
        BuiltIn().set_test_variable("${distributor_id}", distributor_id)
        BuiltIn().set_test_variable("${customer_id}", customer_id)
        COMMON_KEY.get_tenant_id()
        tenant_id = BuiltIn().get_variable_value("${tenant_id}")
        whs_id = BuiltIn().get_variable_value("${whs_id}")
        txn_no = BuiltIn().get_variable_value("${res_bd_so_no}")
        if isinstance(res_bd_sales_order_id, list):
            res_bd_sales_order_id = res_bd_sales_order_id[-1]
        payload = [
            {
                "TENANT_ID": tenant_id,
                "TXN_ID": res_bd_sales_order_id,
                "TXN_NO": txn_no,
                "DIST_ID": distributor_id,
                "ROUTE_ID": route_id,
                "CUST_ID": customer_id,
                "WHS_ID": whs_id
            }
        ]
        payload = json.dumps(payload)
        print("Payload: ", payload)
        return payload

    def validated_temp_invoice_delivery_status_is_default_to_pending(self):
        so_no = BuiltIn().get_variable_value("${res_bd_so_no}")
        query = "select cast(ID as varchar), cast(DIST_ID as varchar), cast(ROUTE_ID as varchar), cast(CUST_ID as varchar), cast(WHS_ID as varchar) FROM txn_invoice  where SO_NO = '{0}' ORDER BY CREATED_DATE DESC".format(
            so_no)
        HanaDB.HanaDB().connect_database_to_environment()
        record =[]
        count = 0
        while len(record) == 0:
            record = HanaDB.HanaDB().fetch_all_record(query)
            count = count + 1
            time.sleep(1)
            if count == 20:
                break

        HanaDB.HanaDB().disconnect_from_database()
        length_rec = len(record)
        assert length_rec != 0, "Unable to retrieve Temp invoice information"
