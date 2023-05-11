""" Python file related to game setup API """
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI.PerformanceMgmt.Gamification.Games import GamesDelete, GamesPost
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import TokenAccess, APIMethod, APIAssertion

END_POINT_URL = PROTOCOL + "gamification" + APP_URL + "game-team"


class GamesGet:
    """ Functions related to game setup GET request """

    @keyword("user retrieves team assignment in ${data_type} game setup")
    def user_retrieves_team_assignment_in_game_setup(self, data_type):
        """ Functions to retrieve all/ created game setup """
        url = END_POINT_URL

        if data_type == "created":
            game_setup_id = BuiltIn().get_variable_value("${game_setup_id}")
            url = "{0}/{1}".format(END_POINT_URL, game_setup_id)

        print("GET URL", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

        try:
            body_result = response.json()
            BuiltIn().set_test_variable("${body_result}", body_result)

        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)

    def validate_user_scope_on_get_game_setup_team(self, user_role, expected_status):
        """ Functions to validate user scope on get request for team assignment in game setup """
        common = TokenAccess.TokenAccess()
        common.user_retrieves_token_access_as(user_role)

        if user_role == "hqadm" or user_role == "sysimp":
            common = GamesPost.GamesPost()
            common.user_creates_game_setup_using_data("random")
            common.user_creates_team_assignment_in_game_setup_using_data("random")

        common = APIAssertion.APIAssertion()
        common.expected_return_status_code(expected_status)
        GamesDelete.GamesDelete().user_deletes_created_game_setup()
