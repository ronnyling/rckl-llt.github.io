""" Python file related to reward setup API """
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, TokenAccess
from resources.restAPI.PerformanceMgmt.Gamification.Rewards import RewardsPost

END_POINT_URL_REWARD = PROTOCOL + "gamification" + APP_URL + "gamification-reward-setup"


class RewardsDelete:
    """ Functions related to reward setup DELETE request """

    def validate_user_scope_on_delete_reward_setup(self, user_role):
        """ Functions to validate user scope on DELETE reward setup """
        common = TokenAccess.TokenAccess()
        common.user_retrieves_token_access_as(user_role)
        RewardsPost.RewardsPost().user_creates_reward_setup_using_data("random")
        self.user_deletes_created_reward_setup()

    def user_deletes_created_reward_setup(self):
        """ Functions to delete created reward setup """
        url = END_POINT_URL_REWARD
        reward_setup_id = BuiltIn().get_variable_value("${reward_setup_id}")
        if reward_setup_id:
            url = "{0}/{1}".format(END_POINT_URL_REWARD, reward_setup_id)

        print("url", url)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")

        BuiltIn().set_test_variable("${status_code}", response.status_code)

        if reward_setup_id:
            assert str(response.status_code) == "200" or str(response.status_code) == "403", "Status Code is not match"
        else:
            assert str(response.status_code) == "404", "Status Code is not match"