import json
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from setup.hanaDB import HanaDB
from resources.restAPI.MasterDataMgmt.RouteMgmt.RouteMapping import RouteMappingGet
from robot.libraries.BuiltIn import BuiltIn
from resources.Common import Common
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL


class RouteMappingPost(object):
    """ Functions to retrieve route record """

    @keyword("user maps ${cond} route to supervisor route")
    def user_maps_route_to_supervisor_route(self, cond):
        """ Function to retrieve all  available  route record """
        route_id = BuiltIn().get_variable_value("${res_bd_route_id}")
        payload = self.route_mapping_payload(cond)
        url = "{0}supervisor-route-mapping/routes/{1}".format(END_POINT_URL, route_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("bod_res",body_result)
            BuiltIn().set_test_variable("${route_mapping_id_post}", body_result[0]['ID'])
            print("Total number of records retrieved are ", len(body_result))
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().user_validates_database_data("supervisor-route-mapping", body_result[0])
            # HanaDB.HanaDB().disconnect_from_database()
            BuiltIn().set_test_variable("${body_result}", body_result)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    def route_mapping_payload(self, cond):
        if cond == 'random':
            RouteMappingGet.RouteMappingGet().randomize_available_route()
            route_id = BuiltIn().get_variable_value("${route_mapping_route_id}")
        else:
            route_id = Common().generate_random_id("0")
        payload = [
            {
            "ROUTE_ID": route_id
            }
        ]
        payload = json.dumps(payload)
        return payload

