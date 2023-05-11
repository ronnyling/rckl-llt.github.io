from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, PAGINATION, TEXTFIELD, COMMON_KEY


class ChecklistResultListPage(PageObject):

    PAGE_TITLE = "Merchandising / Activity Setup / Checklist Result"
    PAGE_URL = "/merchandising/checklist-result"
    CHECKLIST_DETAILS = "${checklist_details}"

    _locators = {
        "No_Search" : "(//input[@type='text'])[1]",
        "Cust_Search": "(//input[@type='text'])[4]",
        "Route_Search": "(//input[@type='text'])[6]",
        "Distributor_Search": "(//input[@type='text'])[2]",
    }

    @keyword('user filters checklist result by ${field}')
    def user_filters_checklist_result(self, field):
        details = BuiltIn().get_variable_value(self.CHECKLIST_DETAILS)
        item = details['filter_item']
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field(field, item)
        BUTTON.click_button("Apply")

    @keyword('user searches checklist result by ${field}')
    def user_searches_checklist_result(self, field):
        details = BuiltIn().get_variable_value(self.CHECKLIST_DETAILS)
        item = details['search_item']
        BUTTON.click_icon("search")
        if field == "Transaction No.":
            locator = self.locator.No_Search
        elif field == "Distributor":
            locator = self.locator.Distributor_Search
        elif field == "Customer":
            locator = self.locator.Customer_Search
        else :
            locator = self.locator.Route_Search
        COMMON_KEY.wait_keyword_success("input_text", locator, item)

    @keyword('user selects checklist result to ${action}')
    def user_selects_checklist_result_to(self, action):
        details = BuiltIn().get_variable_value(self.CHECKLIST_DETAILS)
        transaction_no = details['txn_no']
        col_list = ["TXN_NO"]
        data_list = [transaction_no]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Checklist Result", action, col_list, data_list)

    def user_is_able_to_view_the_result_successfully(self):
        PAGINATION.validates_table_column_visibility("Checklist Code", "displaying")
        PAGINATION.validates_table_column_visibility("Checklist Description", "displaying")
        PAGINATION.validates_table_column_visibility("Activity Code","displaying")
        PAGINATION.validates_table_column_visibility("Activity Description","displaying")



