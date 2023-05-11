import json
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Customer.CustomerGet import CustomerGet
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route.RouteGet import RouteGet
from resources.restAPI.MasterDataMgmt.Product.ProductGet import ProductGet

END_POINT_URL = PROTOCOL + "invoice" + APP_URL


class SalesReturnGetLatestInvoiceDetails(object):
    @keyword('user retrieves invoice details by data')
    def user_retrieves_latest_invoice_details(self):
        url = "{0}getLatestInvoiceDetails".format(END_POINT_URL)
        payload = self.payload_salesreturn()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Latest invoice details:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_salesreturn(self):
        payload = {
            "CUST_ID": None,
            "ROUTE_ID": None,
            "FROM_DATE": None,
            "TO_DATE": None,
            "INV_NO": None,
            "PRD_ID": None
        }

        details = BuiltIn().get_variable_value("${invoice_details}")
        if details:
            if 'CUST_NAME' in details.keys():
                cust_details = CustomerGet().user_retrieves_cust_name(details['CUST_NAME'])
                details['CUST_ID'] = cust_details['ID']
                del details['CUST_NAME']
            if 'ROUTE_CD' in details.keys():
                details['ROUTE_ID'] = RouteGet().user_gets_route_by_using_code(details['ROUTE_CD'])
                del details['ROUTE_CD']
            if 'PRD_CD' in details.keys():
                details['PRD_CD'] = details['PRD_CD'].split(",")
                prd_list = []
                for prd in details['PRD_CD']:
                    prd_details = ProductGet().user_retrieves_prd_by("code", prd)
                    prd_list.append(prd_details['ID'])
                details['PRD_ID'] = prd_list
                del details['PRD_CD']

            payload.update((k, v) for k, v in details.items())
            if payload['INV_NO'] == "yes":
                invoice_no = BuiltIn().get_variable_value("${res_bd_invoice_no}")
                payload['INV_NO'] = invoice_no
        payload = json.dumps(payload)
        print("Invoice Details Payload: ", payload)
        return payload
