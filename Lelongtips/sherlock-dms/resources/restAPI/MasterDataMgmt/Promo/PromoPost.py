from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.MasterDataMgmt.Promo import PromoBuyTypeGet
from resources.restAPI.Config.ReferenceData.Uom.UomGet import UomGet
from setup.hanaDB import HanaDB
from resources.restAPI.MasterDataMgmt.Product import ProductGet
from resources.restAPI.Common import TokenAccess
import json, secrets, datetime

NOW = datetime.datetime.now()
PROMO_END_POINT_URL = PROTOCOL + "promotion" + APP_URL


class PromoPost(object):

    DT_FORMAT = "%Y-%m-%dT00:00:00.000Z"
    @keyword('user creates promotion with fixed data')
    def create_promotion(self):
        """
        This function is to create promotion
        payload of promotion are splitting into 3 main part
        promotion general info, promo slab , and promo slab product assignment

        :param promo_details:


        :return: status code return from api
        """
        promo_details = BuiltIn().get_variable_value("${promo_details}")
        promo_slab = self.promo_slab_payload(**promo_details)
        promo_details['Slabs'] = promo_slab
        promo_payload = self.promo_general_payload(**promo_details)
        print("Promo==", promo_payload)
        url = "{0}promotion".format(PROMO_END_POINT_URL)
        role = BuiltIn().get_variable_value("${role}")
        user_role = BuiltIn().get_variable_value("${user_role}")
        if role is not None:
            user_role = role
        TokenAccess.TokenAccess().get_token_by_role(user_role)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, promo_payload)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${promo}", body_result)
            promotion_id = body_result['ID']
            promotion_cd = body_result['PROMO_CD']
            HanaDB.HanaDB().connect_database_to_environment()
            HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM PROMO where ID = '{0}'".format(promotion_id), 1)
            HanaDB.HanaDB().disconnect_from_database()
            BuiltIn().set_test_variable("${promo_id}", promotion_id)
            BuiltIn().set_test_variable("${promotion_cd}", promotion_cd)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return response.status_code

    def retrieve_and_save_prd_info(self, csv_flag, item, prd):
        if csv_flag:
            item = json.loads(item)
        product_code = item['PRD_CODE']
        prd.append(ProductGet.ProductGet().user_retrieves_prd_by_prd_code(product_code)['ID'])
        return prd

    def promo_prd_payload(self, **promo_details):
        """
        This function is return payload of product assignment of the slab
        promotion able to assign to multiple product


        :param promo_details:
        :return: list of the promo product assignment details
        """
        prd_assignment = promo_details.get('PROD_ASS_DETAILS')
        prd = []
        csv_flag = False
        if isinstance(prd_assignment, str):
            csv_flag = True
            if ";" in prd_assignment:
                prd_assignment = prd_assignment.split(';')

        if isinstance(prd_assignment, list):
            for item in prd_assignment:
                prd = self.retrieve_and_save_prd_info(csv_flag, item, prd)
        else:
            prd = self.retrieve_and_save_prd_info(csv_flag, prd_assignment, prd)


        promo_prd = []
        for prd_id in prd:
            promo_prd_details = {
                "ID": None,
                "PROMO_SLAB_ID": None,
                "PRDCAT_ID": None,
                "PRDCAT_VALUE_ID": prd_id,
                "UOM_ID": None,
                "MIN_QTY": None,
                "MUST_IND": None,
                "VERSION": 1,
                "action": "create"
            }
            promo_prd.append(promo_prd_details)
        return promo_prd

    def check_dist_method(self, disc_method, value):
        payload = {}
        if disc_method == "DiscountByPerc":
            payload['DISC_PERC'] = int(value)
        else:
            payload['DISC_AMT'] = str(value)
        return payload

    def promo_slab_payload(self, **promo_details):
        """
        This function is to create promotion slab
        in default we will have maximum 3 slab
        slabs will be store in a list and loop it
        while looping it will break the slab with :
        and use those info to complete the promo slab discount details

        :param promo_details:
        :return:

        """
        promo_prd = self.promo_prd_payload(**promo_details)


        slabs = []
        slab = [promo_details.get('SLAB_1'), promo_details.get('SLAB_2'), promo_details.get('SLAB_3')]
        if promo_details.get("APPLY_UOM") is not None:
            print("inside promo", promo_details)
            apply_uom_id = UomGet().user_retrieves_uom_by_code_in_uom_listing(promo_details.get("APPLY_UOM"))['ID']
        else:
            apply_uom_id = None
        for item in slab:
            if item == "":
                break
            data = item.split("/")
            slab = {
                    "ID": None,
                    "PROMO_ID": None,
                    "MECHANIC_TYPE": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_promo_mechanic_type(promo_details.get('DISC_METHOD'), "refParam")[0]['ID'],
                    "APPLY_ON": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_apply_on(promo_details.get('APPLY_ON'))['ID'],
                    "APPLY_UOM_ID": apply_uom_id,
                    "TOTAL_BUY": int(data[0]),
                    "MIN_BUY": 0,
                    "MAX_BUY": 0,
                    "FOR_EVERY": 0,
                    "FOR_EVERY_UOM_ID": None,
                    "FOC_UOM_ID": None,
                    "FOC_COND": None,
                    "DISC_AMT": "0.0000",
                    "DISC_PERC": 0.000,
                    "FOC_QTY": None,
                    "VERSION": 0,
                    "action": "create",
                    "FOC": [],
                    "PROMO_PRD": promo_prd,
                    "PROMO_COMBI_GROUP": []
                }
            details = self.check_dist_method(promo_details.get("DISC_METHOD"), data[1])
            slab.update((k, v) for k, v in details.items())
            slabs.append(slab)
        return slabs

    def string_to_boolean(self, string):
        flag = True
        if string == "FALSE":
            flag = False
        return flag

    def promo_general_payload(self, **promo_details):
        promo_cd = promo_details.get('PROMO_CD')
        promo_desc = promo_details.get('PROMO_DESC')
        if promo_details.get('BUY_UOM'):
            buy_uom_id = UomGet().user_retrieves_uom_by_code_in_uom_listing(promo_details.get('BUY_UOM'))['ID']
        else:
            buy_uom_id = None
        if promo_cd == 'random':
            promo_cd = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15))
        if promo_desc == 'random':
            promo_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15))
        BuiltIn().set_test_variable("${promo_cd}", promo_cd)
        st_date = str((NOW + datetime.timedelta(days=1)).strftime(self.DT_FORMAT))
        end_date = str((NOW + datetime.timedelta(days=1000)).strftime(self.DT_FORMAT))
        claim_end_date = str((NOW + datetime.timedelta(days=1200)).strftime(self.DT_FORMAT))
        BuiltIn().set_test_variable("${claim_end_date}", claim_end_date)
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        promo = {
            "ID": None,
            "PROMO_CD": promo_cd,
            "PROMO_DESC": promo_desc,
            "START_DT": st_date,
            "END_DT": end_date,
            "SPACEBUY_END_DT": None,
            "CLAIMABLE_IND": True,
            "CLAIM_ENDDT": claim_end_date,
            "TYPE": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_promo_type(promo_details.get('PROMO_TYPE'), 'refParam')[0]['ID'],
            "PRIME_FLAG": "PRIME",
            "PROMO_SEQ_ID": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_promo_seq_by_code(promo_details.get('PROMO_CAT'))['ID'],
            "BUY_TYPE": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_promo_buy_type(promo_details.get('BUY_TYPE'), 'refParam')[0]['ID'],
            "BUY_UOM_ID": buy_uom_id,
            "CLAIM_TYPE_ID": "41C373A2:7B364AD2-3A94-438E-94C3-EB1374B796D3",
            "AUTO_CHECKED": False,
            "AUTO_PROMO": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_auto_promo(promo_details.get('APPLY_PROMO'))['ID'],
            "SCHEME_QPS": False,
            "SCHEME_PRORATA": self.string_to_boolean(promo_details.get('SCHEME_PRORATA')),
            "SCHEME_RANGE": self.string_to_boolean(promo_details.get('SCHEME_RANGE')),
            "SCHEME_COMBI": False,
            "SCHEME_MRP": False,
            "SCHEME_POSM_ASSIGNMENT": False,
            "DISC_METHOD": False,
            "FOC_RECURRING": False,
            "MAX_COUNT_FLAG": False,
            "MAX_COUNT": 0,
            "FOR_EVERY_FLAG": self.string_to_boolean(promo_details.get('FOR_EVERY_FLAG')),
            "PROMO_STATUS": PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_promo_status(promo_details.get('STATUS'))['ID'],
            "APPR_IND": None,
            "APPR_DT": None,
            "NOTES": None,
            "RETAIL_CAP_FLAG": False,
            "RETAILER_CAP": None,
            "EXCL_PROMO": False,
            "NEW_POS": False,
            "BATCH": False,
            "MIN_BUY_IND": self.string_to_boolean(promo_details.get('MIN_BUY_IND')),
            "CASH_CUST": None,
            "CREDIT_CUST": None,
            "LOB": "725CF01F:D37928F6-F57B-48AE-8334-2D962D934737",
            "PRD_ASS_TYPE":  PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_prod_assign_type(promo_details.get('PROD_ASS_TYPE'))['ID'],
            "CUST_ASS_ALL": False,
            "DIST_ASS_ALL": False,
            "PRD_HIER_ID": "5E306ADB:A7493D33-401F-4BA3-BF7C-CD2B2BDF44EC",
            "GEO_HIER_ID": None,
            "CUST_HIER_ID": None,
            "BUDGET": "0.00",
            "SERVICE_TAX_ID": None,
            "SPACEBUY_PAYOUT_CUST_SPEC": False,
            "PROMO_SLABS": promo_details['Slabs'],
            "PROMO_PRD_EX": [],
            "PROMO_MRP": [],
            "VERSION": 0,
            "action": "create",
            "CLAIMABLE_PERC": 100
        }
        self.update_promo_payload(promo)
        BuiltIn().set_test_variable("${promo_payload}", promo)
        promo = json.dumps(promo)
        return promo

    def update_promo_payload(self, promo):
        role = BuiltIn().get_variable_value("${role}")
        if role is not None:
            user_role = role
        else:
            user_role = BuiltIn().get_variable_value("${user_role}")
        details = BuiltIn().get_variable_value("${promo_update}")
        if user_role == "distadm":
            promo['SCHEME_POSM_ASSIGNMENT'] = False
            promo['CLAIMABLE_IND'] = False
            promo['CLAIM_ENDDT'] = None
            promo['CLAIMABLE_PERC'] = None
            promo['CLAIM_TYPE_ID'] = None
        if details:
            promo.update((k, v) for k, v in details.items())
        return promo

    @keyword("user updates promotion start date as ${date}")
    def set_start_promotion(self, date):
        promo_id = BuiltIn().get_variable_value("${promo_id}")
        if date == 'today':
            st_date = str(NOW.strftime("%Y-%m-%d %H:%M:%S.000000000"))
        elif date == 'tomorrow':
            st_date = str((NOW + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S.000000000"))
        else:
            st_date = date + " 00:00:00.000000000"
        promo_id = COMMON_KEY.convert_id_to_string(promo_id)
        HanaDB.HanaDB().connect_database_to_environment()
        update_query = "UPDATE PROMO SET START_DT = '{0}' WHERE ID ='{1}'".format(st_date, promo_id)
        print(update_query)
        result = HanaDB.HanaDB().execute_sql_string(update_query)
        print("DB Result", result)
        HanaDB.HanaDB().disconnect_from_database()

    def user_creates_fixed_promotion_as_prerequisite(self):
        promo_details = {
            "CUST_ASS_ALL": "FALSE",
            "DIST_ASS_ALL": "FALSE",
            "FOR_EVERY_FLAG": "FALSE",
            "SCHEME_RANGE": "FALSE",
            "SCHEME_PRORATA": "FALSE",
            "MIN_BUY_IND" : "FALSE",
            "APPLY_ON": "PerTier",
            "APPLY_PROMO": "Manual",
            "BUY_TYPE": "Amount",
            "BUY_UOM": None,
            "DISC_METHOD": "DiscountByPerc",
            "PROD_ASS_DETAILS": [{
                "PRD_CODE": "A1002",
                "PRD_UOM": [
                    {
                       "QTY": "10",
                       "UOM": "EA"
                    }
                ]
            }],
            "PROD_ASS_TYPE": "Hierarchy",
            "PROMO_CAT": "random",
            "PROMO_CD": "random",
            "PROMO_DESC": "random",
            "PROMO_RULE": None,
            "PROMO_TYPE": "PromoNDeal",
            "SLAB_1": "100/2",
            "SLAB_2": "300/3",
            "SLAB_3": "500/4",
            "STATUS": "Active",
            "DIST": "DistEgg",
            "ROUTE": "Rchoon",
            "WAREHOUSE": "whtt",
            "CUST": "CXTESTTAX"
        }
        promo_update = {
            "SCHEME_POSM_ASSIGNMENT": True
        }
        BuiltIn().set_test_variable("${promo_details}", promo_details)
        BuiltIn().set_test_variable("${promo_update}", promo_update)
