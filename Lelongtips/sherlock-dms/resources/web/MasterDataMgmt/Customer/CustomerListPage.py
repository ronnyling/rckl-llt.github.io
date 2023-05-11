from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, COMMON_KEY, PAGINATION
from robot.api.deco import keyword
from selenium.common.exceptions import ElementNotInteractableException


class CustomerListPage(PageObject):
    PAGE_TITLE = "Master Data Management / Customer"
    PAGE_URL = "/customer?template=p"

    _locators = \
        {
            "ADD": "(//span[contains(text(),'Add')]/parent::button[1])",
            "SearchIcon": "(//button[@class='ant-btn ng-star-inserted ant-btn-icon-only'])[1]",
            "CustomerCodeSearch": "(//input[@type='text'])[1]",
            "POSMtab": "//div[contains(text(),'POSM')]",
        }

    timeout = "0.2 min"
    wait = "3 sec"

    def click_add_customer_button(self):
        self._wait_for_page_refresh()
        BUTTON.click_button("Add")
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")

    def click_search_icon(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.SearchIcon)

    def enter_customer_code(self, cust_cd):
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "input_text",
                                                 self.locator.CustomerCodeSearch, cust_cd)

    def click_shown_customer_code(self, cust_cd):
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                 "//a[contains(text(),'%s')]" % cust_cd)

    @keyword("user searches customer with code")
    def search_customer_with_code(self):
        cust = self.builtin.get_variable_value("&{CUSTOMER}")
        cust_cd = cust.get('CD')
        self._wait_for_page_refresh()
        self.click_search_icon()
        self.enter_customer_code(cust_cd)
        self.click_shown_customer_code(cust_cd)
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")

    @keyword("user go to POSM tab")
    def navigate_to_posm_tab(self):
        try:
            self.selib.click_element(self.locator.POSMtab)
        except ElementNotInteractableException:     # if the tab was not visible and needed scrolling
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     "//span[2]//span[1]//i[1]//*[local-name()='svg']")
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     self.locator.POSMtab)

    @keyword("user validates the POSM data")
    def validate_posm_product(self):
        cust = self.builtin.get_variable_value("&{CUSTOMER}")
        posm_cd = cust.get('POSMCD')
        self.selib.wait_until_element_is_visible("//*[text()='%s']" % posm_cd)

    @keyword('user selects customer to ${action}')
    def user_selects_customer_to(self, action):
        """ Function to select customer to edit/delete """
        cust_name = BuiltIn().get_variable_value("${cust_name}")
        cust_status = "Active"
        col_list = ["CUST_NAME", "STATUS"]
        data_list = [cust_name, cust_status]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Customer", action, col_list, data_list)
