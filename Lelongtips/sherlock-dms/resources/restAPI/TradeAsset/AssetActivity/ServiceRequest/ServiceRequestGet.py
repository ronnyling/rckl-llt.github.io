import secrets

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ServiceRequestGet(object):

    @keyword("user retrieves service request listing")
    def user_retrieves_service_request_listing(self):
        url = "{0}trade-asset/asset-service-request".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${amm_ls}", response.json())
        return str(response.status_code), response.json()

    @keyword("user retrieves service request details")
    def user_retrieves_service_request_details(self):
        asr_id = BuiltIn().get_variable_value("${asr_id}")
        if not asr_id:
            self.user_retrieves_service_request_listing()
            asr_ls = BuiltIn().get_variable_value("${asr_ls}")
            rand_asr = secrets.choice(asr_ls)
            asr_id = rand_asr['ID']

        url = "{0}trade-asset/asset-service-request/{1}".format(END_POINT_URL, asr_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${ae_details}", response.json())
        return str(response.status_code)

    def user_retrieves_service_request_models(self):
        url = "{0}trade-asset/asset-service-request-model".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${srm_ls}", response.json())
        return str(response.status_code)
