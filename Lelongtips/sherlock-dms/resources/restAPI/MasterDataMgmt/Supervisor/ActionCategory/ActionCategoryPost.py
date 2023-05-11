import json, secrets
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL


class ActionCategoryPost(object):

    @keyword("user creates supervisor action category with ${cond} data")
    def user_creates_action_category_with_data(self, cond):
        """ Function to create action category """
        payload = self.action_category_payload()
        url = "{0}supervisor-action-category".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("testing", body_result)
            BuiltIn().set_test_variable("${action_category_id}", body_result['ID'])
            BuiltIn().set_test_variable("${action_category_cd}", body_result['ACTION_CAT_CODE'])
            BuiltIn().set_test_variable("${rs_bd_action_category}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)


    def action_category_payload(self):
        payload = {
            "ACTION_CAT_CODE": 'AC' + str(secrets.choice(range(1, 9999999))),
            "ACTION_CAT_DESC": 'AC DESC' + str(secrets.choice(range(1, 9999999))),
        }
        action_category_details = BuiltIn().get_variable_value("${action_category_details}")
        if action_category_details:
            payload.update((k, v) for k, v in action_category_details.items())
        payload = json.dumps(payload)
        print("print payload", payload)
        return payload
