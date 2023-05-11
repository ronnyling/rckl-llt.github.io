from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE
import secrets


class AgeingTermsAddPage(PageObject):

    PAGE_TITLE = "Configuration / Reference Data / Ageing Terms"
    PAGE_URL = "objects/aging-term"
    TERM_DETAILS = "${term_details}"
    _locators = {

    }

    @keyword('user creates ageing terms with ${data_type} data')
    def user_creates_ageing_terms_using(self, data_type):
        details = self.builtin.get_variable_value(self.TERM_DETAILS)
        if details is None:
            start = secrets.choice(range(30, 100))
            end = start + 10
            desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
        else:
            start = details['start_day']
            end = details['end_day']
            desc = details['desc']
        BUTTON.click_button("Add")
        TEXTFIELD.insert_into_field("Ageing Starting Day", start)
        TEXTFIELD.insert_into_field("Ageing Ending Day", end)
        TEXTFIELD.insert_into_field("Ageing Description", desc)
        self.builtin.set_test_variable("${start_day}", start)
        self.builtin.set_test_variable("${end_day}", end)
        BUTTON.click_button("Save")

    @keyword('validate error message on empty fields')
    def validate_invalid_fields(self):
        TEXTFIELD.validate_validation_msg("Ageing Starting Day", "Please enter a value")
        TEXTFIELD.validate_validation_msg("Ageing Ending Day", "Please enter a value")
