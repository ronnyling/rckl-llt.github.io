""" Python file related to badge setup API """
import secrets

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, TokenAccess

END_POINT_URL = PROTOCOL + "gamification" + APP_URL + "gamification-badge"


class BadgesGet:
    """ Functions related to badge setup GET request """

    @keyword("user retrieves ${data_type} badge setup")
    def user_retrieves_badge_setup(self, data_type):
        """ Functions to retrieve all/random badge setup """
        user_role = BuiltIn().get_variable_value("${user_role}")
        common = TokenAccess.TokenAccess()
        common.user_retrieves_token_access_as(user_role)

        url = END_POINT_URL

        print("GET URL", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

        try:
            body_result = response.json()
            print("Result: ", body_result)
            BuiltIn().set_test_variable("${body_result}", body_result)

            if data_type == "random":
                random_count = secrets.choice(body_result)
                random_id = random_count['ID']
                print("Random id: ", random_id)
                BuiltIn().set_test_variable("${random_id}", random_id)

        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)
