from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from setup.hanaDB import HanaDB
import json

END_POINT_URL = PROTOCOL + "invoice" + APP_URL


class SalesInvoiceConfirm(object):
    TEMP_INV = "${temp_inv_list}"

    def user_confirms_temporary_invoice(self):
        dist_id = BuiltIn().get_variable_value(COMMON_KEY.DISTRIBUTOR_ID)
        url = "{0}confirmInvoice".format(END_POINT_URL)
        payload = self.temp_invoice_payload(dist_id)
        payload = json.dumps(payload)
        common = APIMethod.APIMethod()
        rand_string = COMMON_KEY.generate_random_id("0")
        headers = {
            'np-session': rand_string
        }
        response = common.trigger_api_request("POST", url, payload, **headers)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        if response.status_code == 202:
            body_result = response.json()
            assert body_result['message'] == 'request successfully processed'
            temp_inv_list = BuiltIn().get_variable_value(self.TEMP_INV)
            for i in range(len(temp_inv_list)):
                invoice_id = COMMON_KEY.convert_id_to_string(temp_inv_list[i])
                query = "SELECT CAST(INV_STATUS as VARCHAR) FROM TXN_INVOICE WHERE ID = '{0}' " \
                            "ORDER BY TXN_CREATED_DT DESC".format(invoice_id)
                HanaDB.HanaDB().connect_database_to_environment()
                trial = 0
                while trial < 300:
                    trial = trial + 1
                    status = HanaDB.HanaDB().fetch_one_record(query)
                    if status == 'S':
                        break
                    if trial == 299:
                        assert status == 'S', "Temporary Invoice not being Confirm correctly"
            HanaDB.HanaDB().disconnect_from_database()

    def temp_invoice_payload(self, dist_id):
        tenant_id = COMMON_KEY.get_tenant_id()
        tenant_id = COMMON_KEY.convert_string_to_id(tenant_id)
        route_id = BuiltIn().get_variable_value("${route_id}")
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        whs_id = BuiltIn().get_variable_value("${WAREHOUSE_ID}")
        temp_inv_list = BuiltIn().get_variable_value(self.TEMP_INV)
        if temp_inv_list is None:
            temp_inv_list = self.get_invoice_id_using_order_number()
        payload = []
        for i in range(len(temp_inv_list)):
            details = {
                "TENANT_ID": tenant_id,
                "INV_ID": temp_inv_list[i],
                "DIST_ID": dist_id,
                "ROUTE_ID": route_id,
                "CUST_ID": cust_id,
                "WHS_ID": whs_id,
                "INVTERM_ID": None
            }
            payload.append(details)
        print(payload)
        return payload

    def get_invoice_id_using_order_number(self):
        temp_inv_list = BuiltIn().get_variable_value(self.TEMP_INV)
        if temp_inv_list is None:
            temp_inv_list = []
        res_bd_so_no = BuiltIn().get_variable_value("${res_bd_so_no}")
        if isinstance(res_bd_so_no, list):
            res_bd_so_no = res_bd_so_no[-1]
        query_n = "SELECT CAST(ID as VARCHAR) FROM TXN_INVOICE WHERE SO_NO = '{0}' ORDER BY TXN_CREATED_DT DESC" \
            .format(res_bd_so_no)
        HanaDB.HanaDB().connect_database_to_environment()
        trial = 0
        res_bd_invoice_id = None
        while trial < 300:
            try:
                trial = trial + 1
                res_bd_invoice_id = HanaDB.HanaDB().fetch_one_record(query_n)
                break
            except Exception as e:
                print(e.__class__, "occured")
        assert res_bd_invoice_id, "Temporary Invoice is not generated"
        invoice_id = COMMON_KEY.convert_string_to_id(res_bd_invoice_id)
        HanaDB.HanaDB().disconnect_from_database()
        temp_inv_list.append(invoice_id)
        BuiltIn().set_test_variable(self.TEMP_INV, temp_inv_list)
        return temp_inv_list
