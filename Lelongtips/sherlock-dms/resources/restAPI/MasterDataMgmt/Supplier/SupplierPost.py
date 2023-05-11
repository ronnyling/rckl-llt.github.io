import secrets
from resources.restAPI import PROTOCOL, APP_URL
import json
from resources.restAPI.Common import APIMethod, TokenAccess
from resources.restAPI.Config.ReferenceData.Country import CountryPost
from resources.restAPI.Config.ReferenceData.Country.CountryGet import CountryGet
from resources.restAPI.Config.ReferenceData.Locality import LocalityPost
from resources.restAPI.Config.ReferenceData.Locality.LocalityGet import LocalityGet
from resources.restAPI.Config.ReferenceData.State import StatePost
from resources.restAPI.Config.ReferenceData.State.StateGet import StateGet
from resources.restAPI.Config.TaxMgmt.TaxGroup import TaxGroupGet
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

from resources.restAPI.MasterDataMgmt.Supplier.SupplierGet import SupplierGet
END_POINT_URL = PROTOCOL + "setting" + APP_URL


class SupplierPost:

    @keyword("user creates supplier with ${data_type} data")
    def user_create_supplier_with(self, data_type):
        url = "{0}supplier".format(END_POINT_URL)
        payload = self.payload_supplier(data_type)
        payload = json.dumps(payload)
        print (payload)
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        print("POST Status code for supplier is " + str(response.status_code))
        body_result = response.json()
        if response.status_code == 201:
            print(body_result)
            BuiltIn().set_test_variable("${status_code}", response.status_code)
            BuiltIn().set_test_variable("${supplier_id}", body_result["ID"])
        return body_result['ID']

    def payload_supplier(self, data_type):
        details = BuiltIn().get_variable_value("${supplier_details}")
        if not details:
            details = {}
        if details.get("PRIME_FLAG"):
            prime_flag = details["PRIME_FLAG"]
        else:
            prime_flag = secrets.choice(["PRIME", "NON_PRIME"])
        city_id = BuiltIn().get_variable_value("${res_bd_locality_id}")
        state_id = BuiltIn().get_variable_value("${res_bd_state_id}")
        country_id = BuiltIn().get_variable_value("${res_bd_country_id}")
        if prime_flag == "NON_PRIME":
            tax_group = BuiltIn().get_variable_value("${np_tax_group_id}")
        else:
            tax_group = BuiltIn().get_variable_value("${tax_group_id}")
        if data_type == 'random':
            tax_group_ls = TaxGroupGet.TaxGroupGet().retrieve_get_tax_group_by_type("S")
            locality_br = LocalityGet().user_gets_all_localities_data_new()
            country_br = CountryGet().user_gets_all_countries_data_new()
            state_br = StateGet().user_gets_all_states_data_new()

            tax_group = tax_group_ls['ID']
            city_id = locality_br[0]['ID']
            state_id = state_br[0]['ID']
            country_id = country_br[0]['ID']

        payload = {
            "SUPP_CD": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15)),
            "SUPP_NAME": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
            "REG_NO": str(secrets.choice(range(100000, 200000))),
            "PRIME_FLAG": prime_flag,
            "DEFAULT_SUPP": False,
            "TAX_GROUP": {
                "ID": tax_group
            },
            "MAIN_ADDRESS": {
                "ADD1": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                "ADD2": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                "ADD3": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                "POST_CD": ''.join(secrets.choice('0123456789') for _ in range(5)),
                "LOCALITY": {
                    "ID": city_id
                },
                "STATE": {
                    "ID": state_id
                },
                "COUNTRY": {
                    "ID": country_id
                }
            },
            "CONTACT_PERSON": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
            "MOBILE_NO": ''.join(secrets.choice('0123456789') for _ in range(10)),
            "TELEPHONE_NO": ''.join(secrets.choice('0123456789') for _ in range(10)),
            "EMAIL_ADDRESS": ''.join(secrets.choice('0123456789') for _ in range(10)) +\
                             ''.join(secrets.choice(["@gmail.com", "@yahoo.com", "@hotmail.com"]))
        }
        if data_type == "fixed":
            payload = SupplierGet().user_retrieves_supplier_by_id()[1]
        payload.update((k, v) for k, v in details.items())
        return payload

    def user_creates_supplier_as_prerequisite(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("sysimp")
        CountryPost.CountryPost().user_creates_country_as_prerequisite()
        StatePost.StatePost().user_creates_state_as_prerequisite()
        LocalityPost.LocalityPost().user_creates_locality_as_prerequisite()
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        TaxGroupGet.TaxGroupGet().user_get_random_tax_group_by_principal_flag("PRIME")
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        TaxGroupGet.TaxGroupGet().user_get_random_tax_group_by_principal_flag("NON_PRIME")
        self.user_create_supplier_with("random")
