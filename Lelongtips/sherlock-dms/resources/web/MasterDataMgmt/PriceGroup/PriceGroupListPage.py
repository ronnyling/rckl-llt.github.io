from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, PAGINATION


class PriceGroupListPage(PageObject):

    PAGE_TITLE = "Master Data Management / Price Group"
    PAGE_URL = "/pricegrouplisting"
    PG_DETAILS = "${pg_details}"

    @keyword('user validates buttons for price group listing page')
    def user_validates_buttons(self):
        BUTTON.validate_button_is_shown("Add")
        BUTTON.validate_icon_is_shown("delete")
        BUTTON.validate_icon_is_shown("search")
        BUTTON.validate_icon_is_shown("filter")

    @keyword('user backs to price group listing page')
    def user_backs_to_listing_page(self):
        BUTTON.click_button("Cancel")

    @keyword('user selects price group to ${action}')
    def user_selects_price_group_to(self, action):
        pg_code = BuiltIn().get_variable_value("${pg_code}")
        col_list = ["PRICE_GRP_CD"]
        data_list = [pg_code]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Price Group", action, col_list, data_list)
        if action == "delete":
            BUTTON.click_button("Yes")
