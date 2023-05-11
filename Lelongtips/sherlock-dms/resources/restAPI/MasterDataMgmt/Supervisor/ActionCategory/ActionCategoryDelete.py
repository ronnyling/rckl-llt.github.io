import random
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL


class ActionCategoryDelete(object):

    @keyword("user deletes ${cond} supervisor action category")
    def user_delete_action_category(self, cond):
        """ Function to delete  created  action_category """
        if cond == 'invalid':
            action_category_id = Common().generate_random_id("0")
        else:
            action_category_id = BuiltIn().get_variable_value("${action_category_id}")
        url = "{0}supervisor-action-category/{1}".format(END_POINT_URL, action_category_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("Delete", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

