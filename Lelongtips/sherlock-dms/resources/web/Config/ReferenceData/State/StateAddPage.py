from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web.Common import POMLibrary
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE


class StateAddPage (PageObject):
    """ Functions related to add page of State """
    PAGE_TITLE = "Configuration / Reference Data / State"
    PAGE_URL = "/objects/address-state"


    @keyword('user creates state with ${data_type} data')
    def user_creates_state_with_data(self, data_type):
        """ Function to create state with random/fixed data """
        state_details = self.builtin.get_variable_value("&{state_details}")
        country_name = self.builtin.get_variable_value("&{country_name}")
        POMLibrary.POMLibrary().check_page_title("StateAddPage")
        BUTTON.click_button("Add")
        state_cd = self.user_inserts_state_cd(data_type, state_details)
        state_name = self.user_inserts_state_name(data_type, state_details)
        country_name = self.user_choose_country(data_type, country_name)
        self.builtin.set_test_variable("${state_cd}", state_cd)
        self.builtin.set_test_variable("${state_name}", state_name)
        self.builtin.set_test_variable("${country_name}", country_name)
        BUTTON.click_button("Save")

    def user_inserts_state_cd(self, data_type, details):
        if data_type == "fixed":
            state_cd = TEXTFIELD.insert_into_field("State Code", details['state_cd'])
        elif data_type == "random":
            state_cd = TEXTFIELD.insert_into_field_with_length("State Code", "letter", 8)
        return state_cd

    def user_inserts_state_name(self, data_type, details):
        if data_type == "fixed":
            state_name = TEXTFIELD.insert_into_field("State Name", details['state_name'])
        elif data_type == "random":
            state_name = TEXTFIELD.insert_into_field_with_length("State Name", "random", 8)
        return state_name

    def user_choose_country(self, data_type, country_name):
        if data_type == "fixed":
            if country_name:
                country_name = DRPSINGLE.selects_from_single_selection_dropdown("Country", country_name)
        elif data_type == "random":
                country_name = DRPSINGLE.selects_from_single_selection_dropdown("Country", "random")
        return country_name

