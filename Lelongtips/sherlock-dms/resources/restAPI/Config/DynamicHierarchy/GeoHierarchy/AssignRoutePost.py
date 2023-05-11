from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
import json
import datetime

END_POINT_URL = PROTOCOL + "dynamic-hierarchy" + APP_URL
node_id = 'B3EA05F1:15A2D068-A36D-4A7B-AFAD-76D7CF92719F'
    # geo hierarchy automation is not done yet, so using hard coded for now


class AssignRoutePost(object):
    """ Function to assign route/salesperson to geo tree """

    def user_assign_route_to_geotree(self):
        """ Function to assign route to geo tree """
        url = "{0}assign-route/assigned/{1}".format(END_POINT_URL, node_id)
        payload = self.payload_assign_route()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_assign_route(self):
        """ Function for geo tree assignment payload content """
        start_dt = datetime.datetime.today() + datetime.timedelta(days=1)
        end_dt = datetime.datetime.today() + datetime.timedelta(days=36)
        route_id = BuiltIn().get_variable_value("${res_bd_route_id}")
        payload = {
            "START_DATE": start_dt.strftime("%Y-%m-%d"),
            "END_DATE": end_dt.strftime("%Y-%m-%d"),
            "SELECTED_IDS": [
                route_id,
            ]
        }
        payload = json.dumps(payload)
        print("Assigned Route Payload: ", payload)
        return payload
