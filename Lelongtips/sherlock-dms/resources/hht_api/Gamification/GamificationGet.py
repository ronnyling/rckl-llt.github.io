""" Python File related to HHT Gamification API """
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.Common import Common
import json

APP_URL = '-svc-qa.cfapps.jp10.hana.ondemand.com/api/v1.0/'
GAMIFICATION_END_POINT_URL = PROTOCOL + "gamification"

class GamificationGet:
    """ Functions related to HHT Gamification GET/SYNC Request """

    @keyword("user retrieves Gamification Setup Header using ${user_file}")
    def get_gamification_setup_header(self, user_file):
        url = "{0}comm/gamification-game-setup".format(GAMIFICATION_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Gamification Ranking using ${user_file}")
    def get_gamification_ranking(self, user_file):
        url = "{0}comm/gamification-game-ranking".format(GAMIFICATION_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Gamification Team and Salesperson Setup using ${user_file}")
    def get_gamification_team_and_salesperson(self, user_file):
        url = "{0}comm/gamification-reference".format(GAMIFICATION_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Gamification Badge Setup using ${user_file}")
    def get_gamification_badge(self, user_file):
        url = "{0}comm/gamification-badge".format(GAMIFICATION_END_POINT_URL + APP_URL)
        parameter = {}
        if user_file == 'hqsalesperson':
            parameter = {'Data': {'REQUEST_DIST_ID': BuiltIn().get_variable_value(Common.DISTRIBUTOR_ID)}}
            parameter = {k: json.dumps(parameter[k]) for k in parameter}
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "", **parameter)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Gamification Badge Attachment Setup")
    def get_gamification_badge_attachment_setup(self):
        url = "{0}comm/attachment/gamification-badge".format(GAMIFICATION_END_POINT_URL + APP_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Gamification Leaderboard")
    def get_gamification_leaderboard(self):
        url = "{0}comm/gamification-route-leaderboard".format(GAMIFICATION_END_POINT_URL + APP_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Gamification Route Rank")
    def get_gamification_route_rank(self):
        url = "{0}comm/gamification-route-rank".format(GAMIFICATION_END_POINT_URL + APP_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves Gamification Route Badge")
    def get_gamification_route_badge(self):
        url = "{0}comm/gamification-route-badge".format(GAMIFICATION_END_POINT_URL + APP_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)