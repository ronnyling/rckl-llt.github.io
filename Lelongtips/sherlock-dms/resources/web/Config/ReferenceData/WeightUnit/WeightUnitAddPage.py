from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from resources.web import BUTTON, TEXTFIELD, POPUPMSG
import secrets


class WeightUnitAddPage(PageObject):

    PAGE_TITLE = "Configuration / Reference Data / Weight Unit"
    PAGE_URL = "objects/weight-unit"
    WEIGHT_CD = "${weight_cd}"
    WEIGHT_DESC = "${weight_desc}"
    CONV_FACTOR_KG = "${conv_factor_kg}"
    _locators = {

    }

    @keyword('user creates weight unit with ${data_type} data')
    def user_creates_weight_unit_using(self, data_type):
        details = self.builtin.get_variable_value(self.WEIGHT_CD)
        if details is None and data_type != "empty":
            weight_cd = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            weight_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
            conv_factor_kg = secrets.choice(range(1, 360))
        elif data_type == "deleted" or data_type == "existing":
            weight_cd = BuiltIn().get_variable_value(self.WEIGHT_CD)
            weight_desc = BuiltIn().get_variable_value(self.WEIGHT_DESC)
            conv_factor_kg = BuiltIn().get_variable_value(self.CONV_FACTOR_KG)
        else:
            weight_cd = details['weight_cd']
            weight_desc = details['weight_desc']
            conv_factor_kg = details['conv_factor_kg']

        BUTTON.click_button("Add")
        TEXTFIELD.insert_into_field("Weight Code", weight_cd)
        TEXTFIELD.insert_into_field("Weight Description", weight_desc)
        TEXTFIELD.insert_into_field("Conversion Factor To KG", conv_factor_kg)
        if data_type != "empty":
            self.builtin.set_test_variable("${weight_cd}", weight_cd)
        self.builtin.set_test_variable("${weight_desc}", weight_desc)
        self.builtin.set_test_variable("${conv_factor_kg}", conv_factor_kg)
        BUTTON.click_button("Save")

    @keyword('validate error message on empty fields')
    def validate_invalid_fields(self):
        error = "Please enter a value"
        TEXTFIELD.validate_validation_msg("Weight Unit", error)
        TEXTFIELD.validate_validation_msg("Weight Description", error)
        TEXTFIELD.validate_validation_msg("Conversion Factor To KG", error)

    def error_message_weight_unit_already_exists(self):
        POPUPMSG.validate_pop_up_msg("The record already exists")
        POPUPMSG.click_button_on_pop_up_msg()

    @keyword("expect pop up message: ${msg}")
    def expect_error(self, msg):
        POPUPMSG.validate_pop_up_msg(msg)
        POPUPMSG.click_button_on_pop_up_msg()
