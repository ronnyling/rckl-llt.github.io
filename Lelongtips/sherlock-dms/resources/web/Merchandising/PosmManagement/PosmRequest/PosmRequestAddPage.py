from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE, COMMON_KEY, CALENDAR
import secrets


class PosmRequestAddPage(PageObject):

    PAGE_TITLE = "Merchandising / POSM Management / POSM Request"
    PAGE_URL = "/merchandising/posm-request"
    PR_DETAILS = "${pr_details}"

    _locators = {
        "req_qty_field": "(//*[contains(text(),'Request Quantity')]/following::input)[2]",
        "customer_field": "//input[@placeholder='Select']"
    }

    @keyword('user creates posm request using ${data_type} data')
    def user_creates_posm_request(self, data_type):
        details = self.builtin.get_variable_value(self.PR_DETAILS)
        BUTTON.click_button("Add New Request")
        if data_type == "fixed":
            req_type = details['REQUEST_TYPE']
            cust = details['CUSTOMER']
            posm_cat = details['POSM_CATEGORY']
            reason = details['REASON']
            posm_code = details['POSM_CODE']
            req_qty = details['REQUEST_QTY']

        DRPSINGLE.select_from_single_selection_dropdown("Request Type", req_type)
        self.select_customer(cust)
        DRPSINGLE.select_from_single_selection_dropdown("POSM Category", posm_cat)
        DRPSINGLE.select_from_single_selection_dropdown("Reason", reason)
        self.select_product(posm_code)
        COMMON_KEY.wait_keyword_success("input_text", self.locator.req_qty_field, req_qty)
        BUTTON.click_button("Save")

    def select_customer(self, cust):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.customer_field)
        self.selib.input_text(self.locator.customer_field, cust)
        COMMON_KEY.wait_keyword_success("click_element", "//*[text()='%s']" % cust)

    def select_product(self, prod):
        TEXTFIELD.insert_into_field("POSM Code", prod)
        COMMON_KEY.wait_keyword_success("click_element", "//*[text()='%s']" % prod)
