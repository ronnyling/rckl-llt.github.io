from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import  BUTTON, COMMON_KEY, TEXTFIELD, PAGINATION
from robot.libraries.BuiltIn import BuiltIn

import secrets


class OutletNoteListPage(PageObject):
    """ Functions in Customer add page """
    PAGE_TITLE = "Outlet Note"
    PAGE_URL = "/customer?template=p"
    NOTE_DETAILS = "${note_details}"

    _locators = {
        "spoke_search":"//core-textfield[@ng-reflect-name='CUST_CONTACT_NAME']//input",
        "notes_search": "//core-textfield[@ng-reflect-name='NOTES']//input",
        "spoke_filter": "(//input[1][@type='text'])[6]",
        "notes_filter": "(//input[1][@type='text'])[8]",
        "cancel": "//div/div/div[3]/button"
    }


    def user_filters_outlet_note_in_listing(self):
        details = BuiltIn().get_variable_value("${note_details}")
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Spoke To", details['spokeTo'])
        TEXTFIELD.insert_into_filter_field("Outlet Note Detail", details['note'])
        BUTTON.click_button("Apply")

    def validate_the_column_display_for_outlet_note(self):
        PAGINATION.validates_table_column_visibility("Route", "displaying")
        PAGINATION.validates_table_column_visibility("Spoke To", "displaying")
        PAGINATION.validates_table_column_visibility("Date", "displaying")
        PAGINATION.validates_table_column_visibility("Time", "displaying")
        PAGINATION.validates_table_column_visibility("Outlet Note Detail", "displaying")

    def user_searches_outlet_note_in_listing(self):
        details = BuiltIn().get_variable_value("${note_details}")
        BUTTON.click_icon("search")
        COMMON_KEY.wait_keyword_success("input_text", self.locator.spoke_search, details['spokeTo'])
        COMMON_KEY.wait_keyword_success("input_text", self.locator.notes_search, details['note'])

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No outlet note in listing"

    @keyword('user selects outlet note to view')
    def user_selects_outlet_note_to_view(self):
        BUTTON.click_icon("right")

    def user_clicks_cancel_button(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.cancel)

    def validate_able_to_cancel_the_outlet_note_selection(self):
        self.user_clicks_cancel_button()
        self.validate_the_column_display_for_outlet_note()