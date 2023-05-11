""" Python file related to vs score card API """
import datetime
import json

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.PerformanceMgmt.VisionStore.ScoreCardSetup import ScoreCardSetupGet

END_POINT_URL_KPI_ASSIGNMENT = PROTOCOL + "vs-scorecard" + APP_URL + "kpi-assignment"
NOW = datetime.datetime.now()


class ScoreCardSetupPut:
    """ Functions related to vs score card PUT request """

    def user_generates_payload_for_kpi_assignment(self):
        """ Functions to generate payload for kpi assignment """
        existing_payload = ScoreCardSetupGet.ScoreCardSetupGet().get_vsscorecard_kpi_assignment()
        details = BuiltIn().get_variable_value("${VSScoreCardDetails}")
        print("existing_payload", existing_payload)
        existing_payload[0].update((k, v) for k, v in details.items())

        return json.dumps([existing_payload[0]])

    @keyword("user updates kpi assignment using ${data_type} data")
    def user_updates_kpi_assignment_using_data(self, data_type):
        """ Functions to update kpi assignment using random/fixed data """
        payload = self.user_generates_payload_for_kpi_assignment()
        kpi_assignment_id = BuiltIn().get_variable_value("${kpi_assignment_id}")
        if kpi_assignment_id:
            url = "{0}/{1}".format(END_POINT_URL_KPI_ASSIGNMENT, kpi_assignment_id)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print("PUT URL", url)
        print("PUT payload", payload)
        data = response.json()
        print("Result:", data)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
