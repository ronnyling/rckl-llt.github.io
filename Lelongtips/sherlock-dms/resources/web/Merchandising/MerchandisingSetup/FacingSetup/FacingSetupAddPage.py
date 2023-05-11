from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import TEXTFIELD, DRPSINGLE, BUTTON, RADIOBTN, POPUPMSG

class FacingSetupAddPage(PageObject):
    PAGE_TITLE = "Merchandising / Merchandising Setup / Facing Setup"
    PAGE_URL = "/merchandising/merc-prod-group?template=p"
    SETUP_DETAILS="${setup_details}"
    BRAND_CODE = "Brand Code"
    BRAND_DESC = "Brand Description"
    _locators = {

    }

    @keyword('user creates facing setup using ${data_type} data')
    def user_creates_facing_setup_with_data(self, data_type):
        BUTTON.click_button("Add")
        if data_type == "fixed" or data_type=="existing":
            self.create_fixed_data_setup()
        else:
            RADIOBTN.select_from_radio_button("Type", "random")
            setup_category = DRPSINGLE.selects_from_single_selection_dropdown("Category", "random")
            if data_type=="random":
                setup_code = TEXTFIELD.insert_into_field_with_length(self.BRAND_CODE, "random", 10)
                TEXTFIELD.insert_into_field_with_length(self.BRAND_DESC, "random", 15)
                self.builtin.set_test_variable("${setup_code}", setup_code)
                self.builtin.set_test_variable("${setup_category}", setup_category)
            elif data_type =="invalid":
                TEXTFIELD.insert_into_field(self.BRAND_CODE, "*!&@^#%$")
                TEXTFIELD.insert_into_field(self.BRAND_DESC, "        ")
        BUTTON.click_button("Save")

    def create_fixed_data_setup(self):
        setup = self.builtin.get_variable_value(self.SETUP_DETAILS)
        DRPSINGLE.selects_from_single_selection_dropdown("Category", setup['category'])
        TEXTFIELD.insert_into_field(self.BRAND_CODE, setup['brand_code'])
        TEXTFIELD.insert_into_field(self.BRAND_DESC, setup['brand_desc'])
        RADIOBTN.select_from_radio_button("Type", setup['type'])

    @keyword('user validates the missing mandatory error message')
    def validate_missing_mandatory_error_message(self):
        TEXTFIELD.validate_validation_msg("Category", "Please select a value")
        TEXTFIELD.validate_validation_msg(self.BRAND_CODE, "Please enter a value")
        TEXTFIELD.validate_validation_msg(self.BRAND_DESC, "Please enter a value")

    @keyword('data will be limited to set length')
    def validate_data_limited_to_set_length(self):
        setup = self.builtin.get_variable_value(self.SETUP_DETAILS)
        cd_limit= TEXTFIELD.retrieves_text_field_length(self.BRAND_CODE)
        desc_limit= TEXTFIELD.retrieves_text_field_length(self.BRAND_DESC)
        assert int(cd_limit) < len(setup['long_code']), "Brand Code is not limited to set length"
        assert int(desc_limit) < len(setup['long_desc']), "Brand Description is not limited to set length"


    @keyword('user tries to create facing setup using maximum data')
    def create_setup_with_maximum_length_data(self):
        BUTTON.click_button("Add")
        setup = self.builtin.get_variable_value(self.SETUP_DETAILS)
        TEXTFIELD.insert_into_field(self.BRAND_CODE, setup['long_code'])
        TEXTFIELD.insert_into_field(self.BRAND_DESC, setup['long_desc'])

    @keyword("expect pop up message: ${msg}")
    def expect_error(self, msg):
        POPUPMSG.validate_pop_up_msg(msg)
        POPUPMSG.click_button_on_pop_up_msg()
        BUTTON.click_button("Cancel")


