from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON,TEXTFIELD
import secrets


class AgeingTermsEditPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Ageing Terms"
    PAGE_URL = "objects/aging-term"
    TERM_DETAILS = "${edit_term_details}"
    START_DAY = "${start_day}"
    END_DAY = "${end_day}"
    _locators = {
    }

    @keyword('user edits ageing terms with ${data_type} data')
    def user_edits_ageing_terms_using(self, data_type):
        details = self.builtin.get_variable_value(self.TERM_DETAILS)
        if details is None:
            desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
        else:
            desc = details['desc']
        TEXTFIELD.insert_into_field("Ageing Description", desc)
        BUTTON.click_button("Save")


