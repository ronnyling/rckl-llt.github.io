import secrets

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL

class StoreSpaceGet(object):
    RES_BD_STORE_SPACE_ID="${res_bd_store_space_id}"
    RES_BD_STORE_SPACE_LEVEL_ID="${res_bd_store_space_level_id}"

    @keyword('user retrieves all store spaces')
    def user_retrieves_all_store_spaces(self):
        url = "{0}merchandising/merc-store-space".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_so = secrets.randbelow(len(body_result))
            else:
                rand_so = 0
            BuiltIn().set_test_variable("${rand_store_id}", body_result[rand_so]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves all store spaces level')
    def user_retrieves_all_store_spaces_level(self):
        url = "{0}merchandising/merc-store-space-all".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable("${rand_level_id}", body_result[0]["LEVEL_ID"])
            BuiltIn().set_test_variable("${rand_cust_group_id}", body_result[0]["CUST_GROUP_ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves store space by ID')
    def user_gets_store_space_by_id(self):
        res_bd_store_space_id = BuiltIn().get_variable_value(self.RES_BD_STORE_SPACE_ID)
        url = "{0}merchandising/merc-store-space/{1}".format(END_POINT_URL, res_bd_store_space_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_store_space_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword('user retrieves store space level by ID')
    def user_gets_store_space_level_by_id(self):
        res_bd_store_space_id = BuiltIn().get_variable_value(self.RES_BD_STORE_SPACE_ID)
        res_bd_store_space_level_id = BuiltIn().get_variable_value(self.RES_BD_STORE_SPACE_LEVEL_ID)
        url = "{0}merchandising/merc-store-space/{1}/merc-store-space-level/{2}".format(END_POINT_URL,res_bd_store_space_id, res_bd_store_space_level_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_store_space_level_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)