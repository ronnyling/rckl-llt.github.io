from PageObjectLibrary import PageObject
from resources.web import BUTTON, RADIOBTN
from robot.api.deco import keyword
from selenium.common.exceptions import ElementNotInteractableException


class CustomerOptionsPage(PageObject):
    PAGE_TITLE = "Master Data Management / Customer"
    PAGE_URL = "/customer?template=p"

    _locators = \
        {
            "ADD": "(//span[contains(text(),'Add')]/parent::button[1])",
            "SearchIcon": "(//button[@class='ant-btn ng-star-inserted ant-btn-icon-only'])[1]",
            "OptionsTab": "//div[contains(text(),'Options')]",
        }

    timeout = "0.2 min"
    wait = "3 sec"

    @keyword("user go to Options tab")
    def navigate_to_options_page(self):
        try:
            self.selib.click_element(self.locator.OptionsTab)
        except ElementNotInteractableException:  # if the tab was not visible and needed scrolling
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     "//span[2]//span[1]//i[1]//*[local-name()='svg']")
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     self.locator.OptionsTab)

    @keyword("user updates customer options with ${data_type} data")
    def update_customer_options(self, data_type):
        if data_type == 'random':
            RADIOBTN.select_from_radio_button("Back Order Allowed", "random")
            RADIOBTN.select_from_radio_button("Partial Fulfilment Allowed", "random")
            RADIOBTN.select_from_radio_button("Over Due Checking", "random")
            RADIOBTN.select_from_radio_button("Customer Purchased Order Mandatory", "random")
            RADIOBTN.select_from_radio_button("Credit Limit Checking", "random")
        elif data_type == 'fixed':
            cust_option = self.builtin.get_variable_value("&{CUSTOMER_OPTIONS}")
            RADIOBTN.select_from_radio_button("Back Order Allowed", cust_option["BackOrder"])
            RADIOBTN.select_from_radio_button("Partial Fulfilment Allowed", cust_option["PartialFulfilment"])
            RADIOBTN.select_from_radio_button("Over Due Checking", cust_option["OverDue"])
            RADIOBTN.select_from_radio_button("Customer Purchased Order Mandatory", cust_option["Mandatory"])
            RADIOBTN.select_from_radio_button("Credit Limit Checking", cust_option["CreditCheck"])
        BUTTON.click_button("Save")

    @keyword("user validates options page info")
    def validate_options_page(self):
        self.selib.wait_until_element_is_visible("//div[@class='ant-card-head-title ng-star-inserted'][contains(text(),'Options')]")
        self.selib.wait_until_element_is_visible("//*[contains(text(),'Back Order')]")
        self.selib.wait_until_element_is_visible("//*[contains(text(),'Partial Fulfilment')]")
        self.selib.wait_until_element_is_visible("//*[contains(text(),'Customer Purchased Order Mandatory')]")
        self.selib.wait_until_element_is_visible("//*[contains(text(),'Credit Limit Checking')]")
        self.selib.wait_until_element_is_visible("//*[contains(text(),'Exclude Batch Code Expiry Checking')]")
        self.selib.wait_until_element_is_visible("//*[contains(text(),'Delivery Date Lead Time Checking')]")
        self.selib.wait_until_element_is_visible("//*[contains(text(),'Delivery Date Lead Time in Day')]")
        self.selib.wait_until_element_is_visible("//*[contains(text(),'Exclude Batch Code Expiry in Month')]")