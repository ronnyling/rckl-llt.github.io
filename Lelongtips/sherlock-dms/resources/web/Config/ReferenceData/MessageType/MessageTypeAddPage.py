from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON,TEXTFIELD
import secrets


class MessageTypeAddPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Message Type"
    PAGE_URL = "/objects/message-type"
    MESSAGE_TYPE_DETAILS = "${message_type_details}"

    _locators = {
    }

    @keyword('user creates message type with ${data_type} data')
    def user_creates_message_type_using(self, data_type):
        details = self.builtin.get_variable_value(self.MESSAGE_TYPE_DETAILS)
        if details is None:
            type_code = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            type_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
        else:
            type_code = details['message_code']
            type_desc = details['message_desc']
        BUTTON.click_button("Add")
        TEXTFIELD.insert_into_field("Message Type Code", type_code)
        TEXTFIELD.insert_into_field("Message Type Description", type_desc)
        self.builtin.set_test_variable("${message_code}", type_code)
        self.builtin.set_test_variable("${message_desc}", type_desc)
        BUTTON.click_button("Save")

    @keyword('validate error message on invalid fields')
    def validate_invalid_fields(self):
        TEXTFIELD.validate_validation_msg("Message Type Code", "Value does not match required pattern")
        TEXTFIELD.validate_validation_msg("Message Type Description", "Value does not match required pattern")
