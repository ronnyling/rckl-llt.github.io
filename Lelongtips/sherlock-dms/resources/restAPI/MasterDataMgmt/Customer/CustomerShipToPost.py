import secrets

from resources.restAPI.Config.ReferenceData.Country.CountryGet import CountryGet
from resources.restAPI.Config.ReferenceData.Locality.LocalityGet import LocalityGet
from resources.restAPI.Config.ReferenceData.State.StateGet import StateGet
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
import json

CUST_END_POINT_URL = PROTOCOL + "profile-cust" + APP_URL


class CustomerShipToPost(object):
    SHIPTO_ID = "${shipto_id}"
    DISTRIBUTOR_ID = "${distributor_id}"
    CUSTOMER_ID = "${cust_id}"

    @keyword('user creates customer shipto')
    def user_creates_customer_shipto(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        url = "{0}distributors/{1}/customer/{2}/cust-shipto".format(CUST_END_POINT_URL,
                                                                    dist_id, cust_id)
        common = APIMethod.APIMethod()
        payload = self.payload_shipto()
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload)
        body_result = response.json()
        shipto_id = body_result['ID']
        BuiltIn().set_test_variable("${shipto_id}", shipto_id)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return body_result

    def payload_shipto(self):
        locality_br = LocalityGet().user_gets_all_localities_data_new()
        state_br = StateGet().user_gets_all_states_data_new()
        country_br = CountryGet().user_gets_all_countries_data_new()
        locality_id = locality_br[0]['ID']
        state_id = state_br[0]['ID']
        country_id = country_br[0]['ID']

        payload = {
            "DEFAULT_SHIPTO": False,
            "ADDRESS_CD": {
                "ADD1": "mymumshouse",
                "ADD2": "mymumshouse",
                "ADD3": "mymumshouse",
                "POST_CD": "mymumshous",
                "LOCALITY": {
                    "ID": locality_id
                },
                "STATE": {
                    "ID": state_id
                },
                "COUNTRY": {
                    "ID": country_id
                }
            },
            "SHIPTO_CD": "mymumshouse" + str(secrets.randbelow(9999)),
            "SHIPTO_DESC": "mymumshouse"
        }
        return payload