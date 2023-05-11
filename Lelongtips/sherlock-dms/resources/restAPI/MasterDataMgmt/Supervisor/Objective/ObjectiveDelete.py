from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL

class ObjectiveDelete(object):

    @keyword("user deletes ${cond} supervisor objective")
    def user_deletes_objective(self, cond):
        """ Function to delete created objective """
        objective_id = ""
        if cond == "predefined":
            objective_id = self.search_predefined_data()
        elif cond == 'invalid':
            objective_id = Common().generate_random_id("0")
        else:
            objective_id = BuiltIn().get_variable_value("${objective_id}")

        url = "{0}supervisor-objective/{1}".format(END_POINT_URL, objective_id)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("Delete", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

