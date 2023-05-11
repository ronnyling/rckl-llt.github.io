from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import TokenAccess, APIMethod, APIAssertion
from setup.yaml import YamlDataManipulator
from resources.restAPI.MasterDataMgmt.Warehouse import WarehouseDelete

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class RouteDelete(object):
    """ Functions to delete route record """

    def user_deletes_route_with_created_data(self):
        """ Function to delete route using given id """
        res_bd_route_id = BuiltIn().get_variable_value("${res_bd_route_id}")
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/route/{2}".format(END_POINT_URL, distributor_id, res_bd_route_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_deletes_warehouse_created(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        no_record = YamlDataManipulator.YamlDataManipulator().user_retrieves_data_from_yaml("1-RoutePre.yaml", 'Output')
        for data in no_record.values():
            BuiltIn().set_test_variable("${res_bd_warehouse_id}", data['ID'])
            WarehouseDelete.WarehouseDelete().user_deletes_warehouse_with_data("created")
            APIAssertion.APIAssertion().expected_return_either_status_code_or_status_code("200", "404")

    def user_deletes_prerequisite_for_route(self):
        """ Function to delete pre-requisite for route record """
        self.user_deletes_warehouse_created()
