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

fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ManufacturerPost(object):
    @keyword("user posts to manufacturer")
    def user_posts_to_manufacturer(self):
        url = "{0}trade-asset/asset-manufacturer".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_manu_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            br = response.json()
            BuiltIn().set_test_variable("${manu_id}", br['ID'])
            BuiltIn().set_test_variable("${manu_details}", br)
        return str(response.status_code), response.json()

    def gen_manu_payload(self):
        locality_id = {}
        state_id = {}
        country_id = {}

        locality_br = LocalityGet().user_gets_all_localities_data_new()
        state_br = StateGet().user_gets_all_states_data_new()
        country_br = CountryGet().user_gets_all_countries_data_new()

        locality_id["ID"] = locality_br[0]['ID']
        state_id["ID"] = state_br[0]['ID']
        country_id["ID"] = country_br[0]['ID']
        payload = {
            "ADDRESS_CD": {
                "ADD1": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                "ADD2": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                "ADD3": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                "POST_CD": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                "STATE": state_id,
                "LOCALITY": locality_id,
                "COUNTRY": country_id
            },
            "MAN_CD": 'Manu' + ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "MAN_NAME": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        }
        return payload
