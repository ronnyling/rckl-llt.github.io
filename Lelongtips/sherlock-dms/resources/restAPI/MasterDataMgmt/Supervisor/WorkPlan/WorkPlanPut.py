from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.Common import Common
from resources.restAPI.MasterDataMgmt.Supervisor.WorkPlan import WorkPlanPost
from resources.restAPI.MasterDataMgmt.Supervisor.WorkPlan import WorkPlanDelete
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL


class WorkPlanPut(object):

    @keyword("user updates ${cond} supervisor work plan")
    def user_updates_supervisor_work_plan(self, cond):
        """ Function to retrieve all  created  work plan """
        work_plan_id = ""
        if cond == 'predefined':
            work_plan_id = WorkPlanDelete.WorkPlanDelete().search_predefined_data()
        elif cond == 'invalid':
            work_plan_id = Common().generate_random_id("0")

        else:
            work_plan_id = BuiltIn().get_variable_value("${work_plan_id}")
        url = "{0}supervisor-work-plan-item/{1}".format(END_POINT_URL, work_plan_id)
        payload = WorkPlanPost.WorkPlanPost().work_plan_payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${rs_bd_work_plan}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)




