import secrets
import json
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Supervisor.WorkPlan import WorkPlanGet
from datetime import datetime,timedelta
END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL

class ChecklistPost(object):

    @keyword('user creates checklist with ${data_type} data')
    def user_creates_checklist_with(self, data_type):
        url = "{0}supervisor-checklist".format(END_POINT_URL)
        payload = self.payload_checklist(data_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${res_bd_checklist_payload}", body_result)
            BuiltIn().set_test_variable("${res_bd_checklist_id}", body_result["ID"])
            BuiltIn().set_test_variable("${res_bd_checklist_cd}", body_result["CHECKLIST_CD"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_checklist(self, data_type):

        CHECKLIST_CD = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(10))
        CHECKLIST_DESC = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(20))
        CHECKLIST_TYPE = secrets.choice(['R', 'S'])
        CHECKLIST_ITEM_CD = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(10))
        CHECKLIST_ITEM_DESC = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(10))
        if CHECKLIST_TYPE == 'R':
            field = "FEEDBACK_REQUIRED"
        else:
            field = "Both"
        wp_item = (WorkPlanGet.WorkPlanGet().get_random_work_plan_by_field_and_value(field, "true"))['ID']
        STATUS = secrets.choice(['A', 'I'])
        today_date = datetime.now()
        td1 = timedelta(days=2)
        td2 = timedelta(days=7)
        START_DT = (today_date+td1).strftime('%Y-%m-%d')
        END_DT = (today_date + td2).strftime('%Y-%m-%d')
        payload = {
            "CHECKLIST_ITEM": [
                {
                    "ID": "0",
                    "CHECKLIST_ITEM_CODE": CHECKLIST_ITEM_CD,
                    "CHECKLIST_ITEM_DESC": CHECKLIST_ITEM_DESC
                }
            ],
            "STATUS": STATUS,
            "CHECKLIST_CD": CHECKLIST_CD,
            "CHECKLIST_DESC": CHECKLIST_DESC,
            "CHECKLIST_TYPE": CHECKLIST_TYPE,
            "START_DT": START_DT,
            "END_DT": END_DT,
            "WORK_PLAN_ITEM": [
                {
                    "ID": wp_item
                }
            ]

        }
        details = BuiltIn().get_variable_value("${checklist_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Checklist Payload: ", payload)
        return payload
