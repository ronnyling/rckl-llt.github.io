import random

from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web.MasterDataMgmt.Customer import CustomerAddPage
from resources.web import BUTTON, COMMON_KEY, PAGINATION, TEXTFIELD, TOGGLE
from robot.api.deco import keyword
from selenium.common.exceptions import ElementNotInteractableException


class CustomerShipToPage(PageObject):
    PAGE_TITLE = "Master Data Management / Customer"
    PAGE_URL = "/customer?template=p"

    _locators = \
        {
            "ADD": "(//span[contains(text(),'Add')]/parent::button[1])",
            "SearchIcon": "(//button[@class='ant-btn ng-star-inserted ant-btn-icon-only'])[1]",
            "CustomerCodeSearch": "(//input[@type='text'])[1]",
            "ShipToTab": "//div[contains(text(),'Ship To Address')]",
        }

    timeout = "0.2 min"
    wait = "3 sec"

    @keyword("user go to Ship To Address tab")
    def navigate_to_ship_to_tab(self):
        try:
            self.selib.click_element(self.locator.ShipToTab)
        except ElementNotInteractableException:  # if the tab was not visible and needed scrolling
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     "//span[2]//span[1]//i[1]//*[local-name()='svg']")
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     self.locator.ShipToTab)

    @keyword("user creates a new ship to address")
    def create_ship_to_address(self):
        BUTTON.click_button("Add")
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")
        ship_to_code = TEXTFIELD.insert_into_field_with_length("Ship To Code", "random", 12)
        ship_to_desc = TEXTFIELD.insert_into_field_with_length("Ship To Description", "random", 12)
        TOGGLE.switch_toggle("Default Ship To", random)
        CustomerAddPage.CustomerAddPage().user_inserts_customer_address("1", None)
        CustomerAddPage.CustomerAddPage().user_inserts_customer_address("2", None)
        CustomerAddPage.CustomerAddPage().user_inserts_customer_address("3", None)
        CustomerAddPage.CustomerAddPage().user_inserts_customer_postal(None)
        CustomerAddPage.CustomerAddPage().user_selects_cust_locality(None)
        CustomerAddPage.CustomerAddPage().user_selects_cust_state(None)
        CustomerAddPage.CustomerAddPage().user_selects_cust_country(None)
        BuiltIn().set_test_variable("${ship_to_code}", ship_to_code)
        BuiltIn().set_test_variable("${ship_to_desc}", ship_to_desc)
        BUTTON.click_button("Save")

    @keyword('user selects ship to address to ${action}')
    def user_selects_ship_to(self, action):
        """ Function to select ship to address to edit/delete """
        ship_to_code = BuiltIn().get_variable_value("${ship_to_code}")
        ship_to_desc = BuiltIn().get_variable_value("${ship_to_desc}")
        col_list = ["SHIPTO_CD", "SHIPTO_DESC"]
        data_list = [ship_to_code, ship_to_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Ship To Address", action, col_list, data_list)
        if action == 'delete':
            BUTTON.click_button("Yes")

    @keyword("user updates ship to address with ${data_type} data")
    def update_ship_to_address(self, data_type):
        ship_to_details = self.builtin.get_variable_value("&{SHIP_TO_UPDATE}")
        Desc = ship_to_details['Desc']
        if data_type == 'fixed':
            ship_to_desc = TEXTFIELD.insert_into_field_with_length("Ship To Description", Desc, 30)
            CustomerAddPage.CustomerAddPage().user_inserts_customer_address("1", ship_to_details)
            CustomerAddPage.CustomerAddPage().user_inserts_customer_address("2", ship_to_details)
            CustomerAddPage.CustomerAddPage().user_inserts_customer_address("3", ship_to_details)
            CustomerAddPage.CustomerAddPage().user_inserts_customer_postal(ship_to_details)
        elif data_type == 'random':
            ship_to_desc = TEXTFIELD.insert_into_field_with_length("Ship To Description", "random", 12)
            CustomerAddPage.CustomerAddPage().user_inserts_customer_address("1", None)
            CustomerAddPage.CustomerAddPage().user_inserts_customer_address("2", None)
            CustomerAddPage.CustomerAddPage().user_inserts_customer_address("3", None)
            CustomerAddPage.CustomerAddPage().user_inserts_customer_postal(None)
        BuiltIn().set_test_variable("${ship_to_desc}", ship_to_desc)
        BUTTON.click_button("Save")

