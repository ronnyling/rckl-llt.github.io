from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL


class ChecklistDelete(object):

    @keyword('user deletes merchandising checklist')
    def user_deletes_merchandising_checklist(self):
        cl_id = BuiltIn().get_variable_value('${checklist_id}')
        url = "{0}merchandising-checklist/{1}".format(END_POINT_URL, cl_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
