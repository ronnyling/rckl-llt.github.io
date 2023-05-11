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


class RepairFacilityPost(object):
    @keyword("user posts to repair facility")
    def user_posts_to_repair_facility(self):
        url = "{0}trade-asset/repair-facility".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_repair_facility_payload()
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            br = response.json()
            BuiltIn().set_test_variable("${rf_details}", br)
            BuiltIn().set_test_variable("${rf_id}", br['ID'])
        return str(response.status_code), response.json()

    def gen_repair_facility_payload(self):
        locality_br = LocalityGet().user_gets_all_localities_data_new()
        state_br = StateGet().user_gets_all_states_data_new()
        country_br = CountryGet().user_gets_all_countries_data_new()
        locality_id = locality_br[0]['ID']
        state_id = state_br[0]['ID']
        country_id = country_br[0]['ID']
        payload = {
            "REP_FAC_CD": 'RF' + ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5)),
            "REP_FAC_NAME": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "ADDRESS_CD": {
                "ADD1": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(7)),
                "ADD2": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(7)),
                "ADD3": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(7)),
                "POST_CD": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(7)),
                "STATE": {
                    "ID": state_id
                },
                "LOCALITY": {
                    "ID": locality_id
                },
                "COUNTRY": {
                    "ID": country_id
                }
            }
        }
        return payload
