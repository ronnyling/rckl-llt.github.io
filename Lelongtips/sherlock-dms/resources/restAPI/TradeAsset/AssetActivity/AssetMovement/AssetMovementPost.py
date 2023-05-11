import json
import secrets
from datetime import datetime

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.TradeAsset.AssetActivity.AssetMovement.AssetMovementGet import AssetMovementGet
from resources.restAPI.TradeAsset.RepairReference.RepairFacility.RepairFacilityGet import RepairFacilityGet

fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class AssetMovementPost(object):
    @keyword("user posts to asset movement")
    def user_posts_to_asset_movement(self):
        url = "{0}trade-asset/asset-movement".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_asset_movement_payload()
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            br = response.json()
            BuiltIn().set_test_variable("${amm_details}", br)
            BuiltIn().set_test_variable("${amm_id}", br[0]['ID'])
        return str(response.status_code), response.json()

    def gen_asset_movement_payload(self):
        AssetMovementGet().user_retrieves_movement_asset_master()
        mam_ls = BuiltIn().get_variable_value("${mam_ls}")
        rand_mam = secrets.choice(mam_ls)
        mam_details = rand_mam
        mam_id = mam_details['ID']

        RepairFacilityGet().user_retrieves_repair_facility_listing()
        rf_ls = BuiltIn().get_variable_value("${rf_ls}")
        rand_rf = secrets.choice(rf_ls)
        rf_details = rand_rf

        AssetMovementGet().user_retrieves_movement_reasons()
        mr_ls = BuiltIn().get_variable_value("${mr_ls}")
        rsn_ls = []
        for i in mr_ls:
            print(str(i))
            if i['PARTY_FR'] == mam_details['LOCATION_TYPE'] and i['PARTY_TO'] == 'R':
                rsn_ls = i['REASONS']
                break
        rand_rsn = secrets.choice(rsn_ls)
        rsn_id = rand_rsn['ID']
        payload = {
            "DOC_NO": 'AM' + ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(7)),
            "INSTALL_DT": str(datetime.today().strftime("%Y-%m-%d")),
            "ASSET": [
                mam_id
            ],
            "FROM_LOC_TYPE": mam_details['LOCATION_TYPE'],
            "FROM_ASSET_LOC_ID": None,
            "FROM_ASSET_COND_ID": mam_details['ASSET_CONDITION']['ID'],
            "FROM_ASSET_STATUS": mam_details['ASSET_STATUS'],
            "TO_LOC_TYPE": "R",
            "TO_ASSET_LOC_ID": None,
            "TO_ASSET_COND_ID": mam_details['ASSET_CONDITION']['ID'],
            "TO_ASSET_STATUS": mam_details['ASSET_STATUS'],
            "TFREASON_ID": rsn_id,
            "SPECIAL_ACT_ID": None
        }
        return payload
