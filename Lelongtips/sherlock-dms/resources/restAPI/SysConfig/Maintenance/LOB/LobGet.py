from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json


END_POINT_URL = PROTOCOL + "setting" + APP_URL


class LobGet(object):

    def user_retrieves_lob(self, default):
        lob_filter = {"DEFAULT_IND": {"$eq": default}}
        lob_filter = json.dumps(lob_filter)
        url = "{0}lob-ref?filter={1}".format(END_POINT_URL, lob_filter)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve default LOB"
        body_result = response.json()
        assign_to_id = body_result[0]['ID']
        BuiltIn().set_test_variable("${assign_to_id}", assign_to_id)
        BuiltIn().set_test_variable("${lob_reponse_body}", response.json())
        return assign_to_id
