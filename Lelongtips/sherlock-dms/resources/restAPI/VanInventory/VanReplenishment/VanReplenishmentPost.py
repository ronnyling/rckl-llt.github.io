import secrets

from robot.api.deco import keyword

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route.RouteGet import RouteGet
from resources.restAPI.MasterDataMgmt.Warehouse.WarehouseGet import WarehouseGet
from resources.restAPI.VanInventory.VanReplenishment.VanReplenishmentGet import VanReplenishmentGet
from resources.restAPI.WarehouseInventory.InventoryList.InventoryListGet import InventoryListGet
from resources.restAPI.WarehouseInventory.WarehouseTransfer.WarehouseTransferGet import WarehouseTransferGet

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL


class VanReplenishmentPost(object):
    @keyword("user posts to van replenishment")
    def user_posts_to_van_replenishment(self):
        url = "{0}van-replenishment".format(INVT_END_POINT_URL)
        payload = self.gen_van_rep_payload()
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            BuiltIn().set_test_variable("${van_rep_payload}", payload)
            BuiltIn().set_test_variable("${van_rep_id}", response.json()['ID'])
        print(response.status_code)
        return response.status_code

    def gen_van_rep_payload(self):
        RouteGet().get_route_list_by_operation_type("V")
        route_br = BuiltIn().get_variable_value("${route_br}")
        valid_routes = [route for route in route_br if route.get("STATUS", None) == "Active"
                        and route.get("SALES_PERSON", None) is not None
                        and route['VAN_WHS']['GOOD'].get("ID", None) is not None
                        and route['STATUS'] == "Active"
                        and not route['IS_DELETED']]
        rand_route = secrets.choice(valid_routes)
        route_details = rand_route
        InventoryListGet().user_retrieves_inventory_summary_for_all_warehouse()
        whs_list = BuiltIn().get_variable_value("${whs_list}")
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        WarehouseGet().user_gets_all_warehouse_data()
        whs_ls = BuiltIn().get_variable_value("${whs_ls}")
        active_whs_ids = [whs['ID'] for whs in whs_ls if
                          not whs.get("WHS_IS_BLOCKED", True) and
                          not whs.get("IS_DELETED", True)
                          ]
        valid_whs_list = [whs for whs in whs_list if
                          whs.get("WAREHOUSE_TYPE", None) == "un-managed"
                          and whs.get('WAREHOUSE_ID') in active_whs_ids
                          ]
        valid_prd_ids = [whs['PRODUCT_ID'] for whs in valid_whs_list]
        VanReplenishmentGet().user_retrieves_all_prd_for_dist_status()
        valid_prd_for_dist_ls = BuiltIn().get_variable_value("${valid_prd_for_dist_ls}")
        prd_for_use_ids = [prd['PRD_ID'] for prd in valid_prd_for_dist_ls if prd['PRD_ID'] in valid_prd_ids]
        whs_for_use_ids = list(
            set([whs['WAREHOUSE_ID'] for whs in valid_whs_list if whs['PRODUCT_ID'] in valid_prd_ids]))

        VanReplenishmentGet().user_retrieves_all_prd_for_dist_status()
        valid_prd_for_dist_ls = BuiltIn().get_variable_value("${valid_prd_for_dist_ls}")
        uoms_prd_ids = []
        uoms_prd_ls = []
        for prd in valid_prd_for_dist_ls:
            if prd.get('UOMS', None) is not None:
                if len(prd.get('UOMS')) > 0:
                    for uom in prd.get('UOMS'):
                        if uom['CONV_FACTOR_SML'] == 1:
                            uoms_prd_ids.append(prd['ID'])
                            uoms_prd_ls.append(prd)

        prd_found = False
        prd_details = None
        from_whs_id = None
        for whs_id in whs_for_use_ids:
            WarehouseTransferGet().user_retrieves_warehouse_product_list(distributor_id, whs_id)
            whs_prd_ls = BuiltIn().get_variable_value("${whs_prd_ls}")
            for whs_prd in whs_prd_ls:
                if whs_prd['ID'] in uoms_prd_ids \
                        and whs_prd['ID'] in prd_for_use_ids \
                        and whs_prd.get('AVAILABLE_QTY', None) is not None:
                    if int(float(whs_prd['AVAILABLE_QTY'])) > 5:
                        prd_found = True
                        prd_details = whs_prd
                        from_whs_id = whs_id
                        break
            if prd_found:
                break

        uom_found = False
        uom_details = None
        prd_with_uom_details = None
        for prd in uoms_prd_ls:
            if prd.get('ID') == prd_details['ID']:
                for uom in prd.get('UOMS'):
                    if uom['CONV_FACTOR_SML'] == 1:
                        uom_details = uom
                        prd_with_uom_details = prd
                        uom_found = True
                        break
            if uom_found:
                break

        qty = secrets.choice(range(1, 5))
        amt = int(float(prd_with_uom_details['COST_PRICE'])) * qty
        payload = {
            "VANREP_TYPE": "G",
            "REMARK": "",
            "ROUTE_INFO": {
                "ID": route_details['ID']
            },
            "VANREP_STATUS": "P",
            "WHS_ID_FROM": {
                "ID": from_whs_id
            },
            "WHS_ID_TO": {
                "ID": route_details['VAN_WHS']['GOOD'].get("ID", None)
            },
            "VANREP_AMT": amt,
            "PRODUCTS": [
                {
                    "PRD_ID": prd_details['ID'],
                    "UOMS": [
                        {
                            "UOM_ID": uom_details['UOM_ID'],
                            "REP_QTY": qty,
                        }
                    ],
                    "BATCH_INFO": [],
                    "EXPIRY_INFO": [],
                    "MRP": 0,
                    "REMARK": "Product Added",
                    "VANREP_AMT": amt
                }
            ],
            "PRIME_FLAG": "PRIME"
        }
        return payload
