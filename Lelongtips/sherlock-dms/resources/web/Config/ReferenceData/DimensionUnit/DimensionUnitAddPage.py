from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from resources.web import BUTTON, TEXTFIELD, POPUPMSG
import secrets


class DimensionUnitAddPage(PageObject):

    PAGE_TITLE = "Configuration / Reference Data / Dimension Unit"
    PAGE_URL = "objects/dimension-unit"
    DIMENSION_UNIT = "${dimension_unit}"
    DIMENSION_DESC = "${dimension_desc}"
    CONVERSION_FACTOR = "${conversion_factor}"
    _locators = {

    }

    @keyword('user creates dimension unit with ${data_type} data')
    def user_creates_dimension_unit_using(self, data_type):
        details = self.builtin.get_variable_value(self.DIMENSION_UNIT)
        if details is None and data_type != "empty":
            dimension_unit = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            dimension_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
            conversion_factor = secrets.choice(range(1, 360))
        elif data_type == "deleted" or data_type == "existing":
            dimension_unit = BuiltIn().get_variable_value(self.DIMENSION_UNIT)
            dimension_desc = BuiltIn().get_variable_value(self.DIMENSION_DESC)
            conversion_factor = BuiltIn().get_variable_value(self.CONVERSION_FACTOR)
        else:
            dimension_unit = details['dimension_unit']
            dimension_desc = details['dimension_desc']
            conversion_factor = details['conversion_factor']

        BUTTON.click_button("Add")
        TEXTFIELD.insert_into_field("Dimension Unit", dimension_unit)
        TEXTFIELD.insert_into_field("Dimension Description", dimension_desc)
        TEXTFIELD.insert_into_field("Conversion Factor To M", conversion_factor)
        if data_type != "empty":
            self.builtin.set_test_variable("${dimension_unit}", dimension_unit)
        self.builtin.set_test_variable("${dimension_desc}", dimension_desc)
        self.builtin.set_test_variable("${conversion_factor}", conversion_factor)
        BUTTON.click_button("Save")

    @keyword('validate error message on empty fields')
    def validate_invalid_fields(self):
        error = "Please enter a value"
        TEXTFIELD.validate_validation_msg("Dimension Unit", error)
        TEXTFIELD.validate_validation_msg("Dimension Description", error)
        TEXTFIELD.validate_validation_msg("Conversion Factor To M", error)

    def error_message_dimension_unit_already_exists(self):
        POPUPMSG.validate_pop_up_msg("The record already exists")
        POPUPMSG.click_button_on_pop_up_msg()

    @keyword("expect pop up message: ${msg}")
    def expect_error(self, msg):
        POPUPMSG.validate_pop_up_msg(msg)
        POPUPMSG.click_button_on_pop_up_msg()
