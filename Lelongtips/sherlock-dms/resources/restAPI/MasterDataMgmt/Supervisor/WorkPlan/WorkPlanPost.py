import json, secrets
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL


class WorkPlanPost(object):

    @keyword("user creates supervisor work plan with ${cond} data")
    def user_creates_work_plan_with_data(self, cond):
        """ Function to create work plan """
        payload = self.work_plan_payload()
        url = "{0}supervisor-work-plan-item".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("testing", body_result)
            BuiltIn().set_test_variable("${work_plan_id}", body_result['ID'])
            BuiltIn().set_test_variable("${work_plan_cd}", body_result['WORK_PLAN_ITEM_CODE'])
            BuiltIn().set_test_variable("${rs_bd_work_plan}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)


    def work_plan_payload(self):
        payload = {
            "WORK_PLAN_ITEM_CODE": 'WP' + str(secrets.choice(range(1, 9999999))),
            "WORK_PLAN_ITEM_DESC": 'WP DESC' + str(secrets.choice(range(1, 9999999))),
            "NO_OF_TIMES_PER_DAY":  secrets.choice(range(1, 10)),
            "FEEDBACK_REQUIRED": False
        }
        workplan_details = BuiltIn().get_variable_value("${work_plan_details}")
        if workplan_details:
            payload.update((k, v) for k, v in workplan_details.items())
        payload = json.dumps(payload)
        print("print payload", payload)
        return payload
