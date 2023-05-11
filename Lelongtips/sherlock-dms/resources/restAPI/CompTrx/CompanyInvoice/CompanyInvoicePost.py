from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.CompTrx.CompanyInvoice import CompanyInvoiceGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json
import secrets
import datetime

INV_END_POINT_URL = PROTOCOL + "inventory" + APP_URL
METADATA_END_POINT_URL = PROTOCOL + "metadata" + APP_URL
SETTING_END_POINT_URL = PROTOCOL + "setting" + APP_URL
PRD_SEC_END_POINT_URL = PROTOCOL + "product-sector" + APP_URL


class CompanyInvoicePost(object):

    @keyword('user creates company invoice using ${data} data')
    def user_creates_company_invoice(self, data):
        url = "{0}company-invoice".format(INV_END_POINT_URL)
        payload = self.payload("creates", "SAVE")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, json.dumps(payload))
        print("Company Invoice Payload:", payload)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${inv_id}", body_result[0]['InvoiceId'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload(self, action, post_type):
        current_date = datetime.datetime.now()
        inv_date = str(current_date.strftime("%Y-%m-%d"))
        due_date = str((current_date + datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
        inv_details = BuiltIn().get_variable_value("${inv_details}")
        amt = inv_details['AMOUNT']
        qty = inv_details['QUANTITY']
        ttl_amt = str(int(amt)*int(qty))
        prd_info = self.get_product_info(inv_details['PRD_CD'])
        payload = {
            "POST_TYPE": post_type,
            "WAREHOUSE": self.get_warehouse_id(inv_details['WHS']),
            "STOCK_MOVEMENT": False,
            "SUPPLIER": self.get_random_supplier_id(),
            "INV_NO": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "INV_DATE": inv_date,
            "DUE_DT": due_date,
            "PO_NO": "",
            "PO_DATE": "",
            "DO_NO": "",
            "STATUS": self.get_company_invoice_status_id("Open"),
            "GROSS_TTL": ttl_amt,
            "DISC_TTL": "0",
            "CUST_DISC": "0",
            "CUST_DISC_PERC": "0",
            "TAX_TTL": "0",
            "INV_INTEGRATE": False,
            "NET_TTL": ttl_amt,
            "NET_TTL_TAX": ttl_amt,
            "ADJ_AMT": "0",
            "PRODUCT_DETAILS": [
                {
                    "PRD_ID": prd_info['ID'],
                    "PRD_CD": prd_info['PRD_CD'],
                    "PRD_DESC": prd_info['PRD_DESC'],
                    "MODE": "add",
                    "INV_QTY": qty,
                    "PRD_QTY": qty,
                    "UOM": prd_info['UOMS'][0]['UOM_ID'],
                    "GROSS_AMT": ttl_amt,
                    "COST_PRC": amt,
                    "NET_AMT": ttl_amt,
                    "PRD_INDEX": "0",
                    "VARIANCE": "0",
                    "INV_QTY_SML": qty,
                    "PRD_QTY_SML": qty,
                    "VARIANCE_QTY_SML": 0,
                    "DISCOUNT": "0",
                    "CUST_DISC": "0",
                    "TAX_AMT": "0",
                    "PRD_TAX": False,
                    "INSERTED_PRICE": True,
                }
            ],
            "PRIME_FLAG": "PRIME"
        }
        if action == "confirms" or action == "updates":
            comp_inv_details = CompanyInvoiceGet.CompanyInvoiceGet().user_retrieves_company_invoice_by_id()
            inv_no = comp_inv_details['INV_NO']
            payload.update({"INV_NO": inv_no})
        return payload

    def retreive_all_company_invoice_status(self):
        url = "{0}module-data/company-invoice-status".format(METADATA_END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
        return body_result

    def get_company_invoice_status_id(self, status_desc):
        comp_inv = self.retreive_all_company_invoice_status()
        for x in comp_inv:
            if x['DESC'] == status_desc:
                status_id = x['ID']
                break
        return status_id

    def retreive_all_warehouse(self):
        body_result = None
        inv_details = BuiltIn().get_variable_value("${inv_details}")
        dist_id = DistributorGet.DistributorGet().user_gets_distributor_by_using_code(inv_details['DIST'])
        url = "{0}distributors/{1}/warehouse".format(SETTING_END_POINT_URL, dist_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
        return body_result

    def get_warehouse_id(self, wh_desc):
        whs = self.retreive_all_warehouse()
        for x in whs:
            if x['WHS_DESC'] == wh_desc:
                wh_id = x['ID']
                break
        return wh_id

    def retreive_all_product(self):
        url = "{0}all-product-for-dist".format(PRD_SEC_END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
        return body_result

    def get_product_info(self, prd_cd):
        prd = self.retreive_all_product()
        for x in prd:
            if x['PRD_CD'] == prd_cd:
                prd_info = x
                print("prd info", prd_info)
                break
        return prd_info

    def retreive_all_supplier(self):
        url = "{0}module-data/supplier".format(METADATA_END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
        return body_result

    def get_random_supplier_id(self):
        supplier = self.retreive_all_supplier()
        if len(supplier) > 1:
            rand_so = secrets.randbelow(len(supplier))
            while supplier[rand_so]['PRIME_FLAG'] == "NON_PRIME":
                rand_so = secrets.randbelow(len(supplier))
        else:
            rand_so = 0
        return supplier[rand_so]['ID']
