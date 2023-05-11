from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import PAGINATION, BUTTON
from robot.libraries.BuiltIn import BuiltIn


class InvoiceTermListPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Invoice Terms"
    PAGE_URL = "setting-ui/distributors/3CAF4BF6:8C7572E0-F133-4341-9B42-8C5D32CC6352/setting-invoice-term"

    _locators = {
    }

    @keyword('user selects invoice term to ${action}')
    def user_selects_invoice_term_to(self, action):
        inv_code = BuiltIn().get_variable_value("${invterm_cd}")
        inv_desc = BuiltIn().get_variable_value("${invterm_desc}")
        col_list = ["TERMS", "TERMS_DESC"]
        data_list = [inv_code, inv_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Setting Invoice Term", action, col_list, data_list)

    def click_add_invoice_term_button(self):
        BUTTON.click_button("Add")
