from PageObjectLibrary import PageObject
from resources.web import TEXTFIELD, BUTTON, PAGINATION
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class ObjectiveListPage(PageObject):
    """ Functions in objective listing page """
    PAGE_TITLE = "Master Data Management / Supervisor / Objective"
    PAGE_URL = "/objects/module-data/supervisor-objective"
    OBJ_CODE = "${OBJ_CODE}"
    OBJ_DESC = "${OBJ_DESC}"

    _locators = {

    }
    @keyword("user lands on objective add mode")
    def click_add_objective_button(self):
        """ Function to click add for new objective """
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects objective to ${action}')
    def user_selects_objective_to(self, action):
        """ Function to selects objective to edit/delete """
        obj_cd = BuiltIn().get_variable_value(self.OBJ_CODE)
        obj_desc = BuiltIn().get_variable_value(self.OBJ_DESC)
        col_list = ["OBJECTIVE_CD", "OBJECTIVE_DESC"]
        data_list = [obj_cd, obj_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Objective", action, col_list, data_list)

    @keyword('user filters objective using ${action} data')
    def user_filters_objective(self, action):
        """ Function to filter objective using filter fields """
        obj_cd = BuiltIn().get_variable_value(self.OBJ_CODE)
        obj_desc = BuiltIn().get_variable_value(self.OBJ_DESC)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Objective Code", obj_cd)
        TEXTFIELD.insert_into_filter_field("Objective Description", obj_desc)
        BUTTON.click_button("Apply")

    @keyword('user searches objective using ${action} data')
    def user_searches_objective(self, action):
        """ Function to search objective with inline search """
        obj_cd = BuiltIn().get_variable_value(self.OBJ_CODE)
        obj_desc = BuiltIn().get_variable_value(self.OBJ_DESC)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("Objective Code", obj_cd)
        TEXTFIELD.insert_into_search_field("Objective Description", obj_desc)
        BUTTON.click_icon("search")

    def objective_record_display_in_listing_successfully(self):
        """ Function to validate objective showing in listing """
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "Filtering not working correctly"
