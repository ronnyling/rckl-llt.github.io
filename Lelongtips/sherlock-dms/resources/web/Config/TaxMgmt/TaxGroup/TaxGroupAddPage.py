from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE
import secrets

class TaxGroupAddPage(PageObject):
    PAGE_TITLE = "Configuration / Tax Management / Tax Group"
    PAGE_URL = "/tax-group"
    TAX_DETAILS = "${tax_details}"
    _locators = {

    }

    @keyword('user creates tax group with ${data_type} data')
    def user_creates_tax_group_using(self, data_type):
        details = self.builtin.get_variable_value(self.TAX_DETAILS)
        if details is None:
            tax_code = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
            tax_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
        else:
            tax_code = details['tax_code']
            tax_desc = details['tax_desc']
        BUTTON.click_button("Add")
        TEXTFIELD.insert_into_field("Tax Group Code", tax_code)
        TEXTFIELD.insert_into_field("Tax Group Description", tax_desc)
        DRPSINGLE.selects_from_single_selection_dropdown("Type", "random")
        self.builtin.set_test_variable("${tax_code}", tax_code)
        self.builtin.set_test_variable("${tax_desc}", tax_desc)
        BUTTON.click_button("Save")

    @keyword('validate error message on empty fields')
    def validate_invalid_fields(self):
        TEXTFIELD.validate_validation_msg("Tax Group Code", "Please enter a value")
        TEXTFIELD.validate_validation_msg("Tax Group Description", "Please enter a value")
        DRPSINGLE.validate_validation_msg_for_dropdown("Type")
