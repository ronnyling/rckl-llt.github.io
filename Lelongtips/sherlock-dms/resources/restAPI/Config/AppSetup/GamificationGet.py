""" Python file related to application setup API """
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL_GEO_LEVEL_LEADERBOARD = PROTOCOL + "dynamic-hierarchy" + APP_URL + "structure/hier/"
END_POINT_URL_GEO_HIER = PROTOCOL + "dynamic-hierarchy" + APP_URL + "structure/active/geo tree"


class GamificationGet(object):
    """ Functions related to application setup - gamification GET request """

    def user_retrieves_geo_hier_id(self):
        """ Functions to retrieve option values for geo hierarchy id """
        url = END_POINT_URL_GEO_HIER
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${geo_hier_id}", body_result[0]["hierId"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_option_values_geo_level_leaderboard(self, fixed_data):
        """ Functions to retrieve option values for geo level leaderboard """
        self.user_retrieves_geo_hier_id()
        geo_hier_id = BuiltIn().get_variable_value("${geo_hier_id}")
        url = "{0}{1}".format(END_POINT_URL_GEO_LEVEL_LEADERBOARD, geo_hier_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            geo_level_leaderboard_id = []
            for dic in body_result["levels"]:
                if dic["name"] == fixed_data:
                    geo_level_leaderboard_id.append(dic["treeId"])
                    break
            BuiltIn().set_test_variable("${geo_level_leaderboard_id}", geo_level_leaderboard_id)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
