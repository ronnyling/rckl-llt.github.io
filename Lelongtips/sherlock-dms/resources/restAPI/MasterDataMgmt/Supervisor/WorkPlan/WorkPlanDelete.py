from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.Common import Common
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route import RoutePost
from resources.restAPI.MasterDataMgmt.RouteMgmt.RouteMapping import RouteGeoMapping
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL


class WorkPlanDelete(object):

    @keyword("user deletes ${cond} supervisor work plan")
    def user_deletes_work_plan(self, cond):
        """ Function to delete created  work plan """
        workplan_id = ""
        if cond == "predefined":
            workplan_id = self.search_predefined_data()
        elif cond == 'invalid':
            workplan_id = Common().generate_random_id("0")
        else:
            workplan_id = BuiltIn().get_variable_value("${work_plan_id}")

        url = "{0}supervisor-work-plan-item/{1}".format(END_POINT_URL, workplan_id)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("Delete", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)


    def search_predefined_data(self):
        work_plan_rs_body = BuiltIn().get_variable_value("${rs_bd_work_plan}")
        for item in work_plan_rs_body:
            print("yoyo", item)
            if item['CORE_FLAGS'] == "CX":
                work_plan_details = {
                    "ID":  item['ID']
                }
                BuiltIn().set_test_variable("${work_plan_details}", work_plan_details)
                BuiltIn().set_test_variable("${work_plan_id}", item['ID'])
                return item['ID']
