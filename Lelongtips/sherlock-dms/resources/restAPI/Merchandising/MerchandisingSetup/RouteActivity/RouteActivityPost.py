import secrets, json
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
import datetime

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL
current_date = datetime.datetime.now()


class RouteActivityPost(object):

    @keyword('user creates route activity with ${type} data')
    def user_creates_route_activity_with(self, type):
        url = "{0}merchandising/merc-route-activity".format(END_POINT_URL)
        payload = self.payload_setup(type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${res_bd}", body_result)
            BuiltIn().set_test_variable("${res_bd_route_activity_id}", body_result["ID"])
            BuiltIn().set_test_variable("${res_bd_route_activity_cd}", body_result["ACTIVITY_CODE"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_setup(self, type):
        activity_code = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(8))
        activity_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(15))
        start_date = str((current_date + datetime.timedelta(days=2)).strftime("%Y-%m-%d"))
        end_date = str((current_date + datetime.timedelta(days=3)).strftime("%Y-%m-%d"))

        payload = {
            "ACTIVITY_CODE": activity_code,
            "ACTIVITY_DESC": activity_desc,
            "START_DT": start_date,
            "END_DT": end_date
        }
        details = BuiltIn().get_variable_value("${activity_details}")
        if type == 'fixed' and details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Route Activity Payload: ", payload)
        return payload
