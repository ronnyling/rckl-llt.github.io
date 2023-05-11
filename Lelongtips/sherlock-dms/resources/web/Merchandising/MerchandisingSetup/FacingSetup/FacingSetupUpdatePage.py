from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON,DRPSINGLE,TEXTFIELD,RADIOBTN

class FacingSetupUpdatePage(PageObject):

    PAGE_TITLE = "Merchandising / Merchandising Setup / Facing Setup"
    PAGE_URL = "/merchandising/merc-prod-group?template=p"
    SETUP_DETAILS = "${setup_details}"
    BRAND_DESC = "Brand Description"
    _locators = {
    }

    @keyword('user updates facing setup using ${data_type} data')
    def user_edits_facing_setup_data(self, data_type):
        if data_type == "random":
            setup_category=DRPSINGLE.selects_from_single_selection_dropdown("Category", "random")
            TEXTFIELD.insert_into_field_with_length(self.BRAND_DESC, "random", 15)
            RADIOBTN.select_from_radio_button("Type", "random")
            self.builtin.set_test_variable("${setup_category}", setup_category)
        if data_type == "empty":
            TEXTFIELD.insert_into_field("")
        BUTTON.click_button("Save")

    @keyword('user validates brand code is not editable')
    def user_validates_brand_code_not_editable(self):
        TEXTFIELD.verifies_text_field_is_disabled("Brand Code")
        BUTTON.click_button("Cancel")

    def facing_setup_unable_to_update_successfully_with_validation_message_on_fields(self):
        TEXTFIELD.validate_validation_msg("Brand Description", "Please enter a value")
        BUTTON.click_button("Cancel")
