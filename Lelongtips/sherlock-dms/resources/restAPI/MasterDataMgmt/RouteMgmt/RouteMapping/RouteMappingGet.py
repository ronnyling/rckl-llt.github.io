import secrets
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.Common import Common
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route import RoutePost
from resources.restAPI.MasterDataMgmt.RouteMgmt.RouteMapping import RouteGeoMapping
from resources.restAPI.SysConfig.TenantMaintainance.FeatureSetup.FeatureSetupPut import FeatureSetupPut
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL


class RouteMappingGet(object):
    """ Functions to retrieve route record """
    ROUTE_ID = "${res_bd_route_id}"

    @keyword("user retrieves ${cond} route mapping data")
    def user_retrieves_all_route_mapping_data(self, cond):
        """ Function to retrieve all  available  route record """
        route_id = BuiltIn().get_variable_value(self.ROUTE_ID)
        if cond == 'invalid':
            route_id = Common().generate_random_id("0")
        url = "{0}supervisor-route-mapping/routes/{1}".format(END_POINT_URL, route_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${random_ava_route}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    @keyword("user retrieves mapped route data")
    def user_retrieves_mapped_route_data(self):
        """ Function to retrieve route which mapped with supervisor route """
        route_id = BuiltIn().get_variable_value(self.ROUTE_ID)
        url = "{0}supervisor-route-mapping/routes/{1}/mapped".format(END_POINT_URL, route_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("mapped route data = ", body_result)
        BuiltIn().set_test_variable(Common.STATUS_CODE, response.status_code)

    def randomize_available_route(self):
        self.user_retrieves_all_route_mapping_data('random')
        ava_route = BuiltIn().get_variable_value("${random_ava_route}")
        route_choice = secrets.choice(ava_route)
        BuiltIn().set_test_variable("${route_mapping_route_id}", route_choice['ID'])

    def user_creates_prerequisite_for_route_mapping(self):
        """ Function to create pre-requisite for route """
        FeatureSetupPut().user_set_feature_setup_on_or_off("", "on", "SUPERVISOR")
        RoutePost.RoutePost().user_creates_prerequisite_for_route()
        Common().execute_prerequisite('1-RouteMappingPre.yaml')
        status_code = BuiltIn().get_variable_value(Common.STATUS_CODE)
        if str(status_code) == "201":
            RouteGeoMapping.RouteGeoMapping().user_map_route_to_geo_tree("route", "Area", "Dungun")


