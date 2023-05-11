""" Python file related to vs score card API """
import datetime
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL_VSSCORECARD = PROTOCOL + "vs-scorecard" + APP_URL + "vs-scorecard"
END_POINT_URL_KPI_ASSIGNMENT = PROTOCOL + "vs-scorecard" + APP_URL + "kpi-assignment"
NOW = datetime.datetime.now()


class ScoreCardSetupDelete:
    """ Functions related to vs scorecard POST request """

    def user_deletes_created_vs_score_card(self):
        vs_score_card_id = BuiltIn().get_variable_value("${vs_score_card_id}")
        url = "{0}/{1}".format(END_POINT_URL_VSSCORECARD, vs_score_card_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
