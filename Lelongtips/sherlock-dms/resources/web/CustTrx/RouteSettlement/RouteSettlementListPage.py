from PageObjectLibrary import PageObject
from resources.web.CustTrx.Collection.CollectionListPage import CollectionListPage
from robot.libraries.BuiltIn import BuiltIn
from resources.web import DRPSINGLE, FILEUPLOAD, TEXTFIELD, BUTTON, COMMON_KEY, LABEL, POPUPMSG, CALENDAR, PAGINATION
from robot.api.deco import keyword
import datetime
import re
import secrets


class RouteSettlementListPage(PageObject):
    PAGE_TITLE = "Customer Transaction / Route Settlement"
    PAGE_URL = "/customer-transactions-ui/routesettlement"
    ROUTE_SETTLEMENT_DETAILS="${RouteSettlementDetails}"

    @keyword('user selects route settlement to ${action}')
    def user_selects_route_settlement_to(self, action):
        details = BuiltIn().get_variable_value(self.ROUTE_SETTLEMENT_DETAILS)
        if details :
            route_settlement_no = details["route_settlement_no"]
        else:
            route_settlement_no = BuiltIn().get_variable_value("${route_settlement_no}")
        col_list = ["TXN_NO"]
        data_list = [route_settlement_no]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Route Settlement", action, col_list, data_list)

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No matching route settlement in listing"

    def validate_user_is_redirected_to_route_settlement_details(self):
        LABEL.validate_label_is_visible("VIEW")

    def validate_user_is_redirected_to_listing_page(self):
        LABEL.validate_label_is_visible("Route Settlement Listing")

    def user_filters_the_route_settlement(self):
        details = BuiltIn().get_variable_value(self.ROUTE_SETTLEMENT_DETAILS)
        if details:
            route_settlement_no = details["route_settlement_no"]
            route_code = details["route_code"]
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Route Settlement No.", route_settlement_no)
        TEXTFIELD.insert_into_filter_field("Route Code", route_code)
        BUTTON.click_button("Apply")

    def user_searches_the_route_settlement(self):
        details = BuiltIn().get_variable_value(self.ROUTE_SETTLEMENT_DETAILS)
        if details:
            route_settlement_no = details["route_settlement_no"]
            route_code = details["route_code"]
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("Route Settlement No.", route_settlement_no)
        TEXTFIELD.insert_into_search_field("Route Code", route_code)