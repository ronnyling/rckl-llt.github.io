from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON,TEXTFIELD,LABEL
import secrets


class ClaimTypeEditPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Claim Type"
    PAGE_URL = "objects/claim-type"
    _locators = {
    }

    @keyword('user edits claim type with ${data_type} data')
    def user_edits_claim_type_using(self, data_type):
        claim_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
        TEXTFIELD.insert_into_field("Claim Type Description", claim_desc)
        self.builtin.set_test_variable("${claim_desc}", claim_desc)
        BUTTON.click_button("Save")

    @keyword('claim type viewed successfully')
    def claim_type_viewed_successfully(self):
        LABEL.validate_label_is_visible("EDIT | Claim Type")
        BUTTON.click_button("Cancel")



