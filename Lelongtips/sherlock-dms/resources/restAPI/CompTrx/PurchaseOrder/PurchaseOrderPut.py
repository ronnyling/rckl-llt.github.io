import datetime
import json
import secrets

from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet, DistributorShipToGet
from resources.restAPI.CompTrx.CompanyInvoice import CompanyInvoicePost
from resources.restAPI.CompTrx.PurchaseOrder import PurchaseOrderGet
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "purchase-order" + APP_URL


class PurchaseOrderPut(object):

    @keyword('user updates purchase order using ${data} data')
    def user_updates_purchase_order(self, data):
        po_id = BuiltIn().get_variable_value("${po_id}")
        url = "{0}purchase-order/{1}".format(END_POINT_URL, po_id)
        payload = self.payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, json.dumps(payload))
        print ("PAYLOAD", payload)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${po_id}", body_result['TXN_HEADER']['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)


    def payload(self):
        po_details = PurchaseOrderGet.PurchaseOrderGet().user_retrieves_purchase_order_by_id()
        #po_details = BuiltIn().get_variable_value("${res_bd_po}")
        new_po_details = BuiltIn().get_variable_value("${po_details}")
        prd_info = CompanyInvoicePost.CompanyInvoicePost().get_product_info(new_po_details['PRD_CD'])
        amt = new_po_details['AMOUNT']
        qty = float(new_po_details['QUANTITY'])
        ttl_amt = (int(amt) * int(qty))
        payload = {
              "TXN_HEADER": {
                "DIST_ID": po_details['TXN_HEADER']['DIST_ID'],
                "VMI_DT": po_details['TXN_HEADER']['VMI_DT'],
                "WHS_ID": [
                    po_details['TXN_HEADER']['WHS_ID'][0]['ID']
                ],
                "SHIPTO_ID": po_details['TXN_HEADER']['SHIPTO_ID'],
                "GRS_AMT": ttl_amt,
                "VMI_STATUS": po_details['TXN_HEADER']['VMI_STATUS'],
                "REMARK": prd_info['PRD_DESC'],
                "TXN_NO": po_details['TXN_HEADER']['TXN_NO']
              },
              "TXN_PRODUCT": [
                {
                  "PRD_ID": prd_info['ID'],
                  "UOM_ID": prd_info['UOMS'][0]['UOM_ID'],
                  "ORD_QTY": qty,
                  "MIN_REP_QTY": 0,
                  "INVT_QTY": 0,
                  "BE_QTY": 0,
                  "PROPOSED_QTY": 0,
                  "MAINDIST_QTY": 0,
                  "ADS": 0,
                  "SKU_TYPE": "",
                  "AFT_SC": 0,
                  "BFR_SC": 0,
                  "PALLET": 0,
                  "NET_AMT": ttl_amt,
                  "PRD_GROUP_DESC": prd_info['PRD_DESC']
                }
              ]
            }

        return payload


    @keyword('user ${action} purchase order')
    def user_updates_purchase_order_status(self, action):
        po_id = BuiltIn().get_variable_value("${po_id}")
        if action == "confirm" or action == "cancel":
            url = "{0}purchase-order/action".format(END_POINT_URL, po_id)
        else:
            url = "{0}purchase-order".format(END_POINT_URL, po_id)
        payload = self.action_payload(action)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, json.dumps(payload))
        print ("PAYLOAD", payload)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${po_id}", body_result['TXN_HEADER']['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)


    def action_payload(self, action):
        """Function to update payload status to confirm/cancel/approve/reject"""
        po_id = BuiltIn().get_variable_value("${po_id}")

        if action == "confirm":
            action = "CONFIRM"
        elif action == "cancel":
            action = "CANCEL"
        elif action == "approve":
            action = "APPROVE"
        elif action == "reject":
            action = "REJECT"

        payload = {
                "ACTION": action,
                "TXN_ID": [
                        po_id
                    ]
                }

        return payload


