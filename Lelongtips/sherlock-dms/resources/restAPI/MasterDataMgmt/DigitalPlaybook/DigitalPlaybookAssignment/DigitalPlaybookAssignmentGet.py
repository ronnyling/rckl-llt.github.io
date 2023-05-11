from resources.restAPI import PROTOCOL, APP_URL, Common
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "message" + APP_URL


class DigitalPlaybookAssignmentGet(object):
    """ Functions to retrieve playbook assignment"""

    @keyword("user retrieves ${cond} digital playbook assignment")
    def user_retrieves_digital_playbook_assignment(self, cond):
        playbook_id = BuiltIn().get_variable_value("${playbook_id}")
        if cond == "all":
            url = "{0}playbk-setup/{1}/assignment".format(END_POINT_URL, playbook_id)
        elif cond == "invalid":
            assignment_id = Common().generate_random_id()
            url = "{0}playbk-setup/{1}/assignment/".format(END_POINT_URL, assignment_id)
        else:
            assignment_id = BuiltIn().get_variable_value("${plybk_assignment_id}")
            url = "{0}playbk-setup/{1}/assignment/{2}".format(END_POINT_URL, playbook_id, assignment_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
