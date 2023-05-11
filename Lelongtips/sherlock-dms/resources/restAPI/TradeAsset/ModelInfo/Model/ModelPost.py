import json
import secrets

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Config.ReferenceData.Country.CountryGet import CountryGet
from resources.restAPI.Config.ReferenceData.Locality.LocalityGet import LocalityGet
from resources.restAPI.Config.ReferenceData.State.StateGet import StateGet
from resources.restAPI.Merchandising.MerchandisingSetup.PosmFocusCustomers.PosmFocusCustomersGet import \
    PosmFocusCustomersGet
from resources.restAPI.SysConfig.Attribute.AttributeModule.AttributeModuleGet import AttributeModuleGet
from resources.restAPI.TradeAsset.ModelInfo.AssetType.AssetTypeGet import AssetTypeGet
from resources.restAPI.TradeAsset.ModelInfo.Manufacturer.ManufacturerGet import ManufacturerGet

fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ModelPost(object):
    @keyword("user posts to model")
    def user_posts_to_model(self):
        url = "{0}trade-asset/asset-model".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_model_payload()
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            br = response.json()
            BuiltIn().set_test_variable("${model_details}", br)
            BuiltIn().set_test_variable("${model_id}", br['ID'])
        return str(response.status_code), response.json()

    def gen_model_payload(self):
        locality_id = {}
        state_id = {}
        country_id = {}

        locality_br = LocalityGet().user_gets_all_localities_data_new()
        state_br = StateGet().user_gets_all_states_data_new()
        country_br = CountryGet().user_gets_all_countries_data_new()

        locality_id["ID"] = locality_br[0]['ID']
        state_id["ID"] = state_br[0]['ID']
        country_id["ID"] = country_br[0]['ID']

        AttributeModuleGet().user_retrieves_attribute_module_by_name('Asset Model')
        att_module_id = BuiltIn().get_variable_value("${att_module_id}")
        PosmFocusCustomersGet().user_retrieve_dynamic_attribute()
        dyn_attr_ls = BuiltIn().get_variable_value("${dyn_attr_ls}")
        mand_am_attr_ls = [i for i in dyn_attr_ls if i['MODULE'] == att_module_id and
                           i['MANDATORY'] == "true"]

        PosmFocusCustomersGet().user_retrieve_attribute_value_creation()
        attr_val_ls = BuiltIn().get_variable_value("${attr_val_ls}")

        asset_model_maps = []
        for mand_attr in mand_am_attr_ls:
            asset_model = {}
            att = {}
            att_id = next((i['ID'] for i in attr_val_ls
                                                    if i['MODULE_SELECTION'] == mand_attr['MODULE'] and
                                                    i['ATTRIBUTE'] == mand_attr['ID']), None)
            att['ID'] = att_id
            asset_model['ATTRIBUTE_VAL_ID'] = att
            asset_model_maps.append(asset_model)

        AssetTypeGet().user_retrieves_trade_asset_type_listing()
        tat_ls = BuiltIn().get_variable_value("${tat_ls}")
        rand_tat = secrets.choice(tat_ls)
        tat_id = rand_tat['ID']

        ManufacturerGet().user_retrieves_manufacturer_listing()
        manu_ls = BuiltIn().get_variable_value("${manu_ls}")
        rand_manu = secrets.choice(manu_ls)
        manu_id = rand_manu['ID']

        payload = {
            "ASSET-MODEL-MAPPING": asset_model_maps,
            "MODEL_CD": 'MOD' + ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5)),
            "MODEL_NM": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5)),
            "ASSET_TYPE_ID": {
                "ID": tat_id
            },
            "MANUFACTURER": {
                "ID": manu_id
            }
        }
        return payload
