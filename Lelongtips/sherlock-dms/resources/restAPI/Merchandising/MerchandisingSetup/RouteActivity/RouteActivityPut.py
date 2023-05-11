import secrets, json
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
import datetime

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL
current_date = datetime.datetime.now()


class RouteActivityPut(object):

    @keyword('user updates route activity with ${type} data')
    def user_updates_route_activity_with(self, type):
        res_bd_route_activity_id = BuiltIn().get_variable_value("${res_bd_route_activity_id}")
        url = "{0}merchandising/merc-route-activity/{1}".format(END_POINT_URL, res_bd_route_activity_id)
        payload = self.payload_setup(type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${res_bd}", body_result)
            BuiltIn().set_test_variable("${res_bd_route_activity_id}", body_result["ID"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_setup(self, type):
        activity_code = BuiltIn().get_variable_value("${res_bd_route_activity_cd}")
        activity_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(15))
        start_date = str((current_date + datetime.timedelta(days=3)).strftime("%Y-%m-%d"))
        end_date = str((current_date + datetime.timedelta(days=4)).strftime("%Y-%m-%d"))

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
