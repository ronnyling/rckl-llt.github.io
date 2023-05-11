from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.Common import Common
from resources.restAPI.MasterDataMgmt.Supervisor.ActionCategory import ActionCategoryPost
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL


class ActionCategoryPut(object):

    @keyword("user updates ${cond} supervisor action category")
    def user_updates_supervisor_action_category(self, cond):
        """ Function to update created action category """
        if cond == 'invalid':
            action_category_id = Common().generate_random_id("0")
        else:
            action_category_id = BuiltIn().get_variable_value("${action_category_id}")
        url = "{0}supervisor-action-category/{1}".format(END_POINT_URL, action_category_id)
        payload = ActionCategoryPost.ActionCategoryPost().action_category_payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${rs_bd_action_category}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)




