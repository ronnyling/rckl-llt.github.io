from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import TokenAccess
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route import RouteGet
from resources.restAPI.MasterDataMgmt.Warehouse import WarehouseGet
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
import json
import datetime

NOW = datetime.datetime.now()
PROMO_END_POINT_URL = PROTOCOL + "promotion-eng" + APP_URL


class PromoEntitlementPost(object):

    @keyword("Entitle Promotion")
    def entitle_promotion(self, promo_details):
        prd_info = BuiltIn().get_variable_value("${prd_info}")
        for item in prd_info:
            net = float(item['GROSS_AMT']) - float(item['CUST_DISC'])
        dist_id = DistributorGet.DistributorGet().user_gets_distributor_by_using_code(promo_details['Distributor'])
        route_id = RouteGet.RouteGet().user_gets_route_by_using_code(promo_details['Route'])
        wh_id = WarehouseGet.WarehouseGet().user_retrieves_warehouse_by_using_code(promo_details['Warehouse'])
        BuiltIn().set_test_variable("${wh_id}", wh_id)
        cust_response = CustomerGet.CustomerGet().user_retrieves_cust_name(promo_details['Customer'])
        entitle_prd_payload = self.entitle_prd_payload(prd_info)
        txn_date = str((NOW + datetime.timedelta(days=0)).strftime("%Y-%m-%d"))
        entitle_payload = {
            "TXN_HEADER": {
                "CUST_ID": cust_response['ID'],
                "DIST_ID": dist_id,
                "NET_AMT": net,
                "PRIME_FLAG": "PRIME",
                "ROUTE_ID": route_id,
                "TXN_DT": txn_date,
                "TXN_ID": None,
                "WHS_ID": wh_id
            },
            "TXN_PRODUCT": entitle_prd_payload
        }
        BuiltIn().set_test_variable("${TXN_HEADER}", entitle_payload['TXN_HEADER'])
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        entitle_payload = json.dumps(entitle_payload)
        url = "{0}promotion-eng/entitlement?type=D".format(PROMO_END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, entitle_payload)
        assert response.status_code == 200, "Unable to entitle Promo"
        BuiltIn().set_test_variable("${entitle_res}", response.json())
        self.is_promo_entileable(response.json())
        return response.json()

    def is_promo_entileable(self, entitle_respone):
        promo_cd = BuiltIn().get_variable_value("${promo_cd}")
        flag = False
        for item in entitle_respone['ENTITLED_PROMO']:
            if item['PROMO_CD'] == promo_cd:
                flag = True
        assert flag, "Unable to entitle promo"

    def entitle_prd_payload(self, prd_info):
        prd_list = []
        for item in prd_info:
            prd = self.payload_single_entitle_prd(item)
            prd_list.append(prd)
        BuiltIn().set_test_variable("${prd_list}", prd_list)
        return prd_list

    def payload_single_entitle_prd(self, item):
        if item["SELLING_IND"] == "1":
            prd_type = 'S'
        for uom in item['PRD_UOM']:
            if int(uom['QTY']) > 0:
                prd = {
                    "PRD_SLSTYPE": prd_type,
                    "PRD_ID": item['PRD_ID'],
                    "MRP": "0.00",
                    "UOM_ID": uom['UOM_ID'],
                    "PRD_INDEX": 1,
                    "PRD_QTY": int(uom['QTY']),
                    "PRD_LISTPRC": str(item['UNIT_PRICE']),
                    "PRD_LISTPRC_UOM": str(uom['PRD_LISTPRC_UOM']),
                    "GROSS_AMT": str(item['GROSS_AMT']),
                    "NET_AMT": str(item['GROSS_AMT'])
                }
        return prd




