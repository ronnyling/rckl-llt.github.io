import secrets, json
from datetime import datetime,timedelta
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Supervisor.WorkPlan import WorkPlanGet
from resources.restAPI.MasterDataMgmt.Supervisor.Checklist import ChecklistGet
END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL

class ChecklistPut(object):
    CHECKLIST_ID = "${res_bd_checklist_id}"
    DT_FORMAT = '%Y-%m-%d'
    @keyword('user updates created checklist with ${type} data')
    def user_updates_checklist(self, type):
        if type == "past start date":
            ChecklistGet.ChecklistGet.user_retrieves_all_checklists(self)
            res_bd_checklist_id = BuiltIn().get_variable_value("${past_checklist_id}")
            BuiltIn().set_test_variable("${res_bd_checklist_id}", res_bd_checklist_id)
        else:
            res_bd_checklist_id = BuiltIn().get_variable_value(self.CHECKLIST_ID)
        url = "{0}supervisor-checklist/{1}".format(END_POINT_URL, res_bd_checklist_id)
        payload = self.payload_checklist(res_bd_checklist_id,type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_checklist(self, checklist_id, type):
        checklist = ChecklistGet.ChecklistGet().user_gets_checklist_by_id(checklist_id)
        if type == "code":
            checklist['CHECKLIST_CD'] = ''.join(
                secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(10))
        CHECKLIST_DESC = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(20))
        CHECKLIST_ITEM_DESC = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(10))
        CHECKLIST_ITEM_CD = ''.join(
            secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(5))
        STATUS = secrets.choice(['A', 'I'])
        start_date_obj = datetime.strptime(checklist['START_DT'], self.DT_FORMAT)
        end_date_obj = datetime.strptime(checklist['END_DT'], self.DT_FORMAT)
        td1 = timedelta(days=3)
        td2 = timedelta(days=10)
        START_DT = (start_date_obj + td1).strftime(self.DT_FORMAT)
        END_DT = (end_date_obj + td2).strftime(self.DT_FORMAT)
        if checklist['CHECKLIST_TYPE'] == 'R':
            field = "FEEDBACK_REQUIRED"
        elif checklist['CHECKLIST_TYPE'] == 'S':
            field = "Both"
        wp_item = (WorkPlanGet.WorkPlanGet().get_random_work_plan_by_field_and_value(field, "true"))['ID']

        payload = {

                "CHECKLIST_ITEM": [
                    {
                        "ID": checklist['CHECKLIST_ITEM'][0]['ID'],
                        "CHECKLIST_ITEM_CODE": CHECKLIST_ITEM_CD,
                        "CHECKLIST_ITEM_DESC": CHECKLIST_ITEM_DESC
                    }
                ],
                "STATUS": STATUS,
                "CHECKLIST_CD": checklist['CHECKLIST_CD'],
                "CHECKLIST_DESC": CHECKLIST_DESC,
                "CHECKLIST_TYPE": checklist['CHECKLIST_TYPE'],
                "START_DT": START_DT,
                "END_DT": END_DT,
                "WORK_PLAN_ITEM": [
                    {
                        "ID": wp_item
                    }
                ],
                "ID": checklist['ID']

        }
        details = BuiltIn().get_variable_value("${new_checklist_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Checklist Payload: ", payload)
        return payload

