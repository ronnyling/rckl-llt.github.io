from robot.api.deco import keyword
from PageObjectLibrary import PageObject

from resources.web import BUTTON, LABEL
from resources.web.Config.ReferenceData.Bank import BankAddPage


class BankEditPage(PageObject):
    """ Functions related to Bank Edit """

    @keyword('user edits bank with ${data_type} data')
    def user_edits_bank_data(self, data_type):
        LABEL.validate_label_is_visible("EDIT | Bank")
        details = self.builtin.get_variable_value("${bank_details}")
        bank_cd = self.builtin.get_variable_value("${bank_cd}")
        bank_desc = BankAddPage.BankAddPage().user_inserts_bank_desc(data_type, details)
        self.builtin.set_test_variable("${updated_bank_cd}", bank_cd)
        self.builtin.set_test_variable("${updated_bank_desc}", bank_desc)
        BUTTON.click_button("Save")
