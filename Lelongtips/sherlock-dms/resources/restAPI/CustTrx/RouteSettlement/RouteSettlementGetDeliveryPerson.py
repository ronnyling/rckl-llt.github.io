from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from resources.Common import Common
import json
import secrets

from resources.restAPI.MasterDataMgmt.RouteMgmt.Route.RouteGet import RouteGet

END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class RouteSettlementGetDeliveryPerson:

    keyword('user retrieves all route settlement delivery person')
    def user_retrieves_all_routesettlement_deliveryperson(self):
        url = "{0}route-settlement-delivery-person".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

        BuiltIn().set_test_variable("${route_settlement_dp_list}", response.json())
        return str(response.status_code), response.json()

    def user_retrieves_random_route_settlement_delivery_person_details_by_id(self):
        self.user_retrieves_all_routesettlement_deliveryperson()
        rs_dp_list = BuiltIn().get_variable_value("${route_settlement_dp_list}")

        rand_int = secrets.choice(rs_dp_list)
        rand_rs_dp_id = rand_int['ID']
        url = "{0}route-settlement-delivery-person/{1}".format(END_POINT_URL, rand_rs_dp_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        BuiltIn().set_test_variable("${rand_rs_dp_id}", rand_rs_dp_id)
        BuiltIn().set_test_variable("${rs_dp_list}", rs_dp_list)
        return str(response.status_code), response.json()

    def user_retrieves_transactions_for_route_settlement_delivery_person(self):
        self.user_retrieves_random_route_settlement_delivery_person_details_by_id()
        all_rs_confirmed_ls = BuiltIn().get_variable_value("${rs_dp_list}")

        all_rs_confirmed = (
            rs for rs in all_rs_confirmed_ls
            if rs['STATUS'] == "C"
        )
        rand_rsdp = next(all_rs_confirmed, None)
        rand_rsdp_id = rand_rsdp['ID']

        tabs = {"main", "/settlement", "/collection", "/invoice", "/return", "/unassigned-return"}
        common = APIMethod.APIMethod()
        status_success = True
        failed_tabs = {}
        for tab in tabs:
            extension = ""
            if tab != "main":
                extension = tab
            url = "{0}route-settlement-delivery-person/{1}{2}".format(END_POINT_URL, rand_rsdp_id, extension)
            response = common.trigger_api_request("GET", url, "")
            if response.status_code == 200 or response.status_code == 204:
                continue
            else:
                status_success = False
                failed_tabs.update(tab)
        assert status_success, "Failed to retrieve details for " + failed_tabs.items()
        BuiltIn().set_test_variable("${status_code}", 200)



