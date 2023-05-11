from robot.api.deco import keyword
from PageObjectLibrary import PageObject

from resources.web import BUTTON, TEXTFIELD
from resources.web.Config.ReferenceData.Bank import BankListPage


class BankAddPage(PageObject):
    """ Functions related to bank Create """
    PAGE_TITLE = "Configuration / Reference Data / Bank"
    PAGE_URL = "/objects/bank"

    _locators = {
    }

    @keyword('user creates bank with ${data_type} data')
    def user_creates_bank(self, data_type):
        details = self.builtin.get_variable_value("${bank_details}")
        BankListPage.BankListPage().click_add_bank_button()
        bank_cd = self.user_inserts_bank_cd(data_type, details)
        bank_desc = self.user_inserts_bank_desc(data_type, details)
        self.builtin.set_test_variable("${bank_cd}", bank_cd)
        self.builtin.set_test_variable("${bank_desc}", bank_desc)
        BUTTON.click_button("Save")

    @staticmethod
    def user_inserts_bank_cd(data_type, details):
        bank_cd = ""
        if data_type == "fixed":
            bank_cd = TEXTFIELD.insert_into_field("Bank Code", details['bank_cd'])
        elif data_type == "random":
            bank_cd = TEXTFIELD.insert_into_field_with_length("Bank Code", "letter", 8)
        return bank_cd

    @staticmethod
    def user_inserts_bank_desc(data_type, details):
        bank_desc = ""
        if data_type == "fixed":
            bank_desc = TEXTFIELD.insert_into_field("Bank Description", details['bank_desc'])
        elif data_type == "random":
            bank_desc = TEXTFIELD.insert_into_field_with_length("Bank Description", "random", 8)
        return bank_desc







