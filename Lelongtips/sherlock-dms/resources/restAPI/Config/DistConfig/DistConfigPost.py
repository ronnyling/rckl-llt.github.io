import json
import secrets
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from faker import Faker
from faker_e164.providers import E164Provider
from resources.restAPI.Common import TokenAccess, APIMethod, APIAssertion
from resources.restAPI.Config.AppSetup.AppSetupGet import AppSetupGet
from resources.restAPI.Config.AppSetup.AppSetupPut import AppSetupPut
from resources.restAPI.Config.DistConfig import DistConfigGet

FAKE = Faker()
FAKE.add_provider(E164Provider)
FEATURE = 'MULTI_PRINCIPLE'
SETT_END_POINT_URL = PROTOCOL + "setting" + APP_URL
CODE_END_POINT_URL = PROTOCOL + "codetable" + APP_URL


class DistConfigPost(object):

    @keyword('user creates dist config using ${data} data')
    def post_dist_config(self, data):

        dist_list = BuiltIn().get_variable_value("${dist_list}")
        payload = ""
        url = "{0}dist-configuration/{1}".format(SETT_END_POINT_URL, FEATURE)
        e_list = []
        for item in dist_list:
            payload = self.payload(**item)
            self.search_dist(item['DIST_NAME'])
            dist_id = BuiltIn().get_variable_value("${dist__id}")
            dist_id_config = BuiltIn().get_variable_value("${dist_config_id}")
            payload['ID'] = dist_id_config
            payload['DIST_ID'] = dist_id
            del payload['DIST_NAME']
            e_list.append(payload)
        e_list = json.dumps(e_list)
        print("elist", e_list)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, e_list)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload(self, **dist_info):
        payload = {
             "ID" : None,
             "DIST_ID": "",
             "FEATURE_STATUS": secrets.choice([True, False])
        }
        payload.update((k, v) for k, v in dist_info.items())
        return payload

    def search_dist(self, dist_name):
        d_body = BuiltIn().get_variable_value("${dist_config_res_body}")
        flag = False
        for item in d_body:
            if dist_name == item['DIST_NAME']:
                BuiltIn().set_test_variable("${dist__id}", item['DIST_ID'])
                BuiltIn().set_test_variable("${dist_config_id}", item['ID'])
                flag = True
                break;
        assert flag is True, "Dist Not Found"

    @keyword('user switches ${status} multi principal')
    def user_switches_multi_principal(self, status):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("sysimp")
        DistConfigGet.DistConfigGet().get_dist_config()
        APIAssertion.APIAssertion().expected_return_status_code("200")
        AppSetupGet().user_retrieves_details_of_application_setup()
        if status == 'On':
            status = True
            AppSetupPut().user_updates_app_setup_details_using_data("multi_on")
        else:
            status = False
            AppSetupPut().user_updates_app_setup_details_using_data("multi_off")

        dist_info = {
            "DIST_NAME": "Eggy Global Company",
            "FEATURE_STATUS": status
        }
        dist_list = []
        dist_list.append(dist_info)
        BuiltIn().set_test_variable("${dist_list}", dist_list)
        BuiltIn().set_test_variable("${multi_status}", status)
        self.post_dist_config("given")
        APIAssertion.APIAssertion().expected_return_status_code("201")
