from PageObjectLibrary import PageObject
from resources.web import PAGINATION, BUTTON
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class VanReplenishmentListPage(PageObject):
    PAGE_TITLE = "Van Inventory / Van Replenishment"
    PAGE_URL = "/inventory/van-stock-replenish"

    _locators = {
    }

    def click_add_van_replenishment_button(self):
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects created van replenishment to ${action}')
    def user_selects_created_van_replenishment_to(self, action):
        """ Function to select van replenishment to edit/delete """
        route_cd = BuiltIn().get_variable_value("${route}")
        warehouse = BuiltIn().get_variable_value("${warehouse}")

        col_list = ["ROUTE_CD", "WAREHOUSE"]
        data_list = [route_cd, warehouse]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Customer", action, col_list, data_list)
