from resources.restAPI import PROTOCOL, APP_URL
import json

from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.RouteMgmt.SalesPerson import SalesPersonPost
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class SalesPersonPut(object):

    @keyword("user updates ${data_type} salesperson info")
    def user_updates_route_salesperson_info(self, data_type):
        salesperson_id = BuiltIn().get_variable_value("${res_bd_salesperson_id}")
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/route-salesperson/{2}".format(END_POINT_URL, dist_id, salesperson_id)
        payload = SalesPersonPost.SalesPersonPost().payload_route_salesperson_info(data_type)
        new_payload = {"ID": salesperson_id}
        dist_payload = {
            "DIST_ID":{
                "ID": dist_id
            }
        }
        payload.update(new_payload)
        payload.update(dist_payload)
        details = BuiltIn().get_variable_value("${update_salesperson_details}")
        payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        common = APIMethod.APIMethod()
        print("FINAL PAYLOAD," ,payload)
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code != 200:
            BuiltIn().set_test_variable("${status_code}", response.status_code)
            return str(response.status_code), ""
        else:
            body_result = response.json()
            BuiltIn().set_test_variable("${status_code}", response.status_code)
            print(body_result)
