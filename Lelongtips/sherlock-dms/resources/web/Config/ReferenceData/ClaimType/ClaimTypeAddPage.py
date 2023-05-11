from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from resources.web import BUTTON,TEXTFIELD,DRPSINGLE,POPUPMSG
import secrets


class ClaimTypeAddPage(PageObject):

    PAGE_TITLE = "Configuration / Reference Data / Claim Type"
    PAGE_URL = "objects/claim-type"
    CLAIM_DETAILS = "${claim_details}"
    CLAIM_CODE = "${claim_code}"
    CLAIM_DESC = "${claim_desc}"
    _locators = {

    }

    @keyword('user creates claim type with ${data_type} data')
    def user_creates_claim_type_using(self, data_type):
        details = self.builtin.get_variable_value(self.CLAIM_DETAILS)
        if details is None and data_type != "empty":
            claim_code = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            claim_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
        else:
            claim_code = details['claim_code']
            claim_desc = details['claim_desc']
        if data_type =="deleted" or data_type=="existing":
            claim_code = BuiltIn().get_variable_value(self.CLAIM_CODE)
            claim_desc = BuiltIn().get_variable_value(self.CLAIM_DESC)
        BUTTON.click_button("Add")
        TEXTFIELD.insert_into_field("Claim Type Code", claim_code)
        TEXTFIELD.insert_into_field("Claim Type Description", claim_desc)
        if data_type != "empty":
            DRPSINGLE.selects_from_single_selection_dropdown("Promotion Type", "random")
        self.builtin.set_test_variable("${claim_code}", claim_code)
        self.builtin.set_test_variable("${claim_desc}", claim_desc)
        BUTTON.click_button("Save")

    @keyword('validate error message on empty fields')
    def validate_invalid_fields(self):
        TEXTFIELD.validate_validation_msg("Claim Type Code", "Please enter a value")
        TEXTFIELD.validate_validation_msg("Claim Type Description", "Please enter a value")
        DRPSINGLE.validate_validation_msg_for_dropdown("Promotion Type")

    @keyword('error message shown already exists')
    def error_message_claim_already_exists(self):
        claim_cd = BuiltIn().get_variable_value(self.CLAIM_CODE)
        msg= "Code for this Claim Type '"+claim_cd+"' already exists"
        POPUPMSG.validate_pop_up_msg(msg)
        POPUPMSG.click_button_on_pop_up_msg()