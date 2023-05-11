from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import secrets

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ChecklistGet(object):

    @keyword('user retrieves all checklist')
    def user_retrieves_all_checklist(self):
        url = "{0}merchandising-checklist".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable("${checklist_res_bd}", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves checklist by id')
    def user_retrieves_checklist_by_id(self):
        checklist_id = BuiltIn().get_variable_value("${rand_checklist_id}")
        url = "{0}merchandising-checklist/{1}".format(END_POINT_URL, checklist_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${checklist_details}", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user randoms a checklist from list')
    def get_random_checklist_id(self):
        self.user_retrieves_all_checklist()
        cl_res_bd = BuiltIn().get_variable_value("${checklist_res_bd}")
        if len(cl_res_bd) > 1:
            rand_so = secrets.randbelow(len(cl_res_bd))
        else:
            rand_so = 0
        BuiltIn().set_test_variable("${rand_checklist_id}", cl_res_bd[rand_so]["ID"])
