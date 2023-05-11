""" Python file related to reward setup API """
import json

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, TokenAccess, APIAssertion
from resources.restAPI.PerformanceMgmt.Gamification.Rewards import RewardsGet, RewardsDelete, \
    RewardsPost

END_POINT_URL_REWARD = PROTOCOL + "gamification" + APP_URL + "gamification-reward-setup"


class RewardsPut:
    """ Functions related to reward setup PUT request """

    def validate_user_scope_on_put_reward_setup(self, user_role, expected_status):
        """ Functions to validate user scope on PUT reward setup """
        common = TokenAccess.TokenAccess()
        common.user_retrieves_token_access_as(user_role)

        if user_role == "hqadm" or user_role == "sysimp":
            common = RewardsPost.RewardsPost()
            common.user_creates_reward_setup_using_data("random")

        dic = {"REWARD_DESC": "Reward_Desc"}
        BuiltIn().set_test_variable("${RewardSetupDetails}", dic)
        self.i_update_created_reward_setup_using_data()
        status_code = BuiltIn().get_variable_value("${status_code}")
        print("PUT_status_code", status_code)

        common = APIAssertion.APIAssertion()
        common.expected_return_status_code(expected_status)

        if user_role == "sysimp":
            common = RewardsDelete.RewardsDelete()
            common.user_deletes_created_reward_setup()

    @keyword('I update created reward setup using fixed data')
    def i_update_created_reward_setup_using_data(self):
        """ Functions to update created reward setup using fixed data """
        reward_setup_id = BuiltIn().get_variable_value("${reward_setup_id}")
        update_data = BuiltIn().get_variable_value("${RewardSetupDetails}")

        url = END_POINT_URL_REWARD
        if reward_setup_id:
            url = "{0}/{1}".format(END_POINT_URL_REWARD, reward_setup_id)
            payload = self.update_created_reward_setup_payload(update_data)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)

        BuiltIn().set_test_variable("${status_code}", response.status_code)
        try:
            body_result = response.json()
            print("Result: ", body_result)
            BuiltIn().set_test_variable("${body_result}", body_result)
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)

    def update_created_reward_setup_payload(self, update_data):
        """ Functions to update created reward setup payload """
        common = RewardsGet.RewardsGet()
        common.user_retrieves_reward_setup("created")
        existing_data = BuiltIn().get_variable_value("${body_result}")
        print("existing_data", existing_data)
        del existing_data["IS_DELETED"]
        del existing_data["MODIFIED_DATE"]
        del existing_data["MODIFIED_BY"]
        del existing_data["CREATED_DATE"]
        del existing_data["CREATED_BY"]
        for item in existing_data["GAME_REWARD_DTL"]:
            del item["ID"]
            del item["REWARD_ID"]
            del item["IS_DELETED"]
            del item["MODIFIED_DATE"]
            del item["MODIFIED_BY"]
            del item["CREATED_DATE"]
            del item["CREATED_BY"]
            del item["VERSION"]
        for item in existing_data["GAME_REWARD_BADGE"]:
            del item["ID"]
            del item["REWARD_ID"]
            del item["BADGE_CD"]
            del item["BADGE_DESC"]
            del item["IS_DELETED"]
            del item["MODIFIED_DATE"]
            del item["MODIFIED_BY"]
            del item["CREATED_DATE"]
            del item["CREATED_BY"]
            del item["VERSION"]
        for item in existing_data["GAME_REWARD_PRD"]:
            del item["ID"]
            del item["REWARD_ID"]
            del item["PRD_HIER_ID"]
            del item["PRD_ENTITY_ID"]
            del item["IS_DELETED"]
            del item["MODIFIED_DATE"]
            del item["MODIFIED_BY"]
            del item["CREATED_DATE"]
            del item["CREATED_BY"]
            del item["VERSION"]
            del item["PRD_CD"]
            del item["PRD_DESC"]
            del item["PRD_VALUE"]
        print("existing_data", existing_data)
        print("update_data", update_data)
        existing_data.update((k, v) for k, v in update_data.items())
        print("payload after update", existing_data)
        return json.dumps(existing_data)
