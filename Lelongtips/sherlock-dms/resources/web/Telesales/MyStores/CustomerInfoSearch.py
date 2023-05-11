from PageObjectLibrary import PageObject
from resources.web import PAGINATION, BUTTON, TEXTFIELD
from robot.api.deco import keyword


class CustomerInfoSearch(PageObject):
    """ Functions in route listing page """
    PAGE_TITLE = "Telesales / My Stores"
    PAGE_URL = "customer-transactions-ui/telesales-my-store"

    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "info_icon": "//viewBox[@class='anticon anticon-info-circle']/parent::div[@class='anticon anticon-info-circle']"
    }

    @keyword('user searches customer using ${data}')
    def user_searches_customer(self, data):
        details = self.builtin.get_variable_value("&{cust_details}")
        cst_name = details['CUST_NAME']
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("CUST_NAME", cst_name)

    @keyword('user selects customer code hyperlink to ${action}')
    def user_selects_customer_code_hyperlink_to(self, action):
        details = self.builtin.get_variable_value("&{cust_details}")
        cst_name = details['CUST_NAME']
        col_list = ["CUST_NAME"]
        data_list = [cst_name]
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "My Stores", action,
                                                                   col_list, data_list)

    @keyword('validate customer details are displayed successfully')
    def validate_customer_details_are_displayed(self):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        details = self.builtin.get_variable_value("&{cust_details}")
        cst_name = details['CUST_NAME']
        cst_cd = details['CUST_CD']
        dist_name = details['DIST_NAME']
        dist_cd = details['DIST_CD']
        self.selib.wait_until_element_is_visible("//*[text()='%s']" % cst_name)
        self.selib.wait_until_element_is_visible("//*[text()='%s']" % cst_cd)
        self.selib.wait_until_element_is_visible("//*[text()='%s']" % dist_name)
        self.selib.wait_until_element_is_visible("//*[text()='%s']" % dist_cd)





