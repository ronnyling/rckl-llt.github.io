from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, PAGINATION, TAB, TEXTFIELD, LABEL, COMMON_KEY


class AuditResultListPage(PageObject):

    PAGE_TITLE = "Merchandising / Activity Setup / Audit Result"
    PAGE_URL = "/merchandising/audit-result"
    AUDIT_DETAILS = "${audit_details}"

    _locators = {
        "Cust_Search" : "(//input[@type='text'])[4]"
    }

    @keyword('And user selects ${audit_type} tab')
    def user_selects_tab(self, audit_type):
        TAB.user_navigate_to_tab(audit_type)

    @keyword('user filters ${audit_type} result')
    def user_filters_audit_result(self, audit_type):
        details = BuiltIn().get_variable_value(self.AUDIT_DETAILS)
        cust_name = details['CUSTOMER_NAME']
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Customer Name", cust_name)
        BUTTON.click_button("Apply")

    @keyword('user searches ${audit_type} result')
    def user_searches_audit_result(self, audit_type):
        details = BuiltIn().get_variable_value(self.AUDIT_DETAILS)
        cust_name = details['CUSTOMER_NAME']
        BUTTON.click_icon("search")
        COMMON_KEY.wait_keyword_success("input_text", self.locator.Cust_Search, cust_name)

    @keyword('user selects result to ${action}')
    def user_selects_audit_result_to(self, action):
        details = BuiltIn().get_variable_value(self.AUDIT_DETAILS)
        transaction_no = details['TRANSACTION_NO']
        col_list = ["TXN_NO"]
        data_list = [transaction_no]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Audit Result", action, col_list, data_list)

    def user_is_able_to_view_the_result_successfully(self):
        PAGINATION.validates_table_column_visibility("Store Space","displaying")
        PAGINATION.validates_table_column_visibility("Category","displaying")

    def user_is_able_to_view_the_compliance_successfully(self):
        results = PAGINATION.return_number_of_cards_in_a_page()
        assert results >= 1, "No planogram compliance result"


