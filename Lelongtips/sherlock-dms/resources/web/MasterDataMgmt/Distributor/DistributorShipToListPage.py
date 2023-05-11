from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, PAGINATION


class DistributorShipToListPage(PageObject):

    PAGE_TITLE = "Master Data Management / Distributor"
    PAGE_URL = "/distributors?template=p"
    SHIPTO_DETAILS = "${shipto_details}"

    @keyword('user validates buttons for ship to listing page')
    def user_validates_buttons(self):
        BUTTON.validate_button_is_shown("Add")
        BUTTON.validate_icon_is_shown("delete")
        BUTTON.validate_icon_is_shown("search")
        BUTTON.validate_icon_is_shown("filter")

    @keyword('user backs to ship to listing page')
    def user_backs_to_listing_page(self):
        BUTTON.click_button("Cancel")

    @keyword('user selects ship to to ${action}')
    def user_selects_distributor_ship_to(self, action):
        shipto_code = BuiltIn().get_variable_value("${shipto_code}")
        col_list = ["SHIPTO_CD"]
        data_list = [shipto_code]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Ship To", action, col_list, data_list)
        if action == "delete":
            BUTTON.click_button("Yes")
