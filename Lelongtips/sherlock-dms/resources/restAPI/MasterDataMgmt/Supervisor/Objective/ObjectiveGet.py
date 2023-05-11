
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL

class ObjectiveGet(object):

    @keyword("user retrieves ${cond} supervisor objective")
    def user_retrieves_objective(self, cond):
        """ Function to retrieve all created objective """
        url = ""
        if cond == 'invalid':
            objective_id = Common().generate_random_id("0")
            url = "{0}supervisor-objective/{1}".format(END_POINT_URL,  objective_id)
        elif cond == 'all':
            url = "{0}supervisor-objective".format(END_POINT_URL)
        else:
            objective_id = BuiltIn().get_variable_value("${objective_id}")
            url = "{0}supervisor-objective/{1}".format(END_POINT_URL, objective_id)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("123", body_result)
            BuiltIn().set_test_variable("${rs_bd_objective}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)




