from PageObjectLibrary import PageObject
from resources.web import PAGINATION, BUTTON, TEXTFIELD, DRPSINGLE
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class WarehouseListPage(PageObject):
    """ Functions in warehouse listing page """
    PAGE_TITLE = "Master Data Management / Warehouse"
    PAGE_URL = "/setting-ui/distributors/3CAF4BF6:8C7572E0-F133-4341-9B42-8C5D32CC6352/warehouse"
    WH_CODE = "${wh_cd}"
    WH_DESC = "${wh_desc}"

    _locators = {
        "PrincipalCol": "//th//child::*[text()='Principal']"
    }

    def click_add_warehouse_button(self):
        """ Function to click add for new warehouse """
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects warehouse to ${action}')
    def user_selects_warehouse_to(self, action):
        """ Function to select warehouse to edit/delete """
        wh_cd = BuiltIn().get_variable_value(self.WH_CODE)
        wh_desc = BuiltIn().get_variable_value(self.WH_DESC)
        col_list = ["WHS_CD", "WHS_DESC"]
        data_list = [wh_cd, wh_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Warehouse", action, col_list, data_list)

    @keyword('user filters warehouse using ${action} data')
    def user_filters_warehouse(self, action):
        """ Function to filter warehouse using filter fields """
        wh_cd = BuiltIn().get_variable_value(self.WH_CODE)
        wh_desc = BuiltIn().get_variable_value(self.WH_DESC)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Warehouse Code", wh_cd)
        TEXTFIELD.insert_into_filter_field("Warehouse Description", wh_desc)
        if action == 'Non-Prime' or action == 'Prime':
            wh_type = BuiltIn().get_variable_value("${wh_type}")
            DRPSINGLE.selects_from_single_selection_dropdown("Principal", wh_type)
        BUTTON.click_button("Apply")

    @keyword('user searches warehouse using ${action} data')
    def user_searches_warehouse(self, action):
        """ Function to search warehouse with inline search """
        wh_cd = BuiltIn().get_variable_value(self.WH_CODE)
        wh_desc = BuiltIn().get_variable_value(self.WH_DESC)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("Warehouse Code", wh_cd)
        TEXTFIELD.insert_into_search_field("Warehouse Description", wh_desc)
        BUTTON.click_icon("search")

    def record_display_in_listing_successfully(self):
        """ Function to validate warehouse showing in listing """
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "Filtering not working correctly"

    @keyword('user validates principal column ${status} in listing')
    def user_validates_principal_column_in_listing(self, status):
        """ Function to validate principal column showing in warehouse listing """
        if status == 'not visible':
            self.selib.page_should_not_contain_element(self.locator.PrincipalCol)
        else:
            self.selib.page_should_contain_element(self.locator.PrincipalCol)
