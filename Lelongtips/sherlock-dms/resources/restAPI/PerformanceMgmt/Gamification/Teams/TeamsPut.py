""" Python file related to team setup API """
import datetime
import json

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.PerformanceMgmt.Gamification.Teams import TeamsGet

END_POINT_URL = PROTOCOL + "gamification" + APP_URL + "team"
END_POINT_URL_ACTIVE_PRODUCT = PROTOCOL + "metadata" + APP_URL + "module-data/product"
NOW = datetime.datetime.now()


class TeamsPut:
    """ Functions related to team setup PUT request """

    @keyword("user updates created team setup using ${data_type} data")
    def user_updates_created_team_setup_using_data(self, data_type):
        """ Functions to update created reward setup using fixed data """
        team_setup_id = BuiltIn().get_variable_value("${team_setup_id}")
        update_data = BuiltIn().get_variable_value("${TeamSetupDetails}")

        url = END_POINT_URL
        if team_setup_id:
            url = "{0}/{1}".format(END_POINT_URL, team_setup_id)
            payload = self.update_created_team_setup_payload(update_data)

        print("PUT url", url)
        print("PUT payload", payload)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)

        BuiltIn().set_test_variable("${status_code}", response.status_code)
        try:
            body_result = response.json()
            print("Result: ", body_result)
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)

    def update_created_team_setup_payload(self, update_data):
        """ Functions to update created team setup payload """
        common = TeamsGet.TeamsGet()
        common.user_retrieves_team_setup("created")
        existing_data = BuiltIn().get_variable_value("${body_result}")
        print("existing_data", existing_data)
        existing_data.update((k, v) for k, v in update_data.items())
        print("payload after update", existing_data)
        return json.dumps(existing_data)
