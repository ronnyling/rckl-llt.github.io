from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Merchandising.ActivitySetup.Checklist import ChecklistPost
import json

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ChecklistPut(object):

    @keyword('user updates merchandising checklist using ${data} data')
    def user_updates_merchandising_checklist(self, data):
        payload = ChecklistPost.ChecklistPost().payload(data)
        url = "{0}merchandising-checklist".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, json.dumps(payload))
        if response.status_code == 201:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${checklist_id}", body_result['HEADER']['ID'])
            BuiltIn().set_test_variable("${activity_id}", body_result['ACTIVITIES'][0]['ID'])
            BuiltIn().set_test_variable("${cl_bd_res}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
