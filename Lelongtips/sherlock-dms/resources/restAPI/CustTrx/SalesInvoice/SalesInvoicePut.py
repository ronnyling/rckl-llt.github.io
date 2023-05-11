from resources.restAPI.CustTrx.SalesInvoice import SalesInvoicePost, SalesInvoiceGet
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod, TokenAccess
from setup.hanaDB import HanaDB
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
import urllib3
import json

urllib3.disable_warnings()

END_POINT_URL = PROTOCOL + "invoice" + APP_URL


class SalesInvoicePut(object):

    @keyword('user updates invoice with ${data_type} data')
    def user_updates_invoice(self, data_type):
        url = "{0}invoice".format(END_POINT_URL)
        inv_header_details = BuiltIn().get_variable_value("${fixedData}")
        res_bd_invoice_id = BuiltIn().get_variable_value("${res_bd_invoice_id}")
        if res_bd_invoice_id is None:
            res_bd_so_no = BuiltIn().get_variable_value("${res_bd_so_no}")
            SalesInvoiceGet.SalesInvoiceGet().user_retrieves_all_invoice("all")
            inv_listing = BuiltIn().get_variable_value("${invoice_list}")
            inv_listing = json.dumps(inv_listing)
            inv_listing_converted = json.loads(inv_listing)

            body_result = [x for x in inv_listing_converted if x['SO_NO'] == res_bd_so_no]

            res_bd_invoice_id = body_result[0]["ID"]

            # query = "SELECT CAST(ID as VARCHAR) FROM TXN_INVOICE WHERE SO_NO = '{0}' ORDER BY TXN_CREATED_DT DESC"\
            #                                                                     .format(res_bd_so_no)
            # print("QUERY for invoice id", query)
            # HanaDB.HanaDB().connect_database_to_environment()
            # res_bd_invoice_id = HanaDB.HanaDB().fetch_one_record(query)
            # res_bd_invoice_id = COMMON_KEY.convert_string_to_id(res_bd_invoice_id)
            # HanaDB.HanaDB().disconnect_from_database()
        BuiltIn().set_test_variable("${fixedData}", inv_header_details)
        payload = SalesInvoicePost.SalesInvoicePost().inv_payload(data_type)
        payload = SalesInvoicePost.SalesInvoicePost().invoice_payload(payload[0], payload[1], payload[2], payload[3])
        update_payload = {"ID": res_bd_invoice_id}
        payload['TXN_HEADER'].update(update_payload)
        payload = json.dumps(payload)
        print(payload)
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        print(response.text)
        if response.status_code != 200:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            inv_id = body_result['TXN_HEADER']['ID']
            inv_prd_id = BuiltIn().get_variable_value("${prd_id}")
            BuiltIn().set_test_variable("${res_bd_invoice_id}", inv_id)
            BuiltIn().set_test_variable("${res_bd_invoice_prd_id}", inv_prd_id)
