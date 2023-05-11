""" Python file related to team setup API """
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL_REWARD = PROTOCOL + "gamification" + APP_URL + "team"


class TeamsDelete:
    """ Functions related to team setup DELETE request """

    def user_deletes_created_team_setup(self):
        """ Functions to delete created team setup """
        url = END_POINT_URL_REWARD
        team_setup_id = BuiltIn().get_variable_value("${team_setup_id}")
        if team_setup_id:
            url = "{0}/{1}".format(END_POINT_URL_REWARD, team_setup_id)

        print("url", url)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")

        BuiltIn().set_test_variable("${status_code}", response.status_code)

        assert str(response.status_code) == "200" or str(response.status_code) == "403", "Status Code is not match"
