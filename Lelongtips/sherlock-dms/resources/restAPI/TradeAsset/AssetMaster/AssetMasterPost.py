import json
import secrets
from datetime import datetime
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Config.AppSetup.AppSetupGet import AppSetupGet
from resources.restAPI.TradeAsset.AssetReference.AssetCondition.AssetConditionGet import AssetConditionGet
from resources.restAPI.TradeAsset.ModelInfo.Model.ModelGet import ModelGet

fake = Faker()
END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class AssetMasterPost(object):
    @keyword("user posts to asset master")
    def user_posts_to_asset_master(self):
        url = "{0}trade-asset/asset-master".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_asset_master_payload()
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            br = response.json()
            BuiltIn().set_test_variable("${am_details}", br)
            BuiltIn().set_test_variable("${am_id}", br['ID'])
        return str(response.status_code)

    def gen_asset_master_payload(self):
        ModelGet().user_retrieves_manufacturer_listing()
        model_ls = BuiltIn().get_variable_value("${model_ls}")
        rand_model = secrets.choice(model_ls)
        model_id = rand_model['ID']

        AssetConditionGet().user_retrieves_asset_condition_listing()
        ac_ls = BuiltIn().get_variable_value("${ac_ls}")
        rand_ac = secrets.choice(ac_ls)
        ac_id = rand_ac['ID']

        payload = {
            "ACQ_DT": str(datetime.today().strftime("%Y-%m-%dT%H:%M:%S.000Z")),
            "ASSET_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "MODEL_DETAIL": {
                "ID": model_id
            },
            "ASSET_CONDITION": {
                "ID": ac_id
            },
            "ASSET_STATUS": "P",
            "LOCATION_TYPE": "S"
        }
        return payload
