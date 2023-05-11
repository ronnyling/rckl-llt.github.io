from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, LABEL
import secrets

class TaxGroupEditPage(PageObject):
    PAGE_TITLE = "Configuration / Tax Management / Tax Group"
    PAGE_URL = "/tax-group"
    NEW_TAX_DETAILS = "${new_tax_details}"
    _locators = {

    }

    @keyword('user edits tax group with ${data_type} data')
    def user_edits_tax_group_using(self, data_type):

        new_details = self.builtin.get_variable_value(self.NEW_TAX_DETAILS)
        if new_details is None:
            tax_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
        else:
            tax_desc = new_details['tax_desc']
        TEXTFIELD.insert_into_field("Tax Group Description", tax_desc)
        self.builtin.set_test_variable("${tax_desc}", tax_desc)
        BUTTON.click_button("Save")

    @keyword('tax group viewed successfully')
    def tax_group_viewed_successfully(self):
        LABEL.validate_label_is_visible("EDIT | Tax Group")
        BUTTON.click_button("Cancel")