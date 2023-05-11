import secrets, json
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL
METADATA_END_POINT_URL = PROTOCOL + "metadata" + APP_URL

class WorkPlanGet(object):

    FILTER_BOTH = '"IN_STORE_ACTIVITY": {"$eq": true},"FEEDBACK_REQUIRED": {"$eq": true}'

    @keyword("user retrieves ${cond} supervisor work plan")
    def user_retrieves_work_plan(self, cond):
        """ Function to retrieve all created  work plan """
        url = ""
        if cond == 'invalid':
            work_plan_id = Common().generate_random_id("0")
            url = "{0}supervisor-work-plan-item/{1}".format(END_POINT_URL, work_plan_id)
        elif cond == 'all':
            url = "{0}supervisor-work-plan-item".format(END_POINT_URL)
        else:
            work_plan_id = BuiltIn().get_variable_value("${work_plan_id}")
            url = "{0}supervisor-work-plan-item/{1}".format(END_POINT_URL, work_plan_id)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${rs_bd_work_plan}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword("get random work plan by Field:${field} Value:${Value}")
    def get_random_work_plan_by_field_and_value(self, field, value):
        if field == "Both":
            filter_pg1 = '{"IN_STORE_ACTIVITY": {"$eq": '+str(value)+'},'
            filter_pg2 = '"FEEDBACK_REQUIRED": {"$eq": '+str(value)+'}}'
            filter_pg = filter_pg1+filter_pg2
        else :
            filter_pg = {field: {"$eq": value}}
            filter_pg = json.dumps(filter_pg)
        url = "{0}module-data/supervisor-work-plan-item?filter={1}".format(METADATA_END_POINT_URL, filter_pg)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve work plan"
        body_result = response.json()
        choice = secrets.choice(body_result)
        BuiltIn().set_test_variable("${rs_bd_work_plan}", choice)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return choice


