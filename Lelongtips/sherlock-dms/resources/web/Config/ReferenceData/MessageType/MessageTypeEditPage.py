from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON,TEXTFIELD
import secrets


class MessageTypeEditPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Message Type"
    PAGE_URL = "/objects/message-type"
    MESSAGE_TYPE_DETAILS = "${message_type_details}"
    NEW_MESSAGE_TYPE_DETAILS = "${new_message_type_details}"
    _locators = {
    }

    @keyword('user edits message type with ${data_type} data')
    def user_edits_message_type_using(self, data_type):
        new_details = self.builtin.get_variable_value(self.NEW_MESSAGE_TYPE_DETAILS)
        if new_details is None:
            type_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
        else:
            type_desc = new_details['message_desc']
        TEXTFIELD.insert_into_field("Message Type Description", type_desc)
        self.builtin.set_test_variable("${message_desc}", type_desc)
        if data_type != "invalid":
            BUTTON.click_button("Save")

    @keyword('validate error message on invalid description')
    def validate_invalid_desc_error_message(self):
        TEXTFIELD.validate_validation_msg("Message Type Description", "Value does not match required pattern")
        BUTTON.click_button("Cancel")
