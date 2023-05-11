from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, LABEL
import secrets

class TaxDefinitionEditPage(PageObject):
    PAGE_TITLE = "Configuration / Tax Management / Tax Definition"
    PAGE_URL = "/tax-group"
    NEW_TAX_DETAILS = "${new_tax_details}"
    _locators = {

    }

    @keyword('user edits tax definition with ${data_type} data')
    def user_edits_tax_definition_using(self, data_type):
        self.tax_code_disabled_during_edit()
        new_details = self.builtin.get_variable_value(self.NEW_TAX_DETAILS)
        if new_details is None:
            tax_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
        else:
            tax_desc = new_details['tax_desc']
        TEXTFIELD.insert_into_field("Tax Component Description", tax_desc)
        self.builtin.set_test_variable("${tax_desc}", tax_desc)
        BUTTON.click_button("Save")

    def tax_code_disabled_during_edit(self):
        status = TEXTFIELD.return_disable_state_of_field("Tax Code")
        assert status is True or status == 'true', "Tax Code not disabled"

    @keyword('tax definition viewed successfully')
    def tax_definition_viewed_successfully(self):
        LABEL.validate_label_is_visible("EDIT | Tax Definition")
        BUTTON.click_button("Cancel")