# import json
# import secrets
# from datetime import datetime
#
# from robot.api.deco import keyword
# from robot.libraries.BuiltIn import BuiltIn
# from faker import Faker
# from resources.restAPI.Common import APIMethod
# from resources.restAPI import PROTOCOL, APP_URL
# from resources.restAPI.Config.AppSetup.AppSetupGet import AppSetupGet
# from resources.restAPI.Config.ReferenceData.Country.CountryGet import CountryGet
# from resources.restAPI.Config.ReferenceData.Locality.LocalityGet import LocalityGet
# from resources.restAPI.Config.ReferenceData.State.StateGet import StateGet
# from resources.restAPI.Merchandising.MerchandisingSetup.PosmFocusCustomers.PosmFocusCustomersGet import \
#     PosmFocusCustomersGet
# from resources.restAPI.SysConfig.Attribute.AttributeModule.AttributeModuleGet import AttributeModuleGet
# from resources.restAPI.TradeAsset.ModelInfo.AssetType.AssetTypeGet import AssetTypeGet
# from resources.restAPI.TradeAsset.ModelInfo.Manufacturer.ManufacturerGet import ManufacturerGet
#
# fake = Faker()
#
# END_POINT_URL = PROTOCOL + "merchandising" + APP_URL
#
#
# class AssetExceptionPost(object):
#
#     # @keyword("user retrieves manufacturer listing")
#     # def user_retrieves_manufacturer_listing(self):
#     #     url = "{0}trade-asset/asset-manufacturer".format(END_POINT_URL)
#     #     common = APIMethod.APIMethod()
#     #     response = common.trigger_api_request("GET", url, "")
#     #     BuiltIn().set_test_variable("${status_code}", response.status_code)
#     #     if response.status_code == 200:
#     #         BuiltIn().set_test_variable("${manu_ls}", response.json())
#     #     return str(response.status_code), response.json()
#
#     @keyword("user posts to asset exception")
#     def user_posts_to_asset_exception(self):
#         # manu_id = BuiltIn().get_variable_value("${manu_id}")
#         # if not manu_id:
#         #     self.user_retrieves_manufacturer_listing()
#         #     manu_ls = BuiltIn().get_variable_value("${manu_ls}")
#         #     rand_manu = secrets.randbelow(len(manu_ls))
#         #     manu_id = manu_ls[rand_manu]
#
#         url = "{0}trade-asset/asset-exception".format(END_POINT_URL)
#         common = APIMethod.APIMethod()
#         payload = self.gen_asset_exception_payload()
#         payload = json.dumps(payload)
#         print("payload = " + str(payload))
#         response = common.trigger_api_request("POST", url, payload)
#         BuiltIn().set_test_variable("${status_code}", response.status_code)
#         if response.status_code == 201:
#             br = response.json()
#             BuiltIn().set_test_variable("${ae_details}", br)
#             BuiltIn().set_test_variable("${ae_id}", br['ID'])
#         return str(response.status_code), response.json()
#
#     def gen_asset_exception_payload(self):
#         AppSetupGet().user_retrieves_details_of_application_setup()
#         app_setup = BuiltIn().get_variable_value("${body_result}")
#         app_setup['COMPANY_NAME']
#
#         payload = {
#             "ACQ_DT": str(datetime.today().strftime("%Y-%m-%dT%H:%M:%S.000Z")),
#             "LOCATION_TYPE": "S",
#             "ASSET_STATUS": "P",
#             # "ASSET_LOC_DESC": "ekaterra",
#             # "ASSET_DESC": "testdelete",
#             "MODEL_DETAIL": {
#                 "ID": "0424F054:852DDB01-0EED-4302-BFC5-64CD053A38D7",
#                 "MODEL_CD": "MOD2",
#                 "MODEL_NM": "Model Square",
#                 "ASSET_TYPE_ID": {
#                     "ID": "63759191:A8671DEB-EA96-4C4C-8F14-61AE1F1EBBDC",
#                     "ASSET_TYPE_DESC": "Asset2"
#                 },
#                 "MANUFACTURER": {
#                     "ID": "9EF5EFEE:A20F8ADF-BB8C-4A02-B374-55E02D5A46BD",
#                     "MAN_NAME": "M Manufacturer"
#                 },
#                 "MODIFIED_DATE": "2023-03-27 10:27:27.990000000",
#                 "ASSET_MODEL_MAPPING": [
#                     {
#                         "ID": "0F747D1F:BAF828B9-25CD-48F5-9489-09337FEFBA3E",
#                         "ASSET_MODEL_ID": "0424F054:852DDB01-0EED-4302-BFC5-64CD053A38D7",
#                         "ATTRIBUTE_VAL_ID": "5745DFBB:FFB64EA6-F51C-4904-B696-384DB8A8BEA4",
#                         "IS_DELETED": false,
#                         "MODIFIED_DATE": "2023-03-27 10:27:28.184000000",
#                         "MODIFIED_BY": "54AAA1DF79E6EA15652C416CB1AD2BCC20227ECE",
#                         "CREATED_DATE": "2022-11-23 12:43:02.100000000",
#                         "CREATED_BY": "54AAA1DF20FD5989BAF948C9A49EC04A803997FA",
#                         "VERSION": 2,
#                         "CORE_FLAGS": null,
#                         "ATTRIBUTE_VALUE": "Make Year",
#                         "ATTRIBUTE_NAME": "ATM001"
#                     }
#                 ],
#                 "ATM001": "Make Year",
#                 "_DESC": "MOD2 - Model Square"
#             },
#             "MANUFACTURER": "M Manufacturer",
#             "ASSET_TYPE_ID": "Asset2",
#             "ASSET_CONDITION": {
#                 "ID": "A25035DC:143CEF14-AA7C-47E2-92DC-6F48F433FB03",
#                 "ASSET_COND_CD": "ACC02",
#                 "ASSET_COND_DESC": "Asset Good",
#                 "IS_DELETED": false,
#                 "MODIFIED_DATE": "2022-11-23 12:37:05.614000000",
#                 "MODIFIED_BY": "54AAA1DF20FD5989BAF948C9A49EC04A803997FA",
#                 "CREATED_DATE": "2022-11-23 12:37:05.614000000",
#                 "CREATED_BY": "54AAA1DF20FD5989BAF948C9A49EC04A803997FA",
#                 "VERSION": 1,
#                 "CORE_FLAGS": null
#             },
#             "ASSET_LOCATION": None
#         }
#         return payload
