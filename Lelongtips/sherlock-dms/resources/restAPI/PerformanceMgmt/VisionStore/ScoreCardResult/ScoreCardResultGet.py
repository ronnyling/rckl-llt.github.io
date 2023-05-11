"""_Python file related to vs score card API """
import datetime
import secrets

from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

SC_END_POINT_URL = PROTOCOL + "vs-scorecard" + APP_URL
NOW = datetime.datetime.now()


class ScoreCardResultGet:
    """ Functions related to vs score card GET request """
    def user_retrieve_score_card_result_listing(self):
        url = "{0}vs-scorecard-result".format(SC_END_POINT_URL)
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        data = response.json()
        if response.status_code == 200:
            BuiltIn().set_test_variable("${scr_ls}", response.json())
        print("GET data", data)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieve_score_card_result_details(self):
        scr_id = BuiltIn().get_variable_value("${scr_id}")
        if scr_id is None:
            self.user_retrieve_score_card_result_listing()
            scr_ls = BuiltIn().get_variable_value("${scr_ls}")
            rand_sc = secrets.choice(scr_ls)
            scr_id = rand_sc['ID']
            BuiltIn().set_test_variable("${sc_id}", scr_id)

        url = "{0}vs-scorecard-result/{1}".format(SC_END_POINT_URL, scr_id)
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        data = response.json()
        if response.status_code == 200:
            BuiltIn().set_test_variable("${scr_details}", data)
        print("GET data", data)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieve_vision_store_assignment(self):
        sc_id = BuiltIn().get_variable_value("${sc_id}")
        if sc_id is None:
            self.user_retrieve_score_card_setup_listing()
            sc_ls = BuiltIn().get_variable_value("${sc_ls}")
            rand_sc = secrets.choice(sc_ls)
            sc_id = rand_sc['ID']
            BuiltIn().set_test_variable("${sc_id}", sc_id)

        url = "{0}vs-assignment/{1}".format(SC_END_POINT_URL, sc_id)
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        data = response.json()
        if response.status_code == 200:
            BuiltIn().set_test_variable("vsa_details", data)
        print("GET data", data)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieve_kpi_assignment(self):
        sc_id = BuiltIn().get_variable_value("${sc_id}")
        if sc_id is None:
            self.user_retrieve_score_card_setup_listing()
            sc_ls = BuiltIn().get_variable_value("${sc_ls}")
            rand_sc = secrets.choice(sc_ls)
            sc_id = rand_sc['ID']
            BuiltIn().set_test_variable("${sc_id}", sc_id)

        url = "{0}kpi-assignment/scorecard/{1}".format(SC_END_POINT_URL, sc_id)
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        data = response.json()
        if response.status_code == 200:
            BuiltIn().set_test_variable("kpia_details", data)
        print("GET data", data)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieve_kpi_type(self):
        url = "{0}vs-kpi-type".format(SC_END_POINT_URL)
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        data = response.json()
        if response.status_code == 200:
            BuiltIn().set_test_variable("kpi_type_ls", data)
        print("GET data", data)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
