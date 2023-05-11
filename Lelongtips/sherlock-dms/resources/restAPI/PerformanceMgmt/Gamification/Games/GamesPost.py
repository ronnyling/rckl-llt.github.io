""" Python file related to game setup API """
import datetime
import json
import secrets
import string

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.PerformanceMgmt.Gamification.Games import GamesGet, GamesDelete
from resources.restAPI.PerformanceMgmt.Gamification.Rewards import RewardsGet
from resources.restAPI.Common import TokenAccess, APIMethod, APIAssertion

END_POINT_URL_GAME_TEAM = PROTOCOL + "gamification" + APP_URL + "game-team"
END_POINT_URL_GAME = PROTOCOL + "gamification" + APP_URL + "game"


class GamesPost:
    """ Functions related to game setup POST request """
    TEST = "test{0}"

    @keyword("user creates game setup using ${data_type} data")
    def user_creates_game_setup_using_data(self, data_type):
        """ Functions to create game setup using random data """
        url = END_POINT_URL_GAME

        if data_type == "random":
            payload = self.create_payload_game_setup(fixed_data=None)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

        try:
            body_result = response.json()
            BuiltIn().set_test_variable("${game_setup_id}", body_result['ID'])

        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)

    def create_payload_game_setup(self, fixed_data):
        """ Functions to create payload for game setup """
        alphabet = string.digits + string.ascii_letters
        random_char = ''.join(secrets.choice(alphabet) for _ in range(5))
        start_date = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime("%Y-%m-%d")
        end_date = (datetime.datetime.today() + datetime.timedelta(days=36)).strftime("%Y-%m-%d")
        RewardsGet.RewardsGet().user_retrieves_reward_setup_within_start_end_date(start_date, end_date)
        random_reward_setup_id = BuiltIn().get_variable_value("${random_reward_setup_id}")
        payload = {
            "GAME_CD": self.TEST.format(random_char),
            "GAME_DESC": self.TEST.format(random_char),
            "START_DT": start_date,
            "END_DT": end_date,
            "FREQUENCY": "O",
            "STATUS": "A",
            "GAME_RULE": [
                {
                    "ID": random_reward_setup_id
                }
            ],
            "GAME_RANKING": [
                {
                    "RANK_NAME": self.TEST.format(random_char),
                    "RANGE_FROM": 0,
                    "RANGE_TO": 1  # hardcoded temporary
                }
            ]
        }

        if fixed_data:
            payload.update((k, v) for k, v in fixed_data.items())

        payload = json.dumps(payload)
        print("payload",payload)
        return payload

    @keyword("user creates team assignment in game setup using ${data_type} data")
    def user_creates_team_assignment_in_game_setup_using_data(self, data_type):
        """ Functions to create team assignment in game setup using random data """
        game_setup_id = BuiltIn().get_variable_value("${game_setup_id}")
        url = "{0}/{1}".format(END_POINT_URL_GAME_TEAM, game_setup_id)

        if data_type == "random":
            payload = self.create_payload_game_setup_team(fixed_data=None)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def create_payload_game_setup_team(self, fixed_data):
        """ Functions to create payload for team assignment in game setup """
        GamesGet.GamesGet().user_retrieves_team_assignment_in_game_setup("all")
        body_result = BuiltIn().get_variable_value("${body_result}")
        count = len(body_result)
        random_number = secrets.randbelow(count - 1)

        payload = {
            "TEAM_ID": body_result[random_number]["TEAM_ID"]
        }
        if fixed_data:
            payload.update((k, v) for k, v in fixed_data.items())
        payload = json.dumps([payload])

        return payload

    def validate_user_scope_on_post_game_setup_team(self, user_role, expected_status):
        """ Functions to validate user scope on post request for team assignment in game setup """
        common = TokenAccess.TokenAccess()
        common.user_retrieves_token_access_as(user_role)
        self.user_creates_game_setup_using_data("random")
        self.user_creates_team_assignment_in_game_setup_using_data("random")
        common = APIAssertion.APIAssertion()
        common.expected_return_status_code(expected_status)
        GamesDelete.GamesDelete().user_deletes_created_game_setup()
