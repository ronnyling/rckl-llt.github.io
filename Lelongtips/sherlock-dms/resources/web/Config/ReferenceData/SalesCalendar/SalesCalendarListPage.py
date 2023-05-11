from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, TEXTFIELD, PAGINATION


class SalesCalendarListPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Sales Calendar"
    PAGE_URL = "/sales-calendar"

    _locators = {

    }

    def click_add_sales_calendar_button(self):
        """ Function to click add button for new sales calendar """
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    def user_deletes_created_sales_calendar(self):
        """ Function to click delete icon in the listing page """
        BUTTON.click_inline_delete_icon("1")

    @keyword('user searches created sales calendar in listing page')
    def inline_search_created_calendar(self):
        """ Function to search sales calendar with inline search"""
        BUTTON.click_icon("search")
        calendar_name = BuiltIn().get_variable_value("${calendar_name}")
        TEXTFIELD.insert_into_search_field("CALENDAR NAME", calendar_name)
        BUTTON.click_icon("search")

    def record_display_in_listing_successfully(self):
        """ Function to validate sales calendar showing in listing """
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "Sales Calendar not displayed in listing"

    def user_clicks_created_sales_calendar(self):
        """ Function to click on the created sales calendar for edit """
        BUTTON.click_hyperlink(1)
