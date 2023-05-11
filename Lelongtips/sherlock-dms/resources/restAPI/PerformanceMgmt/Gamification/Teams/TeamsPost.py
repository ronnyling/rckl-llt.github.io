""" Python file related to team setup API """
import datetime
import json
import secrets
import string

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, TokenAccess, APIAssertion
from resources.restAPI.PerformanceMgmt.Gamification.Teams import TeamsDelete
from resources.Common import Common

END_POINT_URL = PROTOCOL + "gamification" + APP_URL + "team"
END_POINT_URL_ACTIVE_PRODUCT = PROTOCOL + "metadata" + APP_URL + "module-data/product"
NOW = datetime.datetime.now()


class TeamsPost:
    """ Functions related to team setup POST request """
    TEAM_SETUP_DETAILS = "${TeamSetupDetails}"

    def validate_value_for_status(self, status_value, expected_status):
        """ Functions to validate value for status """
        user_role = BuiltIn().get_variable_value(Common.USER_ROLE)
        TokenAccess.TokenAccess().user_retrieves_token_access_as(user_role)
        dic = {
            "STATUS": status_value
        }
        BuiltIn().set_test_variable(self.TEAM_SETUP_DETAILS, dic)
        self.user_creates_team_setup_using_data("fixed")

        common = APIAssertion.APIAssertion()
        common.expected_return_status_code(expected_status)

        if str(expected_status) == "201":
            TeamsDelete.TeamsDelete().user_deletes_created_team_setup()

    @keyword('user creates team setup using ${data_type} data')
    def user_creates_team_setup_using_data(self, data_type):
        """ Functions to create team setup using random/fixed data """
        url = END_POINT_URL
        if data_type == "fixed":
            fixed_data = BuiltIn().get_variable_value(self.TEAM_SETUP_DETAILS)
            payload = self.create_payload_team(fixed_data)
        else:
            payload = self.create_payload_team(None)

        print("POST url", url)
        print("POST payload", payload)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print("POST response.status_code", response.status_code)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

        try:
            body_result = response.json()
            print("Result: ", body_result)
            BuiltIn().set_test_variable("${team_setup_id}", body_result['ID'])
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)

    def create_payload_team(self, given_data):
        """ Functions to create payload for team setup """
        payload = {
            "TEAM_CD": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(4)),
            "TEAM_NAME": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(4)),
            "STATUS": secrets.choice(["A", "I"]),
            "ASSIGNMENTS": [
                {
                    "assignmentType": "D",
                    "criteriaRelationship": "NONE",
                    "stateChanged": True,
                    "assignAll": True,
                    "criteria": {
                        "main": {
                            "data": []
                        },
                        "hierarchy": {
                            "data": []
                        },
                        "attribute": {
                            "data": []
                        }
                    },
                    "assigned": {
                        "data": []
                    },
                    "excluded": {
                        "data": []
                    }
                },
                {
                    "assignmentType": "O",
                    "criteriaRelationship": "NONE",
                    "stateChanged": True,
                    "assignAll": True,
                    "criteria": {
                        "main": {
                            "data": []
                        },
                        "hierarchy": {
                            "data": []
                        },
                        "attribute": {
                            "data": []
                        }
                    },
                    "assigned": {
                        "data": []
                    },
                    "excluded": {
                        "data": []
                    }
                }
            ]
        }

        if given_data:
            payload.update((k, v) for k, v in given_data.items())

        payload = json.dumps(payload)

        return payload

    def verify_data_length_for_team_code_and_team_name(self, team_code_len, team_name_len, expected_status):
        """ Functions to verify data length for team code and team name """
        alphabet = string.ascii_letters + string.digits
        team_code = ''.join(secrets.choice(alphabet) for _ in range(team_code_len))
        team_name = ''.join(secrets.choice(alphabet) for _ in range(team_name_len))

        user_role = BuiltIn().get_variable_value(Common.USER_ROLE)
        TokenAccess.TokenAccess().user_retrieves_token_access_as(user_role)

        dic = {
            "TEAM_CD": team_code,
            "TEAM_NAME": team_name
        }
        BuiltIn().set_test_variable(self.TEAM_SETUP_DETAILS, dic)
        self.user_creates_team_setup_using_data("fixed")

        common = APIAssertion.APIAssertion()
        common.expected_return_status_code(expected_status)

        if str(expected_status) == "201":
            TeamsDelete.TeamsDelete().user_deletes_created_team_setup()

    def validate_mandatory_fields_for_team_setup(self, key, value, expected_status):
        """ Functions to validate mandatory fields for team setup """
        user_role = BuiltIn().get_variable_value(Common.USER_ROLE)
        TokenAccess.TokenAccess().user_retrieves_token_access_as(user_role)
        dictionary = {key: value}

        BuiltIn().set_test_variable(self.TEAM_SETUP_DETAILS, dictionary)

        self.user_creates_team_setup_using_data("fixed")

        common = APIAssertion.APIAssertion()
        common.expected_return_status_code(expected_status)

        if str(expected_status) == "201":
            TeamsDelete.TeamsDelete().user_deletes_created_team_setup()
