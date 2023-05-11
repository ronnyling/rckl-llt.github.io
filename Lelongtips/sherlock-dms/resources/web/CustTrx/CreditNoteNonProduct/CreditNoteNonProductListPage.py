""" Python file related to credit note non product UI """
from PageObjectLibrary import PageObject
from resources.web import BUTTON, PAGINATION
from robot.api.deco import keyword


class CreditNoteNonProductListPage(PageObject):
    """ Functions in credit note non product listing page """
    PAGE_TITLE = "Customer Transaction / Credit Note (Non Product)"
    PAGE_URL = "customer-transactions-ui/creditnote-non-product-listing"

    _locators = {
    }

    def click_add_credit_note_non_product_button(self):
        """ Function to add new credit note non product """
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects credit note non product to ${action}')
    def user_selects_credit_note_non_product_to(self, action):
        cn_cust_name = self.builtin.get_variable_value("${cn_np_cust}")
        cn_np_route_cd = self.builtin.get_variable_value("${cn_np_route_cd}")
        col_list = ["CUST_NAME", "ROUTE_CD"]
        data_list = [cn_cust_name, cn_np_route_cd]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Credit Note (Non Product)", action, col_list, data_list)

    def confirm_credit_note(self):
        BUTTON.click_button("Confirm CN")
        BUTTON.click_pop_up_screen_button("Yes")
