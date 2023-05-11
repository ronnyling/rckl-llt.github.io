from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, PAGINATION, TEXTFIELD
from robot.libraries.BuiltIn import BuiltIn


class SalesPersonListPage(PageObject):
    PAGE_TITLE = "Master Data Management / Route Management / Salesperson"
    PAGE_URL = "distributors/3CAF4BF6:8C7572E0-F133-4341-9B42-8C5D32CC6352/route-salesperson?template=p"

    _locators = {

    }

    @keyword('user selects salesperson to ${action}')
    def user_selects_salesperson_to(self, action):
        """ Function to select salesperson in listing to edit/delete """
        salesperson_cd = BuiltIn().get_variable_value("${salesperson_cd}")
        salesperson_name = BuiltIn().get_variable_value("${salesperson_name}")
        col_list = ["SALESPERSON_CODE", "SALESPERSON_NAME"]
        data_list = [salesperson_cd, salesperson_name]
        if action == 'delete':
            action = "check"
        PAGINATION.validate_the_data_is_in_the_table_and_select_to \
            ("present", "Sales Person", action, col_list, data_list)
        if action == 'check':
            BUTTON.click_icon("delete")

    @keyword('user searches created salesperson in listing page')
    def inline_search_created_salesperson(self):
        """ Function to search salesperson with inline search"""
        BUTTON.click_icon("search")
        salesperson_name = BuiltIn().get_variable_value("${salesperson_name}")
        TEXTFIELD.insert_into_search_field("Salesperson Name", salesperson_name)
        BUTTON.click_icon("search")

    def record_display_in_listing_successfully(self):
        """ Function to validate salesperson showing in listing """
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "Sales Person not displayed in listing"