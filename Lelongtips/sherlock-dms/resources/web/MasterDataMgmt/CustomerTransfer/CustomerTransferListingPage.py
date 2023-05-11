from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources import Common
from resources.web import BUTTON, PAGINATION, TEXTFIELD
from robot.api.deco import keyword


class CustomerTransferListingPage(PageObject):

    _locators = {
        "search_icon": "//core-button[@ng-reflect-icon='search']",
        "sort_no": "(//div[@class='cell-render auto-increment ng-star-inserted'])[1]"
    }

    @keyword('user selects customer transfer to ${action}')
    def user_selects_ship_to(self, action):
        cust_transfer = BuiltIn().get_variable_value("${CustTransferDetails}")
        dist_to = BuiltIn().get_variable_value("${dist_to}")
        dist_from = BuiltIn().get_variable_value("${dist_from}")
        Common().wait_keyword_success("click_element", self.locator.search_icon)
        TEXTFIELD.insert_into_search_field("From Distributor", dist_from)
        TEXTFIELD.insert_into_search_field("To Distributor", dist_to)
        Common().wait_keyword_success("click_element", self.locator.sort_no)
        Common().wait_keyword_success("click_element", self.locator.sort_no)

        col_list = ["FROM_DIST_NAME", "TO_DIST_NAME"]
        data_list = [cust_transfer["DistFrom"], cust_transfer["DistTo"]]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Customer Transfer", action, col_list, data_list)
        if action == 'check':
            BUTTON.click_button("Cancel")