from PageObjectLibrary import PageObject
from resources.web.MasterDataMgmt.RouteMgmt.Route import RouteListPage
from robot.api.deco import keyword
from resources.web.Common import POMLibrary
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE
from setup.yaml import YamlDataManipulator


class RouteAddPage(PageObject):
    """ Functions in Route add page """
    PAGE_TITLE = "Master Data Management / Route Management / Route"
    PAGE_URL = "/route?template=p"

    _locators = {
        "np_warehouse": "//*[text()='Non Prime Warehouse']"
    }

    @keyword('user creates route using ${data_type} data')
    def user_creates_route_using_data(self, data_type):
        """ Function to create route with random/given data """
        POMLibrary.POMLibrary().check_page_title("RouteListPage")
        route_details = self.builtin.get_variable_value("&{RouteDetails}")
        RouteListPage.RouteListPage().click_add_route_button()
        POMLibrary.POMLibrary().check_page_title("RouteAddPage")
        route_cd = self.user_inserts_route_code(route_details)
        route_name = self.user_inserts_route_name(route_details)
        route_op = self.user_selects_operation_type(route_details)
        warehouse = self.user_selects_main_warehouse(route_details)
        multi_status = self.builtin.get_variable_value("${multi_status}")
        user_role = self.builtin.get_variable_value("${user_role}")
        if multi_status is True:
            np_warehouse = self.user_selects_np_warehouse(route_details)
            self.builtin.set_test_variable("${np_warehouse}", np_warehouse)
        elif multi_status is False or user_role == 'hqadm':
            self.selib.page_should_not_contain_element(self.locator.np_warehouse)
        self.user_selects_lob("random", route_details)
        self.builtin.set_test_variable("${route_cd}", route_cd)
        self.builtin.set_test_variable("${route_name}", route_name)
        self.builtin.set_test_variable("${route_op}", route_op)
        self.builtin.set_test_variable("${warehouse}", warehouse)


    @keyword('user assigns geo value using ${data_type} data')
    def user_assign_geo_assignment(self, data_type):
        """ Function to assign geo with random/given data """
        geo_details = self.builtin.get_variable_value("&{GeoDetails}")
        geo_level = self.user_selects_geo_level(geo_details)
        geo_value = self.user_selects_geo_values(geo_details)
        self.builtin.set_test_variable("${geo_level}", geo_level)
        self.builtin.set_test_variable("${geo_value}", geo_value)
        BUTTON.click_button("Apply")
        BUTTON.click_button("Save")


    def user_inserts_route_code(self, route_details):
        """ Function to insert route code with random/given data """
        route_cd_given = self.builtin.get_variable_value("&{RouteDetails['routeCode']}")
        if route_cd_given is not None:
            route_cd = TEXTFIELD.insert_into_field("Route Code", route_cd_given)
        else:
            route_cd = TEXTFIELD.insert_into_field_with_length("Route Code", "random", 6)
        return route_cd

    def user_inserts_route_name(self, route_details):
        """ Function to insert route name with random/given data """
        route_name_given = self.builtin.get_variable_value("&{RouteDetails['routeName']}")
        if route_name_given is not None:
            route_name = TEXTFIELD.insert_into_field("Route Name", route_name_given)
        else:
            route_name = TEXTFIELD.insert_into_field_with_length("Route Name", "random", 6)
        return route_name

    def user_selects_operation_type(self, route_details):
        """ Function to select route operation type with random/given data """
        user_role = self.builtin.get_variable_value("${user_role}")
        route_op_given = self.builtin.get_variable_value("${RouteDetails['OP_TYPE']}")
        if route_op_given is not None:
            route_op = DRPSINGLE.selects_from_single_selection_dropdown("Operation Type", route_op_given)
        else:
            if user_role == 'hqadm':
                route_op = DRPSINGLE.selects_from_single_selection_dropdown("Operation Type", "random")
            else:
                route_op = DRPSINGLE.selects_from_single_selection_dropdown("Operation Type", "Pre-Sales")
        return route_op

    def user_selects_main_warehouse(self, route_details):
        """ Function to select warehouse in route with random/given data """
        route_op_given = self.builtin.get_variable_value("${RouteDetails['OP_TYPE']}")
        if route_op_given == 'HQ Telesales':
            wh = None
        else:
            wh_info = YamlDataManipulator.YamlDataManipulator().user_retrieves_data_from_yaml("1-RoutePre.yaml", "Output")
            wh = DRPSINGLE.selects_from_single_selection_dropdown("Main Warehouse", wh_info['1_WarehousePost']['WHS_DESC'])
        return wh

    def user_selects_np_warehouse(self, route_details):
        """ Function to select warehouse in route with random/given data """
        wh_info = YamlDataManipulator.YamlDataManipulator().user_retrieves_data_from_yaml("1-RoutePre.yaml",
                                                                                          "Output")
        np_wh = DRPSINGLE.selects_from_single_selection_dropdown("Non Prime Warehouse", wh_info['2_WarehousePost']['WHS_DESC'])
        return np_wh

    def user_selects_lob(self, type, route_details):
        """ Function to select lob in route with random/given data """
        DRPSINGLE.selects_from_single_selection_dropdown("LOB", type)

    def user_selects_geo_level(self, geo_details):
        """"Function to select the geo level"""
        geo_level_given = self.builtin.get_variable_value("&{RouteDetails['geoLevel']}")
        if geo_level_given is not None:
            geo_level = DRPSINGLE.select_from_single_selection_dropdown("Geo Level", geo_details['geoLevel'])
        else:
            geo_level = DRPSINGLE.select_from_single_selection_dropdown("Geo Level", "random")
        return geo_level

    def user_selects_geo_values(self, geo_details):
        """"Function to select the geo value"""
        geo_lvalue_given = self.builtin.get_variable_value("&{RouteDetails['geoValue']}")
        if geo_lvalue_given is not None:
            geo_values = DRPSINGLE.select_from_single_selection_dropdown("Geo Value", geo_details['geoValue'])
        else:
            geo_values = DRPSINGLE.select_from_single_selection_dropdown("Geo Value", "random")
        return geo_values
