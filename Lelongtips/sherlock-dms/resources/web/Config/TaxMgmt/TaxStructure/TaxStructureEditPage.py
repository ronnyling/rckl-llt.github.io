from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, LABEL, CALENDAR
import secrets

class TaxStructureEditPage(PageObject):
    PAGE_TITLE = "Configuration / Tax Management / Tax Structure"
    PAGE_URL = "/taxstructure"
    NEW_TAX_DETAILS = "${new_tax_details}"
    _locators = {
    }

    @keyword('user edits tax structure with ${data_type} data')
    def user_edits_tax_structure_using(self, data_type):
        new_details = self.builtin.get_variable_value(self.NEW_TAX_DETAILS)
        if new_details is None:
            tax_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
        else:
            tax_desc = new_details['tax_desc']
        TEXTFIELD.insert_into_field("Tax Structure Description", tax_desc)
        CALENDAR.selects_date_from_calendar_str("Effective To", "next day")
        self.builtin.set_test_variable("${tax_desc}", tax_desc)
        BUTTON.click_button("Save")

    @keyword('tax structure viewed successfully')
    def tax_structure_viewed_successfully(self):
        LABEL.validate_label_is_visible("EDIT | Tax Structure")
        BUTTON.click_button("Cancel")