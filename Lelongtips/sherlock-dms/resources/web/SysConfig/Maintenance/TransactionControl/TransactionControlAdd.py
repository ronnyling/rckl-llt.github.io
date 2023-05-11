from PageObjectLibrary import PageObject
from resources.web import BUTTON, DRPSINGLE


class TransactionControlAdd(PageObject):
    PAGE_TITLE = "System Configuration / Maintenance / Transaction Controll"
    PAGE_URL = "/configure-transaction-control"

    _locators = {
        "AddPageTitle": "//div[contains(text(),'Transaction Control Listing')]",

    }

    def click_add_configure_route_transaction_control_button(self):
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    def select_operation_type(self, operation_type):
        DRPSINGLE.selects_from_single_selection_dropdown("Operation Type", operation_type)

    def select_transaction_control(self, transaction_control):
        DRPSINGLE.selects_from_single_selection_dropdown("Transaction Control", transaction_control)

    def click_save_configure_route_transaction_control_button(self):
        BUTTON.click_button("Save")
        self._wait_for_page_refresh()

    def create_configure_route_transaction_control(self):
        details = self.builtin.get_variable_value("&{Details}")
        self.click_add_configure_route_transaction_control_button()
        self.selib.wait_until_element_is_visible(self.locator.AddPageTitle)
        self.select_operation_type(details['operationtype'])
        self.select_transaction_control(details['transactioncontrol'])
        self.click_save_configure_route_transaction_control_button()


