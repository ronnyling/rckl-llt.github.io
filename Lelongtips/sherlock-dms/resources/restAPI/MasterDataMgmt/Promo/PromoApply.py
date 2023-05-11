from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure import StructureGet
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.MasterDataMgmt.Warehouse.WarehouseGet import WarehouseGet
from resources.restAPI.Common import TokenAccess
from resources.restAPI.MasterDataMgmt.Promo import PromoBuyTypeGet
from resources.restAPI.MasterDataMgmt.Promo import PromoGet
from resources.restAPI.MasterDataMgmt.Promo.PromoCalculation.PromoDealCalculation import PromoDealCalculation
from resources.restAPI.MasterDataMgmt.Product import ProductUomGet

import json
import datetime

NOW = datetime.datetime.now()
PROMO_END_POINT_URL = PROTOCOL + "promotion-eng" + APP_URL
DATE_FORMAT = "%Y-%m-%d"

class PromoApply(object):
    @keyword("Apply Promotion")
    def apply_promotion(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        payload = self.apply_payload()
        print("Apply Payload=", payload)
        url = "{0}promotion-eng/apply?type=D".format(PROMO_END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        assert response.status_code == 200, "Unable to apply Promo"
        print("apply Response=", response.json())
        return response.json()

    def date_time_format(self, data):
        data_time = data.split(" ")
        data_time = data_time[0] + "T00:00:00.000Z"
        return data_time

    def apply_payload(self):
        prd_info = BuiltIn().get_variable_value("${prd_info}")
        txn_header = BuiltIn().get_variable_value("${TXN_HEADER}")
        prd_list = BuiltIn().get_variable_value("${prd_list}")
        txn_date = str(NOW.strftime(DATE_FORMAT))
        total_tax = 0
        for item in prd_info:
            total_tax = total_tax + item['NET_TTL_TAX']
        print("prd info", prd_info)
        payload = {
            "TXN_HEADER": {
                "TXN_ID": None,
                "TXN_DT": txn_date,
                "DIST_ID": txn_header['DIST_ID'],
                "CUST_ID": txn_header['CUST_ID'],
                "ROUTE_ID": txn_header['ROUTE_ID'],
                "NET_AMT": total_tax,
                "WHS_ID": txn_header['WHS_ID'],
                "PRIME_FLAG": txn_header['PRIME_FLAG']
            },
            "TXN_PRODUCT": prd_list,
            "APPLIED_PROMO": [
                self.apply_applied_promo_payload(prd_list, prd_info)
            ],
            "QPS_PRODUCT": []
        }
        payload = json.dumps(payload)
        return payload

    def search_for_foc(self, entitle_res, promo_cd):
        entitled_foc = None
        for item in entitle_res['ENTITLED_PROMO']:
            if item['PROMO_CD'] == promo_cd:
                entitled_foc = item['PROMO_FOC_ENTITLED']
                break;
        return entitled_foc


    def apply_applied_promo_payload(self, prd_list, prd_info):
        foc_allocate_payload = []
        foc_entitle_payload = []
        is_foc_linked = False
        PromoGet.PromoGet().get_promotion()
        promo = BuiltIn().get_variable_value("${promo_response}")
        COMMON_KEY.get_tenant_id()
        tenant_id = BuiltIn().get_variable_value("${tenant_id}")
        tenant_id = COMMON_KEY.convert_string_to_id(tenant_id)
        str_dt = self.date_time_format(promo['START_DT'])
        end_dt = self.date_time_format(promo['END_DT'])
        approve_dt = self.date_time_format(promo['APPR_DT'])
        auto_promo = BuiltIn().get_variable_value("${auto_promo_ref_res_body}")
        claim_end_date = BuiltIn().get_variable_value("${claim_end_date}")
        promo_type_desc = PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_promo_type(promo['TYPE'], "id")[
            'REF_DESC']
        buy_type_desc = PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_promo_buy_type(promo['BUY_TYPE'], 'id')[
            'REF_DESC']
        total = 0.00

        for item in prd_list:
            if buy_type_desc == "By Quantity":
                total = int(item['PRD_QTY'])
            else:
                total = total + float(item['NET_AMT'])
        ttb, disc_value, promo_slab = PromoDealCalculation().hitting_which_slab(promo['PROMO_SLABS'], total, "TOTAL_BUY", "")
        if promo_slab['MECHANIC_TYPE'] == 'B4183EC5:1A39D88B-1B2D-46EA-AA2D-AF4F2A8FDEE7':
            entitle_res = BuiltIn().get_variable_value("${entitle_res}")
            entitled_foc = self.search_for_foc(entitle_res, promo['PROMO_CD'])
            foc_allocate_payload = self.foc_allocate_payload(promo_slab, entitled_foc)
            foc_entitle_payload = self.foc_entitled_payload(promo_slab, entitled_foc)
            is_foc_linked = True
            promo_benefic = "FOC"
        else:
            promo_benefic = promo_slab['DISC_PERC']
        foc_qty = promo_slab['FOC_QTY']
        if foc_qty is None:
            foc_qty = 0
        payload = {
                    "ID": promo['ID'],
                    "TENANT_ID": tenant_id,
                    "DIST_ID": promo['DIST_ID'],
                    "PROMO_CD":  promo['PROMO_CD'],
                    "PROMO_DESC":  promo['PROMO_DESC'],
                    "START_DT": str_dt,
                    "END_DT": end_dt,
                    "SPACEBUY_END_DT": promo['SPACEBUY_END_DT'],
                    "CLAIMABLE_IND": promo['CLAIMABLE_IND'],
                    "CLAIM_ENDDT": claim_end_date,
                    "TYPE": promo['TYPE'],
                    "PROMO_SEQ_ID": promo['PROMO_SEQ_ID'],
                    "BUY_TYPE": promo['BUY_TYPE'],
                    "BUY_UOM_ID": promo['BUY_UOM_ID'],
                    "CLAIM_TYPE_ID": promo['CLAIM_TYPE_ID'],
                    "AUTO_CHECKED": promo['AUTO_CHECKED'],
                    "AUTO_PROMO":  promo['AUTO_PROMO'],
                    "SCHEME_QPS":  promo['SCHEME_QPS'],
                    "SCHEME_PRORATA":  promo['SCHEME_PRORATA'],
                    "SCHEME_RANGE":  promo['SCHEME_RANGE'],
                    "SCHEME_COMBI":  promo['SCHEME_COMBI'],
                    "SCHEME_MRP":  promo['SCHEME_MRP'],
                    "DISC_METHOD": promo['DISC_METHOD'],
                    "FOC_RECURRING": promo['FOC_RECURRING'],
                    "MAX_COUNT_FLAG": promo['MAX_COUNT_FLAG'],
                    "MAX_COUNT": str(promo['MAX_COUNT']),
                    "FOR_EVERY_FLAG": promo['FOR_EVERY_FLAG'],
                    "PROMO_STATUS":  promo['PROMO_STATUS'],
                    "APPR_IND": promo['APPR_IND'],
                    "APPR_DT": approve_dt,
                    "NOTES": promo['NOTES'],
                    "RETAIL_CAP_FLAG":  promo['RETAIL_CAP_FLAG'],
                    "RETAILER_CAP":  promo['RETAILER_CAP'],
                    "EXCL_PROMO":  promo['EXCL_PROMO'],
                    "NEW_POS": promo['NEW_POS'],
                    "BATCH": promo['BATCH'],
                    "CASH_CUST":  promo['CASH_CUST'],
                    "CREDIT_CUST":  promo['CREDIT_CUST'],
                    "LOB": promo['LOB'],
                    "PRD_ASS_TYPE": promo['PRD_ASS_TYPE'],
                    "CUST_ASS_ALL": promo['CUST_ASS_ALL'],
                    "DIST_ASS_ALL": promo['DIST_ASS_ALL'],
                    "GEO_HIER_ID":  promo['GEO_HIER_ID'],
                    "PRD_HIER_ID":  promo['PRD_HIER_ID'],
                    "CUST_HIER_ID":  promo['CUST_HIER_ID'],
                    "BUDGET":  promo['BUDGET'],
                    "PROMO_SEQ": 341513,
                    "MECHANIC_TYPE_VALUE": 3,
                    "MIN_BUY_IND":  promo['MIN_BUY_IND'],
                    "PROMO_PRD_MAPPING": [
                        self.apply_promo_prd_mapping_payload(promo_slab, prd_list)
                    ],
                    "PROMO_FOC_ENTITLED": foc_entitle_payload,
                    "PROMO_FOC_ALLOCATE": foc_allocate_payload,
                    "PROMO_SLABS": [
                        self.apply_promo_slab_payload(promo_slab, prd_info, foc_qty)
                    ],
                    "AVAILABLE_MAX_COUNT": None,
                    "PERIOD": "28/08/2020 - 16/02/2026",
                    "TYPE_DESC": promo_type_desc,
                    "BUY_TYPE_DESC": buy_type_desc,
                    "TOTAL_BUY": promo_slab['TOTAL_BUY'],
                    "PROMO_BENEFIT": promo_benefic,
                    "checked": True,
                    "autoPromoChecked": promo['AUTO_CHECKED'],
                    "REF_CODE": auto_promo[0],
                    "isExclusive": "No",
                    "isFocLinked": is_foc_linked,
                    "allowClicked": False
                }
        return payload

    def search_prd_in_warehouse(self, prd_id):
        prd_list = WarehouseGet().get_warehouse_inventory()
        prd_cd = ""
        prd_desc = ""
        stock = ""
        for prd in prd_list:
            if prd['PRD_ID'] == prd_id:
                prd_cd = prd['PRD_CD']
                prd_desc = prd['PRD_DESC']
                stock = prd['AVAILABLE_QTY_UOM_WISE']

        return prd_cd, prd_desc, stock

    def foc_entitled_payload(self, promo_slab, entitled_foc):
        payload_list = []
        foc = promo_slab['FOC']
        count = 0
        for item in foc:
            if entitled_foc != None:
                foc_qty = entitled_foc[count]['FOC_QTY']
                ori_foc_qty = entitled_foc[count]['ORI_FOC_QTY']
            else:
                ori_foc_qty = 0
                foc_qty = 0
            uom = ProductUomGet.ProductUomGet().user_retrieves_prd_uom_by_id(item['PRDCAT_VALUE_ID'], item['FOC_UOM_ID'])
            prd_cd, prd_desc, stock = self.search_prd_in_warehouse(item['PRDCAT_VALUE_ID'])
            payload = {
                    "PROMO_ID":  promo_slab['PROMO_ID'],
                    "PROMO_SLAB_ID":  promo_slab['ID'],
                    "PRDCAT_ID": None,
                    "PRDCAT_VALUE_ID": item['PRDCAT_VALUE_ID'],
                    "FOC_UOM_ID": item['FOC_UOM_ID'],
                    "COST_PRC": "0.000000",
                    "ORI_FOC_QTY": ori_foc_qty,
                    "FOC_QTY": str(foc_qty),
                    "PROMO_FREQ": "1",
                    "UOM_ID": uom['UOM_ID']['ID'],
                    "UOM_CD": uom['UOM_CD'],
                    "focCondition": "AND",
                    "PRD_ID": item['PRDCAT_VALUE_ID'],
                    "PRD_CD": prd_cd,
                    "PRD_DESC": prd_desc,
                    "STOCK": stock
                }
            payload_list.append(payload)
            count = count + 1
        return payload_list

    def foc_allocate_payload(self, promo_slab, entitled_foc):
        payload_list = []
        foc = promo_slab['FOC']
        count = 0
        for item in foc:
            if entitled_foc != None:
                foc_qty = entitled_foc[count]['FOC_QTY']
                ori_foc_qty = entitled_foc[count]['ORI_FOC_QTY']
            else:
                ori_foc_qty = 0
                foc_qty = 0
            payload = {
                        "PROMO_ID": promo_slab['PROMO_ID'],
                        "PROMO_SLAB_ID": promo_slab['ID'],
                        "PRDCAT_ID": None,
                        "PRDCAT_VALUE_ID": item['PRDCAT_VALUE_ID'],
                        "FOC_UOM_ID": item['FOC_UOM_ID'],
                        "ORI_FOC_QTY": str(ori_foc_qty),
                        "FOC_QTY": str(foc_qty),
                        "PROMO_FREQ": "1",
                        "PRD_ID": item['PRDCAT_VALUE_ID']
                    }
            payload_list.append(payload)
            count = count + 1
        return payload_list


    def apply_promo_slab_payload(self, promo_slab, prd_info, foc_qty):
        dist_perc = str(0)
        if promo_slab['DISC_PERC'] is not None:
            dist_perc = promo_slab['DISC_PERC']
        payload = {
                            "ID": promo_slab['ID'],
                            "PROMO_ID":  promo_slab['PROMO_ID'],
                            "MECHANIC_TYPE":  promo_slab['MECHANIC_TYPE'],
                            "APPLY_ON":  promo_slab['APPLY_ON'],
                            "APPLY_UOM_ID":  promo_slab['APPLY_UOM_ID'],
                            "TOTAL_BUY": promo_slab['TOTAL_BUY'],
                            "MIN_BUY": promo_slab['MIN_BUY'],
                            "MAX_BUY": promo_slab['MAX_BUY'],
                            "FOR_EVERY": promo_slab['FOR_EVERY'],
                            "FOR_EVERY_UOM_ID": promo_slab['FOR_EVERY_UOM_ID'],
                            "FOC_UOM_ID": promo_slab['FOC_UOM_ID'],
                            "FOC_COND": promo_slab['FOC_COND'],
                            "DISC_AMT": promo_slab['DISC_AMT'],
                            "DISC_PERC": dist_perc,
                            "FOC_QTY": str(foc_qty),
                            "SORT_TOTAL_BUY": promo_slab['TOTAL_BUY'],
                            "COMBI_RATIO": "0",
                            "B_TTL_BUY_AMT": str(prd_info[0]['GROSS_AMT']),
                            "B_TTL_BUY_QTY": str(prd_info[0]['BUY_QTY']),
                            "PROMO_FREQ": "1",
                            "ACCU_DISCAMT": "0.000000",
                            "ORI_FOC_QTY": "NaN"
                        }
        return payload

    def apply_promo_prd_mapping_payload(self, promo_slab, prd_list):
        payload = {
                            "PROMO_ID": promo_slab['PROMO_ID'],
                            "PROMO_SLAB_ID": promo_slab['ID'],
                            "PRD_ID": promo_slab['PROMO_PRD'][0]['PRDCAT_VALUE_ID'],
                            "UOM_ID": prd_list[0]['UOM_ID'],
                            "MRP": None,
                            "GROUP_B_TTL_BUY_AMT": "0.000000",
                            "GROUP_B_TTL_BUY_QTY": "0.000000"
                        }
        return payload