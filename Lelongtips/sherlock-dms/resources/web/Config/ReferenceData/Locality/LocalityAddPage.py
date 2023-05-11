from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web.Common import POMLibrary
from resources.web import DRPSINGLE, BUTTON, TEXTFIELD


class LocalityAddPage(PageObject):
    """ Functions related to add page of Locality """
    PAGE_TITLE = "Configuration / Reference Data / Locality"
    PAGE_URL = "/objects/address-city"


    @keyword('user creates locality with ${data_type} data')
    def user_creates_locality_with_data(self, data_type):
        """ Function to create locality with random/fixed data """
        locality_details = self.builtin.get_variable_value("&{locality_details}")
        state_name = self.builtin.get_variable_value("&{state_name}")
        POMLibrary.POMLibrary().check_page_title("LocalityAddPage")
        BUTTON.click_button("Add")
        city_cd = self.user_inserts_city_cd(data_type, locality_details)
        city_name = self.user_inserts_city_name(data_type, locality_details)
        state_name = self.user_choose_state(data_type, state_name)
        self.builtin.set_test_variable("${city_cd}", city_cd)
        self.builtin.set_test_variable("${city_name}", city_name)
        self.builtin.set_test_variable("${state_name}", state_name)
        BUTTON.click_button("Save")

    def user_inserts_city_cd(self, data_type, locality_details):
        locality_code = "Locality Code"
        if data_type == "fixed":
            city_cd = TEXTFIELD.insert_into_field(locality_code, locality_details['city_cd'])
        elif data_type == "random":
            city_cd = TEXTFIELD.insert_into_field_with_length(locality_code, "letter", 8)
        return city_cd

    def user_inserts_city_name(self, data_type, locality_details):
        locality_name = "Locality Name"
        if data_type == "fixed":
            city_name = TEXTFIELD.insert_into_field(locality_name, locality_details['city_name'])
        elif data_type == "random":
            city_name = TEXTFIELD.insert_into_field_with_length(locality_name, "random", 8)
        return city_name

    def user_choose_state(self, data_type, state_name):
        if data_type == "fixed":
            if state_name:
                state_name = DRPSINGLE.selects_from_single_selection_dropdown("State", state_name)
        elif data_type == "random":
            state_name = DRPSINGLE.selects_from_single_selection_dropdown("State", "random")
        return state_name

    @keyword("return validation message '${message}'")
    def validate_validation_message(self, message):
        TEXTFIELD.validate_validation_msg("Locality Code", message)
        TEXTFIELD.validate_validation_msg("Locality Name", message)
