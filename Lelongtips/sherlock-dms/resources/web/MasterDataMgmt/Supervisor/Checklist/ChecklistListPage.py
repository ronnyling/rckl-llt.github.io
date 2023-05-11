from PageObjectLibrary import PageObject
from resources.web import TEXTFIELD, BUTTON, PAGINATION
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class ChecklistListPage(PageObject):

    PAGE_TITLE = "Master Data Management / Supervisor / Checklist"
    PAGE_URL = "/objects/module-data/supervisor-objective"
    CHECKLIST_DETAILS = "${checklist_details}"
    CHECKLIST_CD = "${checklist_code}"
    CHECKLIST_DESC = "${checklist_desc}"
    _locators = {

    }

    @keyword('user searches created checklist in listing page')
    def user_search_created_dashboard(self):
        details = BuiltIn().get_variable_value(self.CHECKLIST_DETAILS)
        if details is None:
            checklist_code = BuiltIn().get_variable_value(self.CHECKLIST_CD)
        else:
            checklist_code = details['checklist_code']
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_filter_field("Checklist Code", checklist_code)

    @keyword('user filters created checklist in listing page')
    def user_filters_created_dashboard(self):
        details = BuiltIn().get_variable_value(self.CHECKLIST_DETAILS)
        if details is None:
            checklist_code = BuiltIn().get_variable_value(self.CHECKLIST_CD)
            checklist_desc = BuiltIn().get_variable_value(self.CHECKLIST_DESC)
        else:
            checklist_code = details['checklist_code']
            checklist_desc = details['checklist_desc']
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Checklist Code", checklist_code)
        TEXTFIELD.insert_into_filter_field("Checklist Description", checklist_desc)
        BUTTON.click_button("Apply")

    @keyword('user validate created checklist is listed in the table and select to ${action}')
    def user_selects_checklist_to(self, action):
        details = BuiltIn().get_variable_value(self.CHECKLIST_DETAILS)
        if details is None:
            checklist_code = BuiltIn().get_variable_value(self.CHECKLIST_CD)
            checklist_desc = BuiltIn().get_variable_value(self.CHECKLIST_DESC)

        else :
            checklist_code = details['checklist_code']
            checklist_desc = details['checklist_desc']
        col_list = ["CHECKLIST_CD", "CHECKLIST_DESC"]
        data_list = [checklist_code, checklist_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Checklist", action, col_list, data_list)


    @keyword("checklist unable to be deleted")
    def validate_unable_to_delete(self):
        BUTTON.check_icon_is_disabled("delete")

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No checklist in listing"

