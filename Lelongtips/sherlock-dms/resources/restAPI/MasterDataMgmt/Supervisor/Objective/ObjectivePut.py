import json
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL


class ObjectivePut(object):

    @keyword("user updates ${cond} supervisor objective")
    def user_updates_supervisor_objective(self, cond):
        """ Function to retrieve all  Objective """
        if cond == 'invalid':
            objective_id = Common().generate_random_id("0")
        else:
            objective_id = BuiltIn().get_variable_value("${objective_id}")
        url = "{0}supervisor-objective/{1}".format(END_POINT_URL, objective_id)
        payload = self.update_objective_payload(cond)
        print("payload = ", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${rs_bd_objective}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def update_objective_payload(self, cond):
        objective_id = BuiltIn().get_variable_value("${objective_id}")
        payload_objective = BuiltIn().get_variable_value("${payload_objective}")
        if cond != 'invalid':
            payload_objective['ID'] = objective_id
        objective_details = BuiltIn().get_variable_value("${objective_details}")
        if objective_details:
            payload_objective.update((k, v) for k, v in objective_details.items())
        payload_objective = json.dumps(payload_objective)
        return payload_objective



