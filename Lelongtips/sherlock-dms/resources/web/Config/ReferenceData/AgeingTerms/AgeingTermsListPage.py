from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON,TEXTFIELD,PAGINATION
from robot.libraries.BuiltIn import BuiltIn

class AgeingTermsListPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Ageing Terms"
    PAGE_URL = "objects/aging-term"
    TERM_DETAILS = "${term_details}"
    START_DAY = "${start_day}"
    END_DAY = "${end_day}"
    _locators = {
    }

    @keyword('user selects ageing terms to ${action}')
    def user_selects_ageing_terms_to(self, action):
        details = self.builtin.get_variable_value(self.TERM_DETAILS)
        if details is None:
            start = str(BuiltIn().get_variable_value(self.START_DAY))
            end = str(BuiltIn().get_variable_value(self.END_DAY))
        else:
            start = details['start_day']
            end = details['end_day']
        col_list = ["AGING_START", "AGING_END"]
        data_list = [start, end]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Ageing Term", action, col_list, data_list)

    @keyword('user searches created ageing terms')
    def user_searches_ageing_terms(self):
        start = BuiltIn().get_variable_value(self.START_DAY)
        end = BuiltIn().get_variable_value(self.END_DAY)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("Ageing Starting Day", start)
        TEXTFIELD.insert_into_search_field("Ageing Ending Day", end)

    @keyword('user filters created ageing terms')
    def user_filters_ageing_terms(self):
        start = BuiltIn().get_variable_value(self.START_DAY)
        end = BuiltIn().get_variable_value(self.END_DAY)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Ageing Starting Day", start)
        TEXTFIELD.insert_into_filter_field("Ageing Ending Day", end)
        BUTTON.click_button("Apply")

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No matching ageing term in listing"
