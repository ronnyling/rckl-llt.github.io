from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL


class ActionCategoryGet(object):

    @keyword("user retrieves ${cond} supervisor action category")
    def user_retrieves_all_action_category(self, cond):
        """ Function to retrieve all  created  action category """
        url = ""
        if cond == 'invalid':
            work_plan_id = Common().generate_random_id("0")
            url = "{0}supervisor-action-category/{1}".format(END_POINT_URL, work_plan_id)
        elif cond == 'all':
            url = "{0}supervisor-action-category".format(END_POINT_URL)
        else:
            work_plan_id = BuiltIn().get_variable_value("${action_category_id}")
            url = "{0}supervisor-action-category/{1}".format(END_POINT_URL, work_plan_id)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${rs_bd_action_category}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)




