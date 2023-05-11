""" Python file related to reward setup API """
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, APIAssertion, TokenAccess
from resources.restAPI.PerformanceMgmt.Gamification.Rewards import RewardsDelete, RewardsPost
from resources.Common import Common

END_POINT_URL = PROTOCOL + "gamification" + APP_URL + "gamification-reward-setup"


class RewardsGet:
    """ Functions related to reward setup GET request """

    @keyword("user retrieves ${data_type} reward setup")
    def user_retrieves_reward_setup(self, data_type):
        """ Functions to retrieve all reward setup """
        url = END_POINT_URL

        if data_type == "created":
            reward_setup_id = BuiltIn().get_variable_value("${reward_setup_id}")
            url = "{0}/{1}".format(END_POINT_URL, reward_setup_id)

        print("GET URL", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

        try:
            body_result = response.json()
            print("Result: ", body_result)
            BuiltIn().set_test_variable("${body_result}", body_result)
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)

    def user_retrieves_reward_setup_within_start_end_date(self, start_date, end_date):
        """ Functions to retrieve all reward setup """
        url = END_POINT_URL

        print("GET URL", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

        try:
            body_result = response.json()
            print("Result: ", body_result)
            BuiltIn().set_test_variable("${body_result}", body_result)
            for dic in body_result:
                fixed_start_date = start_date
                fixed_end_date = end_date
                reward_start = dic["START_DT"]
                reward_end = dic["END_DT"]
                if reward_start <= fixed_start_date < reward_end and reward_start < fixed_end_date <= reward_end:
                    random_reward_setup_id = dic["ID"]
                    print("dict", dic)
                    print("random_reward_setup_id: ", random_reward_setup_id)
                    BuiltIn().set_test_variable("${random_reward_setup_id}", random_reward_setup_id)
                    BuiltIn().set_test_variable("${random_reward_setup_desc}", dic)
                    break
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)

    def validate_user_scope_on_get_reward_setup(self, user_role, expected_status):
        """ Functions to validate user scope on get reward setup """
        common = TokenAccess.TokenAccess()
        common.user_retrieves_token_access_as(user_role)

        if user_role == "hqadm":
            common = RewardsPost.RewardsPost()
            common.user_creates_reward_setup_using_data("random")

        read_data = self.user_retrieves_reward_setup("random")
        print("read_data", read_data)
        common = APIAssertion.APIAssertion()
        common.expected_return_status_code(expected_status)
        status_code = BuiltIn().get_variable_value(Common.STATUS_CODE)
        print("status_code", status_code)
        if user_role == "sysimp":
            common = RewardsDelete.RewardsDelete()
            common.user_deletes_created_reward_setup()
