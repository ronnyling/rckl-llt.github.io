import datetime
import json
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet, DistributorShipToGet
from resources.restAPI.CompTrx.CompanyInvoice import CompanyInvoicePost
from resources.restAPI.MasterDataMgmt.Warehouse import WarehouseGet
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "purchase-order" + APP_URL


class PurchaseOrderPost(object):

    @keyword('user creates purchase order using ${data} data')
    def user_creates_purchase_order(self, data):
        url = "{0}purchase-order".format(END_POINT_URL)
        payload = self.payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, json.dumps(payload))
        print ("PAYLOAD", payload)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${po_id}", body_result['TXN_HEADER']['ID'])
            BuiltIn().set_test_variable("${po_no}", body_result['TXN_HEADER']['TXN_NO'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)


    def payload(self):
        po_details = BuiltIn().get_variable_value("${po_details}")
        current_date = datetime.datetime.now()
        po_date = str(current_date.strftime("%Y-%m-%d"))
        wh_id = WarehouseGet.WarehouseGet().user_retrieves_warehouse_by_using_code(po_details['WHS'])
        dist_id = DistributorGet.DistributorGet().user_gets_distributor_by_using_code(po_details['DIST'])
        shipto_id = DistributorShipToGet.DistributorShipToGet().user_retrieves_all_shipto()
        prd_info = CompanyInvoicePost.CompanyInvoicePost().get_product_info(po_details['PRD_CD'])
        amt = po_details['AMOUNT']
        qty = float(po_details['QUANTITY'])
        ttl_amt = (int(amt) * int(qty))
        if po_details['STATUS'] == "CONFIRM":
            status = "C"
        else:
            status = "P"

        payload = {
              "TXN_HEADER": {
                "DIST_ID": dist_id,
                "VMI_DT": po_date,
                "WHS_ID": [
                  wh_id
                ],
                "SHIPTO_ID": shipto_id,
                "GRS_AMT": ttl_amt,
                "VMI_STATUS": status
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
                  "PRD_GROUP_DESC": None
                }
              ]
            }

        return payload