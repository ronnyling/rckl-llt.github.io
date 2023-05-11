""" Python file related to team setup API """
import datetime

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "gamification" + APP_URL + "team"
END_POINT_URL_ACTIVE_PRODUCT = PROTOCOL + "metadata" + APP_URL + "module-data/product"
NOW = datetime.datetime.now()


class TeamsGet:
    """ Functions related to team setup GET request """

    @keyword("user retrieves ${data_type} team setup")
    def user_retrieves_team_setup(self, data_type):
        """ Functions to retrieve all team setup """
        url = END_POINT_URL

        if data_type == "created":
            team_setup_id = BuiltIn().get_variable_value("${team_setup_id}")
            url = "{0}/{1}".format(END_POINT_URL, team_setup_id)

        print("GET URL", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

        try:
            body_result = response.json()
            print("Result: ", body_result)
            BuiltIn().set_test_variable("${body_result}", body_result)
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)
