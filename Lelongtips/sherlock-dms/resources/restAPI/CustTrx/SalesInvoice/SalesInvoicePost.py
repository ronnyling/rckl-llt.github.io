import json
import datetime
import secrets
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.MasterDataMgmt.Customer import CustomerShipToGet
from resources.restAPI.MasterDataMgmt.Warehouse import WarehouseGet
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route import RouteGet
from resources.restAPI.MasterDataMgmt.Product import ProductGet
from resources.TransactionFormula import TransactionFormula
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod, TokenAccess
from setup.hanaDB import HanaDB
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.CustTrx.SalesOrder import SalesOrderPost
import urllib3

urllib3.disable_warnings()

END_POINT_URL = PROTOCOL + "invoice" + APP_URL


class SalesInvoicePost(object):

    @keyword('user creates invoice with ${data_type} data')
    def user_creates_invoice(self, data_type):
        url = "{0}invoice".format(END_POINT_URL)
        payload = self.inv_payload(data_type)
        payload = self.invoice_payload(payload[0], payload[1], payload[2], payload[3])
        payload = json.dumps(payload)
        print(payload)
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print("POST Status code for SalesInvoice is " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.text)
        if response.status_code != 200:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            inv_id = body_result['TXN_HEADER']['ID']
            inv_no = body_result['TXN_HEADER']['INV_NO']
            print("payload ",payload)
            inv_prd_id = BuiltIn().get_variable_value("${prd_id}")
            BuiltIn().set_test_variable("${res_bd_invoice_id}", inv_id)
            BuiltIn().set_test_variable("${res_bd_invoice_body_result}", response.json())
            BuiltIn().set_test_variable("${res_bd_invoice_prd_id}", inv_prd_id)
            BuiltIn().set_test_variable("${res_bd_invoice_no}", inv_no)

    @keyword("validated delivery status column is added and default to open status")
    def check_delivery_status_is_added_in_db(self):
        invoice_payload = BuiltIn().get_variable_value("${res_bd_invoice_body_result}")
        query = "select * from txn_Invoice where inv_no = '{0}' AND delivery_status = 'O'".format(invoice_payload['TXN_HEADER']['INV_NO'])
        HanaDB.HanaDB().connect_database_to_environment()
        HanaDB.HanaDB().check_if_exists_in_database_by_query(query)
        HanaDB.HanaDB().disconnect_from_database()

    def inv_payload(self, data_type):
        inv_header = self.invoice_header_payload(data_type)
        prd_info = BuiltIn().get_variable_value("${prd_info}")
        inv_tax = self.inv_prd_tax(prd_info)
        inv_prd = self.inv_prd_paylad(prd_info)
        inv_groupdisc = SalesOrderPost.SalesOrderPost().so_groupdisc(prd_info)
        ttl_groupdisc = BuiltIn().get_variable_value("${ttl_groupdisc}")
        inv_header.update({"GRPDISC_AMT": str(ttl_groupdisc)})
        return inv_header, inv_prd, inv_tax, inv_groupdisc

    def inv_prd_paylad(self, prd_info):
        prd_list = []
        count = 0
        for prd in prd_info:
            prd_type = BuiltIn().get_variable_value("${prdType}")
            if prd_type is None or prd_type['PRD_SLSTYPE'] == 'S':
                sls_type = 'S'
            else:
                sls_type = prd_type['PRD_SLSTYPE']
                prd['GROSS_AMT'] = 0.0000
                prd['PROMO_DISC'] = 0.0000
                prd['CUST_DISC'] = 0.0000
                prd['NET_AMT'] = 0.0000
                prd['NET_TTL_TAX'] = 0.0000
                prd['TOTAL_TAX'] = 0.0000
            count = count + 1
            payload = {
                "PRD_INDEX": count,
                "ORDPRD_INDEX": count,
                "PRD_SLSTYPE": sls_type,
                "INV_FLAG": 0,
                "PROCESS_ERROR": None,
                "MRP": 0,
                "DISCOUNT": prd['DISCOUNT'],
                "GRPDISC_AMT": str(prd['GRPDISC_AMT']),
                "GRPDISC_ID": prd['GRPDISC_ID'],
                "PRD_LISTPRC": str(prd['UNIT_PRICE']),
                "PRD_ID": ProductGet.ProductGet().user_retrieves_prd_by_prd_code(prd['PRD_CODE'])['ID'],
                "PRD_HEIR_ID": "B3EA05F1:76911BF8-EA1E-484E-A747-25CC3A0C20FE",
                "HSN_CD": None,
                "REMARK": "",
                "INV_DISC": prd['CUST_DISC'],
                "DEF_UOM_ID": prd['PRD_UOM'][0]['UOM_ID'],
                "UOM_ID": prd['PRD_UOM'][0]['UOM_ID'],
                "TAX_IND": True,
                "PRD_QTY": str(prd['BUY_QTY']),
                "UOM_LISTPRC": str(prd['PRD_UOM'][0]['PRD_LISTPRC_UOM']),
                "GROSS_AMT": str(prd['GROSS_AMT']),
                "TAX_AMT": str(prd['TOTAL_TAX']),
                "PROMO_DISC": str(prd['PROMO_DISC']),
                "CUST_DISC": str(prd['CUST_DISC']),
                "NET_AMT": str(prd['NET_AMT']),
                "NET_AMT_TAX": str(prd['NET_TTL_TAX']),
                "PRD_DISC": '0'
            }
            prd_list.append(payload)
        return prd_list

    def inv_prd_tax(self, prd_info):
        tax_list = []
        index_count = 0
        prd_count = 0
        print("PROD OUTPUT:", prd_info)
        for prd in prd_info:
            prd_type = BuiltIn().get_variable_value("${prdType}")
            if prd_type is None or prd_type['PRD_SLSTYPE'] == 'S':
                continue
            else:
                break
            if 'TAX_SETTING' not in prd:
                continue
            index_count = index_count + 1
            payload = {
                "TXN_ID": None,
                "PRD_INDEX": index_count,
                "PRD_ID": ProductGet.ProductGet().user_retrieves_prd_by_prd_code(prd['PRD_CODE'])['ID'],
                "UOM_ID": prd['PRD_UOM'][0]['UOM_ID'],
                "UNIT_TAX": prd['TOTAL_TAX'],
                "TAX_AMT":  prd['TOTAL_TAX'],
                "TAX_ID": prd['TAX_SETTING']['ID'],
                "TAX_PERC": prd['TAX_SETTING']['TAX_RATE'],
                "APPLY_SEQ": str(prd['TAX_SETTING']['SEQ_NO']),
                "TAXABLE_AMT": prd['TAXABLE_AMT']
            }
            tax_list.append(payload)
            prd_count = prd_count + 1
        return tax_list

    def invoice_header_payload(self, data_type):
        inv_details = BuiltIn().get_variable_value("${fixedData}")
        dist_details = BuiltIn().get_variable_value("${distData}")
        if dist_details is not None :
            dist_cd = BuiltIn().get_variable_value("${distData['DIST_CD']}")
        else :
            dist_cd = "DistEgg"
        if inv_details is not None:
            principal = BuiltIn().get_variable_value("${fixedData['PRIME_FLAG']}")
        else:
            principal = secrets.choice(["NON_PRIME", "PRIME"])
        if data_type == 'fixed':
            warehouse = inv_details['INV_WH']
            cust = inv_details['INV_CUST']
            route = inv_details['INV_ROUTE']
        else:
            warehouse = "CCCC"
            cust = "CXTESTTAX"
            route = "Rchoon"
        dist_id = DistributorGet.DistributorGet().user_gets_distributor_by_using_code(dist_cd)
        route_id = RouteGet.RouteGet().user_gets_route_by_using_code(route)
        wh_id = WarehouseGet.WarehouseGet().user_retrieves_warehouse_by_using_code(warehouse)
        cust_response = CustomerGet.CustomerGet().user_retrieves_cust_name(cust)
        print("CUST DATA:", cust_response)
        BuiltIn().set_test_variable("${cust_response}",cust_response)
        shipto_id = CustomerShipToGet.CustomerShipToGet().user_retrieves_cust_default_ship_to_address(cust_response['ID'])['ID']
        TransactionFormula().tran_calculation_for_gross_and_cust_disc(principal, inv_details['INV_CUST'], 'percent',
                                                                      inv_details['PROD_ASS_DETAILS'])
        TransactionFormula().tax_calculation_for_multi_product()
        prd_info = BuiltIn().get_variable_value("${prd_info}")
        ttl_details = TransactionFormula().calculation_for_product_total(prd_info)
        amount = TransactionFormula().rounding_based_on_setup(ttl_details[1]["TTL_NET"])
        time = COMMON_KEY.get_local_time()
        inv_type = BuiltIn().get_variable_value("${invType}")
        if inv_type is None :
            txn_type = 'S'
        else :
            txn_type = inv_type['INVOICE_TXNTYPE']
            cust_response["CUST_DISC"] = "0.0"
        sample_id = BuiltIn().get_variable_value("${sampling_id}")
        if sample_id is None:
            sample_id = None
        payload = {
            "DIST_ID": dist_id,
            "INV_DT": time,
            "ROUTE_ID": route_id,
            "RP_ID": None,
            "WHS_ID": wh_id,
            "CUST_ID": cust_response['ID'],
            "DELIVERY_DT": time,
            "SO_NO": "",
            "SHIPTO_ID": shipto_id,
            "DOC_MODE": "C",
            "BILL_REF_NO": "",
            "SO_DT": time,
            "REMARK": "",
            "AUTO_COLLECT": False,
            "CUST_HIER_ID": None,
            "INVTERM_ID": cust_response['TERMS'],
            "INVTERM_CD": cust_response['TERMS'],
            "PRIME_FLAG": principal,
            "INV_TYPE": "I",
            "INVOICE_TXNTYPE" : txn_type,
            "SAMPLE_ID" : sample_id,
            "GROSS_TTL": str(ttl_details[1]["TTL_GROSS"]),
            "CUST_DISC_PERC": cust_response["CUST_DISC"],
            "CUST_DISC": ttl_details[1]["TTL_CUST_DISC"],
            "CUST_DISC_AMT": str(ttl_details[1]["TTL_CUST_DISC"]),
            "PROMO_DISC": str(ttl_details[1]["TTL_PROMO_DISC"]),
            "TAX_TTL": str(ttl_details[1]["TTL_TAX"]),
            "TAXABLE_AMT": str(ttl_details[1]["TTL_TAXABLE"]),
            "NONTAXABLE_AMT": str(ttl_details[1]["TTL_NONTAXABLE"]),
            "NET_TTL": str(ttl_details[1]["TTL_GROSS"]),
            "NET_TTL_TAX": str(ttl_details[1]["TTL_NET"]),
            "ADJ_AMT": str(amount[1]),
            "CREDIT_CHECK": cust_response['CRDT_LIMIT'],
            "AVAILABLE_BLNCE": cust_response['OUT_BLNCE']
        }
        return payload

    def invoice_payload(self, header, txn_prd, txn_tax, txn_groupdisc):
        if txn_groupdisc is None :
            txn_groupdisc = []
        payload = {
            "TXN_HEADER": header,
            "TXN_PRODUCT": txn_prd,
            "TXN_PROMO": [],
            "TXN_FOC_ALLOCATE": [],
            "TXN_PRDTAX": txn_tax,
            "QPS_PRODUCT": [],
            "PRODUCT_CUSTGRP_DISC": txn_groupdisc
        }
        return payload
