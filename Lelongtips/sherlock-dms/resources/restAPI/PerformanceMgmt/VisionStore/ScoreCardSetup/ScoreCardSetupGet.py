"""_Python file related to vs score card API """
import datetime
import secrets

from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL_KPI_ASSIGNMENT = PROTOCOL + "vs-scorecard" + APP_URL + "kpi-assignment"
SC_END_POINT_URL = PROTOCOL + "vs-scorecard" + APP_URL
NOW = datetime.datetime.now()


class ScoreCardSetupGet:
    """ Functions related to vs score card GET request """

    def get_vsscorecard_kpi_assignment(self):
        """ Functions to get vsscorecard kpi assignment """
        vs_score_card_id = BuiltIn().get_variable_value("${vs_score_card_id}")
        if vs_score_card_id:
            url = "{0}/scorecard/{1}".format(END_POINT_URL_KPI_ASSIGNMENT, vs_score_card_id)

        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        data = response.json()
        print("GET data", data)
        BuiltIn().set_test_variable("${kpi_assignment_id}", data[0]["ID"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

        return data

    def user_retrieve_score_card_setup_listing(self):
        url = "{0}vs-scorecard".format(SC_END_POINT_URL)
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        data = response.json()
        if response.status_code == 200:
            BuiltIn().set_test_variable("${sc_ls}", response.json())
        print("GET data", data)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieve_score_card_setup_details(self):
        sc_id = BuiltIn().get_variable_value("${sc_id}")
        if sc_id is None:
            self.user_retrieve_score_card_setup_listing()
            sc_ls = BuiltIn().get_variable_value("${sc_ls}")
            rand_sc = secrets.choice(sc_ls)
            sc_id = rand_sc['ID']
            BuiltIn().set_test_variable("${sc_id}", sc_id)

        url = "{0}vs-scorecard/{1}".format(SC_END_POINT_URL, sc_id)
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        data = response.json()
        if response.status_code == 200:
            BuiltIn().set_test_variable("${sc_details}", data)
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
            BuiltIn().set_test_variable("${vsa_details}", data)
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
            BuiltIn().set_test_variable("$kpia_details", data)
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
