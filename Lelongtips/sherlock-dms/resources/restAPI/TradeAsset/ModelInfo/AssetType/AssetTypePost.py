import json
import secrets

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.MasterDataMgmt.Product.ProductGet import ProductGet
from resources.restAPI.TradeAsset.RepairReference.SparePart.SparePartGet import SparePartGet

fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class AssetTypePost(object):
    @keyword("user posts to trade asset type")
    def user_posts_to_asset_type(self):
        url = "{0}trade-asset/trade-asset-type".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_tat_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            br = response.json()
            BuiltIn().set_test_variable("${tat_id}", br['ID'])
            BuiltIn().set_test_variable("${tat_details}", br)
        return str(response.status_code), response.json()

    def gen_tat_payload(self):
        SparePartGet().user_retrieves_spare_part_listing()
        sp_ls = BuiltIn().get_variable_value("${sp_ls}")
        rand_sp = secrets.choice(sp_ls)
        sp_id = rand_sp['ID']
        sp_map = []
        sp_details = {}
        sp_details['ID'] = sp_id
        sp_map.append(sp_details)

        ProductGet().user_retrieves_prd_by("status", "Active")
        prd_id = BuiltIn().get_variable_value("${prd_id}")
        prd_map = []
        prd_details = {}
        prd_details['ID'] = prd_id
        prd_map.append(prd_details)

        payload = {
            "ASSET-TYPE-MAPPING": [],
            "ASSET-TYPE-SPARE-PART": sp_map,
            "ASSET-TYPE-PRODUCT": prd_map,
            "ASSET_TYPE_CD": "AT" + ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5)),
            "ASSET_TYPE_DESC": None
        }
        return payload
