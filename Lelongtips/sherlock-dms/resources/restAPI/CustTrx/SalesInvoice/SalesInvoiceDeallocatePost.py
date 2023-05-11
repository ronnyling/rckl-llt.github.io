import json
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod, TokenAccess
from resources.restAPI.CustTrx.SalesInvoice.SalesInvoiceGet import SalesInvoiceGet
from resources.restAPI.Config.ReferenceData.ReasonType.ReasonTypeGet import ReasonTypeGet
from robot.libraries.BuiltIn import BuiltIn
from setup.hanaDB import HanaDB
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "invoice" + APP_URL


class SalesInvoiceDeallocatePost(object):
    """ Functions to retrieve SalesInvoice transaction """
    RS_INV_ID = "${res_bd_invoice_id}"

    @keyword("user deallocated invoice with delivery status = ${status}, invoice status = ${inv_status}")
    def user_deallocates_all_invoice(self, deliver_status, invoice_status):
        """ Function to deallocates  invoice """
        url = "{0}invoice-deallocate".format(END_POINT_URL)
        payload = self.deallocate_payload(deliver_status, invoice_status)
        print("deallocate payload", payload)
        common = APIMethod.APIMethod()
        headers = {
            'np-session': "27ea0ccb:688a61a9-80e1-4c6f-bae6-d2a6d28ceee6"
        }
        response = common.trigger_api_request("POST", url, payload, **headers)
        if response.status_code == 202:
            body_result = response.json()
            print("body", body_result)
            BuiltIn().set_test_variable("${deallocate_rs_bd}", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def deallocate_payload(self, deliver_status, invoice_status):
        COMMON_KEY.get_tenant_id()
        invoice_id = BuiltIn().get_variable_value(self.RS_INV_ID)
        ReasonTypeGet().user_gets_reason_by_using_code("RER002", "REJECT_DELIVERY")
        reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        if invoice_id is None:
            body_result = SalesInvoiceGet().user_retrieves_inv_based_on_status(deliver_status, invoice_status)
            BuiltIn().set_test_variable((self.RS_INV_ID), COMMON_KEY.convert_string_to_id(body_result[0]))
        else:
            body_result = SalesInvoiceGet().user_retrieves_particular_invoice_by_id()
            BuiltIn().set_test_variable((self.RS_INV_ID), body_result['ID'])
        payload = [
            {
                "TENANT_ID": COMMON_KEY.convert_string_tenant_id_to_tenant_id(
                    BuiltIn().get_variable_value("${tenant_id}")),
                "INV_ID": COMMON_KEY.convert_string_to_id(body_result[0]),
                "DIST_ID": COMMON_KEY.convert_string_to_id(body_result[1]),
                "ROUTE_ID": COMMON_KEY.convert_string_to_id(body_result[2]),
                "CUST_ID": COMMON_KEY.convert_string_to_id(body_result[3]),
                "WHS_ID": COMMON_KEY.convert_string_to_id(body_result[4]),
                "DELIVERY_REJECT_REASON": reason_id
            }
        ]
        payload = json.dumps(payload)
        print("payload = ", payload)
        return payload

    @keyword("validated invoice delivery status ${cond} updated successfully")
    def loop_until_worker_service_complete_deallocate_process(self, cond):
        for i in range(1, 10):
            print(i)
            flag = self.validate_invoice_deallocation_status(cond)
            if flag:
                break


    def validate_invoice_deallocation_status(self, cond):
        inv_id = BuiltIn().get_variable_value((self.RS_INV_ID))
        reason = self.user_retrieves_inv_from_db(inv_id)
        flag = False
        if (cond == "is" and reason is not None) or (cond == "is not" and reason is None):
            flag = True
        return flag

    def user_retrieves_inv_from_db(self, inv_id):
        inv_id = COMMON_KEY.convert_id_to_string(inv_id)
        query = "select cast(DELIVERY_REJECT_REASON as varchar) FROM txn_invoice where ID='{0}'".format(inv_id)
        HanaDB.HanaDB().connect_database_to_environment()
        result = HanaDB.HanaDB().fetch_all_record(query)
        HanaDB.HanaDB().disconnect_from_database()
        reason = result[0]
        return reason
