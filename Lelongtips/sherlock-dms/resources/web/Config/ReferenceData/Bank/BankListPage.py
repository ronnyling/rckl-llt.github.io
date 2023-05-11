from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.web import PAGINATION, BUTTON
from PageObjectLibrary import PageObject


class BankListPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Bank"
    PAGE_URL = "/objects/bank"
    UPDATED_BANK_CD = "${updated_bank_cd}"
    _locators = {
    }

    @keyword('user selects bank to ${action}')
    def user_selects_bank_to(self, action):
        updated = BuiltIn().get_variable_value(self.UPDATED_BANK_CD)
        if updated:
            bank_code = BuiltIn().get_variable_value(self.UPDATED_BANK_CD)
            bank_desc = BuiltIn().get_variable_value("${updated_bank_desc}")
        else:
            bank_code = BuiltIn().get_variable_value("${bank_cd}")
            bank_desc = BuiltIn().get_variable_value("${bank_desc}")
        col_list = ["CODE", "BANK_DESC"]
        data_list = [bank_code, bank_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Bank", action, col_list, data_list)

    def user_clicks_cancel(self):
        self.builtin.set_test_variable("${updated_bank_cd}", self.builtin.set_test_variable("${bank_cd}"))
        self.builtin.set_test_variable("${updated_bank_desc}", self.builtin.set_test_variable("${bank_desc}"))
        BUTTON.click_button("Cancel")

    def click_add_bank_button(self):
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()
