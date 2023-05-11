from PageObjectLibrary import PageObject
from resources.web.Config.ReferenceData.InvoiceTerm import InvoiceTermListPage
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE


class InvoiceTermAddPage (PageObject):
    """ Functions related to add page of SalesInvoice Term """
    PAGE_TITLE = "Configuration / Reference Data / Invoice Terms"
    PAGE_URL = "setting-ui/distributors/3CAF4BF6:8C7572E0-F133-4341-9B42-8C5D32CC6352/setting-invoice-term"


    @keyword('user creates invoice term with ${data_type} data')
    def user_creates_invoice_term_with_data(self, data_type):
        """ Function to create invoice term with random/fixed data """
        invterm_details = self.builtin.get_variable_value("&{invterm_details}")
        InvoiceTermListPage.InvoiceTermListPage().click_add_invoice_term_button()
        self.user_inserts_invterm_cd(data_type, invterm_details)
        self.user_inserts_invterm_desc(data_type, invterm_details)
        self.user_inserts_invterm_days(data_type, invterm_details)
        BUTTON.click_button("Save")

    def user_inserts_invterm_cd(self, data_type, invterm_details):
        if data_type == "fixed":
            invterm_cd = TEXTFIELD.insert_into_field("Terms", invterm_details['invterm_cd'])
        else:
            invterm_cd = TEXTFIELD.insert_into_field_with_length("Terms", "letter", 8)
        self.builtin.set_test_variable("${invterm_cd}", invterm_cd)
        return invterm_cd

    def user_inserts_invterm_desc(self, data_type, invterm_details):
        if data_type == "fixed":
            invterm_desc = TEXTFIELD.insert_into_field("Terms Description", invterm_details['invterm_desc'])
        else:
            invterm_desc = TEXTFIELD.insert_into_field_with_length("Terms Description", "random", 8)
        self.builtin.set_test_variable("${invterm_desc}", invterm_desc)
        return invterm_desc

    def user_inserts_invterm_days(self, data_type, invterm_details):
        if data_type == "fixed":
            invterm_days = TEXTFIELD.insert_into_field("Terms Days", invterm_details['invterm_days'])
        else:
            invterm_days = TEXTFIELD.insert_into_field_with_length("Terms Days", "number", 2)
        self.builtin.set_test_variable("${invterm_days}", invterm_days)
        return invterm_days

    def user_choose_state(self, data_type,state_name):
        if data_type == "fixed":
            if state_name:
                state_name = DRPSINGLE.selects_from_single_selection_dropdown("State", state_name)
        elif data_type == "random":
            state_name = DRPSINGLE.selects_from_single_selection_dropdown("State", "random")
        return state_name

