from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from faker import Faker
from faker_e164.providers import E164Provider

FAKE = Faker()
FAKE.add_provider(E164Provider)
FEATURE = 'MULTI_PRINCIPLE'
SETT_END_POINT_URL = PROTOCOL + "setting" + APP_URL
CODE_END_POINT_URL = PROTOCOL + "codetable" + APP_URL


class DistConfigGet(object):


    @keyword('user retrieves all dist configuration')
    def get_dist_config(self):
        url = "{0}dist-configuration/{1}/".format(SETT_END_POINT_URL, FEATURE)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        body = response.json()
        BuiltIn().set_test_variable("${dist_config_res_body}", body)
        BuiltIn().set_test_variable("${status_code}", response.status_code)