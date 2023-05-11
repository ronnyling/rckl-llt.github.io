import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, TokenAccess
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.Config.ReferenceData.ReasonType import ReasonTypeGet
from resources.restAPI.MasterDataMgmt.Warehouse import WarehouseGet
from resources.TransactionFormula import TransactionFormula
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route import RouteGet
from resources.restAPI.MasterDataMgmt.Product import ProductGet, ProductUomGet
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json
import datetime
END_POINT_URL = PROTOCOL + "posm-management" + APP_URL
DT_FORMAT = "%Y-%m-%dT00:00:00.000Z"

class PosmInstallationPost(object):

    @keyword('user creates posm direct installing using ${data} data')
    def user_creates_posm_installation(self, data):
        url = "{0}posm-new-installation/".format(END_POINT_URL)
        posm_details = BuiltIn().get_variable_value("${posm_details}")
        dist_id = DistributorGet.DistributorGet().user_gets_distributor_by_using_code(posm_details['DIST'])
        unit_price = TransactionFormula().calculate_posm_prd_net(posm_details['PRODUCT'])
        header = self.posm_installation_header_payload(posm_details, dist_id, unit_price)
        prd = self.posm_prd_payload(posm_details, unit_price)
        payload = self.posm_installation_payload(header, prd)
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body = response.json()
        try:
            print("Result: ", response.json())
            BuiltIn().set_test_variable("${res_body}", response.json())
            BuiltIn().set_test_variable("${direct_install_id}", body['TXN_HEADER']['ID'])
        except IOError:
            print("ResultFail: ", response.status_code)
        BuiltIn().set_test_variable("${status_code}", response.status_code)


    def posm_installation_header_payload(self, posm_details, dist_id, unit_price):
        start_date = str((datetime.datetime.now() + datetime.timedelta(days=2)).strftime("%Y-%m-%d"))
        prd = posm_details['PRODUCT'].split(":")
        header = {
            "DIST_ID": dist_id,
            "CUST_ID": CustomerGet.CustomerGet().user_retrieves_cust_name(posm_details['CUST'])['ID'],
            "REQ_REASON_ID": ReasonTypeGet.ReasonTypeGet().user_gets_reason_by_using_code(posm_details['REASON'], "POSM_INS"),
            "WHS_ID": WarehouseGet.WarehouseGet().user_retrieves_warehouse_by_using_code(posm_details['WAREHOUSE']),
            "NET_TTL": (int(unit_price) * int(prd[1])),
            "POSM_CAT": "D",
            "TXN_TYPE": "WR",
            "INSTALL_DT": start_date,
            "START_EXEC_TIME": "19:00",
            "END_EXEC_TIME": "21:00",
            "POSITION_ASSIGNED": RouteGet.RouteGet().user_gets_route_by_using_code(posm_details['ROUTE'])
        }
        return header

    def posm_prd_payload(self, posm_details, unit_price):
        prd = posm_details['PRODUCT'].split(":")
        prd_id = ProductGet.ProductGet().user_retrieves_prd_by_prd_code(prd[0])['ID']
        uom = ProductUomGet.ProductUomGet().user_retrieves_prd_uom(prd_id)
        prd = {
            "PRD_ID": prd_id,
            "PARENT_PRD_ID": None,
            "UOM_ID": uom[0]['ID'],
            "REQ_QTY": int(prd[1]),
            "LIST_PRC": int(unit_price),
            "NET_AMT": (int(unit_price) * int(prd[1])),
            "STOCK_FLAG": False
        }
        return prd

    def posm_installation_payload(self, txn_header, txn_prd):
        payload = {
            "TXN_HEADER": txn_header,
            "TXN_PRODUCT": [
                txn_prd
            ]
        }
        payload = json.dumps(payload)
        return payload
