import json
import datetime
from resources.restAPI import PROTOCOL, APP_URL, BuiltIn
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet, CustomerOptionGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.MasterDataMgmt.Customer import CustomerShipToGet
from resources.restAPI.MasterDataMgmt.Warehouse import WarehouseGet
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route import RouteGet

from resources.restAPI.Common import APIMethod, TokenAccess

import urllib3
NOW = datetime.datetime.now()

urllib3.disable_warnings()

END_POINT_URL = PROTOCOL + "invoice" + APP_URL


class InvoicePost(object):
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.000Z"
    def create_invoice(self):
        header = BuiltIn().get_variable_value("&{promo_details}")
        prd_info = BuiltIn().get_variable_value("${prd_info}")
        promo_disc = BuiltIn().get_variable_value("${promo_disc}")
        if promo_disc == None:
            promo_disc = 0
        txn_prod_tax = self.txn_prd_tax_payload(prd_info)
        TokenAccess.TokenAccess().get_token_by_role('hqadm')
        txn_header = self.txn_header_payload(header, prd_info,promo_disc)
        txn_product = self.txn_prd_payload(prd_info, promo_disc)
        txn_promo = self.txn_promo(prd_info, promo_disc)
        inv_payload = self.inv_payload(txn_header, txn_prod_tax, txn_product, txn_promo)
        print("print invoice", inv_payload)
        TokenAccess.TokenAccess().get_token_by_role('distadm')
        url = "{0}invoice".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, inv_payload)
        BuiltIn().set_test_variable("${inv_res}", response.json())
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def txn_prd_tax_payload(self, prd_info):
        prd_tax_list = []
        for item in prd_info:

            payload = {
                    "APPLY_SEQ": "1",
                    "PRD_ID": item['PRD_ID'],
                    "PRD_INDEX": 0,
                    "TAX_AMT": str(item['TOTAL_TAX']),
                    "TAX_ID": item['TAX_SETTING']['ID'],
                    "TAX_PERC": str(item['TAX_SETTING']['TAX_RATE']),
                    "TXN_ID": None,
                    "UNIT_TAX": str(item['TOTAL_TAX']),
                    "UOM_ID": item['PRD_UOM'][0]['UOM_ID']
                }
            prd_tax_list.append(payload)
        return prd_tax_list

    def txn_prd_payload(self, prd_info, promo_disc):
        prd_list = []
        for item in prd_info:

            prd = {
                    "CUST_DISC": "0.0000",
                    "DEF_UOM_ID": "5D04252C:95E5E037-F17C-4343-889D-B0000C7BDDB9",
                    "GROSS_AMT": str(item['GROSS_AMT']),
                    "HSN_CD": None,
                    "INV_DISC": str(promo_disc),
                    "INV_FLAG": 0,
                    "MRP": 0,
                    "NET_AMT": str(item['TAXABLE_AMT']),
                    "NET_AMT_TAX": str(item['NET_TTL_TAX']),
                    "ORDPRD_INDEX": 1,
                    "PRD_DISC": str(promo_disc),
                    "PRD_HEIR_ID": "B3EA05F1:76911BF8-EA1E-484E-A747-25CC3A0C20FE",
                    "PRD_ID": item['PRD_ID'],
                    "PRD_INDEX": 1,
                    "PRD_LISTPRC": str(item['UNIT_PRICE']),
                    "PRD_QTY": str(item['PRD_UOM'][0]['QTY']),
                    "PRD_SLSTYPE": "S",
                    "PROCESS_ERROR": None,
                    "PROMO_DISC": str(promo_disc),
                    "REMARK": "",
                    "TAX_AMT": str(item['TOTAL_TAX']),
                    "TAX_IND": True,
                    "UOM_ID": item['PRD_UOM'][0]['UOM_ID'],
                    "UOM_LISTPRC": str(item['UNIT_PRICE'])
                }
            prd_list.append(prd)
        return prd_list
    def txn_promo(self, prd_info, promo_disc):
        promo_res = BuiltIn().get_variable_value("${promo}")
        promo= []
        for item in prd_info:
            slab = BuiltIn().get_variable_value("${slab}")
            payload = {
                "AVAILABLE_MAX_COUNT": None,
                "DISC_AMT": str(promo_disc),
                "DISC_PERC": slab['DISC_PERC'],
                "DISC_SPENT_AMT": str(promo_disc),
                "MECHANIC_TYPE": slab['MECHANIC_TYPE'],
                "ORDPRD_INDEX": 1,
                "MRP": 0,
                "PRD_BUY": "0.000000",
                "PRD_ID": item['PRD_ID'],
                "PRD_INDEX": 1,
                "PRD_INDEX_NEW": 1,
                "PRD_SLSTYPE": "S",
                "PROMO_FREQ": "2",
                "PROMO_ID": slab['PROMO_ID'],
                "PROMO_SEQ": promo_res['PROMO_SEQ_ID'],
                "PROMO_SLAB_ID": slab['ID'],
                "TTL_BUY": "0.000000",
                "TTL_DISC_AMT": "0.000000"
            }
            promo.append(payload)
        return promo
    def txn_header_payload(self, header, prd_info, promo_disc):
        print("inv_prd_info",prd_info)
        gross = 0
        NET_TTL_TAX = 0
        total_tax = 0
        ttl_taxable_amt = 0
        for item in prd_info:
            gross = gross + float(item['GROSS_AMT'])
            NET_TTL_TAX = NET_TTL_TAX + float(item['NET_TTL_TAX'])
            total_tax = total_tax + float(item['TAXABLE_AMT'])
            ttl_taxable_amt = ttl_taxable_amt + float(item['TAXABLE_AMT'])

        st_date = str((NOW + datetime.timedelta(days=0)).strftime("%Y-%m-%dT00:00:00.000Z"))
        dist_id = DistributorGet.DistributorGet().user_gets_distributor_by_using_code(header['DIST'])
        route_id = RouteGet.RouteGet().user_gets_route_by_using_code(header['ROUTE'])
        route_plan = RouteGet.RouteGet().user_gets_route_plan_by_using_code('CY0000000417')
        wh_id = WarehouseGet.WarehouseGet().user_retrieves_warehouse_by_using_code(header['WAREHOUSE'])
        cust_response = CustomerGet.CustomerGet().user_retrieves_cust_name(header['CUST'])
        shipto_id = \
            CustomerShipToGet.CustomerShipToGet().user_retrieves_cust_default_ship_to_address(cust_response['ID'])['ID']
        payload = {
            "ADJ_AMT": "-0.08",
            "AUTO_COLLECT": False,
            "AVAILABLE_BLNCE": 123,
            "BILL_REF_NO": "",
            "CREDIT_CHECK": "",
            "CUST_DISC": "0.00",
            "CUST_DISC_AMT": "0.0000",
            "CUST_DISC_PERC": "0.0000",
            "CUST_HIER_ID": None,
            "CUST_ID": cust_response['ID'],
            "DELIVERY_DT": st_date,
            "DIST_ID": dist_id,
            "DOC_MODE": "C",
            "GROSS_TTL": str(gross),
            "INV_DT": st_date,
            "INV_TYPE": "I",
            "INVTERM_CD": "E6FC108E:214DBCB9-18BA-406F-B649-39070E178FFB",
            "INVTERM_ID": "E6FC108E:214DBCB9-18BA-406F-B649-39070E178FFB",
            "NET_TTL": str(ttl_taxable_amt),
            "NET_TTL_TAX": str(NET_TTL_TAX),
            "NONTAXABLE_AMT": "0.0000",
            "PRIME_FLAG": "PRIME",
            "PROMO_DISC": str(promo_disc),
            "REMARK": "",
            "ROUTE_ID": route_id,
            "RP_ID": route_plan,
            "SHIPTO_ID": shipto_id,
            "SO_DT": st_date,
            "SO_NO": "",
            "TAX_TTL": str(total_tax),
            "TAXABLE_AMT": str(ttl_taxable_amt),
            "WHS_ID": wh_id
        }
        return payload

    def inv_payload(self, txn_header, txn_prod_tax, txn_product, txn_promo):
        payload = {
            "QPS_PRODUCT": [],
            "TXN_FOC_ALLOCATE": [],
            "TXN_HEADER": txn_header,
            "TXN_PRDTAX": txn_prod_tax,
            "TXN_PRODUCT": txn_product,
            "TXN_PROMO": txn_promo
        }
        payload = json.dumps(payload)
        return payload
