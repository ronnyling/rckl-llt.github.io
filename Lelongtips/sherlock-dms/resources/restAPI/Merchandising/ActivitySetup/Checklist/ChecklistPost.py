from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json
import secrets
import datetime

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL
current_date = datetime.datetime.now()


class ChecklistPost(object):

    def payload(self, data):
        if data == 'fixed':
            cl_details = BuiltIn().get_variable_value("${checklist_details}")
            cl_desc = cl_details['CHECKLIST_DESC']
            start_date = cl_details['START_DATE']
            end_date = cl_details['END_DATE']
            act_cd = cl_details['ACTIVITY_CODE']
            act_desc = cl_details['ACTIVITY_DESC']
        else:
            random_string = ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            cl_desc = random_string
            act_cd = random_string
            act_desc = random_string
            start_date = str((current_date + datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
            end_date = str((current_date + datetime.timedelta(days=2)).strftime("%Y-%m-%d"))

        payload = {
            "STATUS": secrets.choice(["Active", "Inactive"]),
            "CHECKLIST_DESC": cl_desc,
            "START_DATE": start_date,
            "END_DATE": end_date,
            "ACTIVITIES": [
                {
                    "ACTIVITY_CD": act_cd,
                    "ACTIVITY_DESC": act_desc,
                    "STATUS": secrets.choice(["Active", "Inactive"])
                }
            ]
        }
        cl_id = BuiltIn().get_variable_value('${checklist_id}')
        act_id = BuiltIn().get_variable_value('${activity_id}')
        if cl_id is not None:
            payload['ID'] = cl_id
            payload['ACTIVITIES'][0]['ID'] = act_id
            payload['ACTIVITIES'][0]['CHECKLIST'] = cl_id
        return payload

    @keyword('user adds merchandising checklist using ${data} data')
    def user_adds_merchandising_checklist(self, data):
        payload = self.payload(data)
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
