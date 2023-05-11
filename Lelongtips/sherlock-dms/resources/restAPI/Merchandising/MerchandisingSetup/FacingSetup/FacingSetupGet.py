from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL

class FacingSetupGet(object):

    @keyword('user retrieves all product groups')
    def user_retrieves_all_product_groups(self):
        url = "{0}merchandising/merc-prod-group".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves product group by ID')
    def user_gets_product_group_by_id(self):
        res_bd_prod_group_id = BuiltIn().get_variable_value("${res_bd_prod_group_id}")
        url = "{0}merchandising/merc-prod-group/{1}".format(END_POINT_URL, res_bd_prod_group_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_prod_group_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)