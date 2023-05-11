import json
import secrets
from datetime import datetime
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Config.AppSetup.AppSetupGet import AppSetupGet
from resources.restAPI.TradeAsset.AssetActivity.ServiceRequest.ServiceRequestGet import ServiceRequestGet

fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ServiceRequestPost(object):
    @keyword("user posts to service request")
    def user_posts_to_service_request(self):
        url = "{0}trade-asset/asset-service-request".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_service_request_payload()
        payload = json.dumps(payload)
        print("payload = " + str(payload))
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            br = response.json()
            BuiltIn().set_test_variable("${asr_details}", br)
            BuiltIn().set_test_variable("${asr_id}", br['ID'])
        return str(response.status_code), response.json()

    def gen_service_request_payload(self):
        ServiceRequestGet().user_retrieves_service_request_models()
        srm_ls = BuiltIn().get_variable_value("${srm_ls}")
        rand_srm = secrets.choice(srm_ls)
        srm_id = rand_srm['ID']
        payload = {
            "TXN_AST_SERVICEHDR": {
                "TXN_DT": str(datetime.today().strftime("%Y-%m-%d")),
                "SERVICE_TYPE": "P",
                "SERVICE_STATUS": "P",
                "TOTAL_COST": 0,
                "ASSET_ID": srm_id,
                "ID": srm_id
            }
        }
        return payload
