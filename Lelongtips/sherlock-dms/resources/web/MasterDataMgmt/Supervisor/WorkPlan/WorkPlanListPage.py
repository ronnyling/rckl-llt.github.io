from PageObjectLibrary import PageObject
from resources.web import TEXTFIELD, TOGGLE, BUTTON, PAGINATION
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class WorkPlanListPage(PageObject):
    """ Functions in work plan listing page """
    PAGE_TITLE = "Master Data Management / Supervisor / Work Plan Item"
    PAGE_URL = "/objects/module-data/supervisor-work-plan-item"
    WP_CODE = "${WP_CODE}"
    WP_DESC = "${WP_DESC}"

    _locators = {

    }
    @keyword("user lands on work plan add mode")
    def click_add_work_plan_button(self):
        """ Function to click add for new work plan """
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects work plan to ${action}')
    def user_selects_work_plan_to(self, action):
        """ Function to selects work plan to edit/delete """
        wp_cd = BuiltIn().get_variable_value(self.WP_CODE)
        wp_desc = BuiltIn().get_variable_value(self.WP_DESC)
        col_list = ["WORK_PLAN_ITEM_CODE", "WORK_PLAN_ITEM_DESC"]
        data_list = [wp_cd, wp_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Work Plan", action, col_list, data_list)

    @keyword('user filters work plan using ${action} data')
    def user_filters_work_plan(self, action):
        """ Function to filter work plan using filter fields """
        wp_cd = BuiltIn().get_variable_value(self.WP_CODE)
        wp_desc = BuiltIn().get_variable_value(self.WP_DESC)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Work Plan Item Code", wp_cd)
        TEXTFIELD.insert_into_filter_field("Work Plan Item Description", wp_desc)
        BUTTON.click_button("Apply")

    @keyword('user searches work plan using ${action} data')
    def user_searches_work_plan(self, action):
        """ Function to search work plan with inline search """
        wp_cd = BuiltIn().get_variable_value(self.WP_CODE)
        wp_desc = BuiltIn().get_variable_value(self.WP_DESC)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("Work Plan Item Code", wp_cd)
        TEXTFIELD.insert_into_search_field("Work Plan Item Description", wp_desc)
        BUTTON.click_icon("search")

    def work_plan_record_display_in_listing_successfully(self):
        """ Function to validate work plan showing in listing """
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "Filtering not working correctly"
