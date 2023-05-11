import json
import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Config.ReferenceData.Country.CountryGet import CountryGet
from resources.restAPI.Config.ReferenceData.State.StateGet import StateGet
from resources.restAPI.Config.ReferenceData.Locality.LocalityGet import LocalityGet
from resources.restAPI.MasterDataMgmt.Distributor.DistributorGet import DistributorGet

END_POINT_URL = PROTOCOL + "profile-dist" + APP_URL


class DistributorShipToPost(object):
    """ Functions to create Distributor Ship To """

    @keyword('user creates ship to with ${type} data')
    def user_creates_ship_to_with(self, type):
        """ Function to create ship to with random/fixed data"""
        DistributorGet().user_retrieves_random_distributor()
        dist_id = BuiltIn().get_variable_value("${dist_id}")
        url = "{0}distributors/{1}/shipto".format(END_POINT_URL, dist_id)
        payload = self.payload("create")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${shipto_id}", body_result['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload(self, action):
        """ Function for shipto payload content """

        CountryGet().user_gets_all_countries_data()
        country_list = BuiltIn().get_variable_value("${country_br}")
        rand_country_no = secrets.choice(country_list)
        StateGet().user_gets_all_states_data()
        state_list = BuiltIn().get_variable_value("${state_br}")
        rand_state_no = secrets.choice(state_list)
        state = rand_state_no
        LocalityGet().user_gets_all_localities_data()
        locality_list = BuiltIn().get_variable_value("${locality_br}")
        rand_locality_no = secrets.choice(locality_list)
        locality = rand_locality_no
        if action == "create":
            shipto_cd = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            BuiltIn().set_test_variable("${shipto_cd}", shipto_cd)
        else:
            shipto_cd = BuiltIn().get_variable_value("${shipto_cd}")

        payload = {
            "ADDRESS_CD": {
                "ADD1": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                "ADD2": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                "ADD3": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                "POST_CD": ''.join(secrets.choice('0123456789') for _ in range(5)),
                "LOCALITY": locality,
                "STATE": state,
                "COUNTRY": rand_country_no
            },
            "DEFAULT_SHIPTO": False,
            "SHIPTO_CD": shipto_cd,
            "SHIPTO_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        }
        payload = json.dumps(payload)
        print("Ship To Payload: ", payload)
        return payload


