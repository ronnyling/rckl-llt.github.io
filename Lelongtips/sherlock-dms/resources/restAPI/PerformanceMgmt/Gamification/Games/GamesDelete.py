""" Python file related to game setup API """
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL_GAME = PROTOCOL + "gamification" + APP_URL + "game"


class GamesDelete:
    """ Functions related to game setup DELETE request """

    def user_deletes_created_game_setup(self):
        """ Functions to delete created game setup """
        game_setup_id = BuiltIn().get_variable_value("${game_setup_id}")
        url = "{0}/{1}".format(END_POINT_URL_GAME, game_setup_id)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
