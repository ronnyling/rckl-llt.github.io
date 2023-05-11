from PageObjectLibrary import PageObject
from resources.web import BUTTON, TEXTFIELD, PAGINATION
from robot.libraries.BuiltIn import BuiltIn


class SummaryListPage(PageObject):
    """ Functions in Customer add page """
    PAGE_TITLE = "Telesales / Summary"
    PAGE_URL = "/customer-transactions-ui/telesales-summary"
    SUMMARY_DETAILS = "${summary_details}"

    _locators = {
        "load_image": "//div[@class='loading-text']//img"
    }

    def user_searches_summary_in_listing(self):
        details = BuiltIn().get_variable_value("${summary_details}")
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("Customer Code", details['CUST_CD'])
        TEXTFIELD.insert_into_search_field("Customer Name", details['CUST_NAME'])

    def user_filters_summary_in_listing(self):
        details = BuiltIn().get_variable_value("${summary_details}")
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Customer Code", details['CUST_CD'])
        TEXTFIELD.insert_into_filter_field("Customer Name", details['CUST_NAME'])
        BUTTON.click_button("Apply")

    def validate_the_column_display_for_summary(self):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        PAGINATION.validates_table_column_visibility("Order No.", "displaying")
        PAGINATION.validates_table_column_visibility("Order Date", "displaying")
        PAGINATION.validates_table_column_visibility("Customer Code", "displaying")
        PAGINATION.validates_table_column_visibility("Customer Name", "displaying")
        PAGINATION.validates_table_column_visibility("Route Name", "displaying")
        PAGINATION.validates_table_column_visibility("Delivery Date", "displaying")
        PAGINATION.validates_table_column_visibility("Order Amount ($)", "displaying")
        PAGINATION.validates_table_column_visibility("Status", "displaying")

    def record_display_in_listing_successfully(self):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No Telesales order summary in listing"
