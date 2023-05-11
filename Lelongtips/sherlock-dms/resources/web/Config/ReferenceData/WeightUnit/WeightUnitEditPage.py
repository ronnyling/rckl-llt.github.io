from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, LABEL



class WeightUnitEditPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Weight Unit"
    PAGE_URL = "objects/weight-unit"
    _locators = {
    }

    @keyword('user edits weight unit with ${data_type} data')
    def user_edits_weight_unit_using(self, data_type):
        weight_desc = TEXTFIELD.insert_into_field_with_length("Weight Description", "random", 50)
        TEXTFIELD.insert_into_field("Weight Description", weight_desc)
        self.builtin.set_test_variable("${weight_desc}", weight_desc)
        BUTTON.click_button("Save")

    @keyword('weight unit viewed successfully')
    def weight_unit_viewed_successfully(self):
        LABEL.validate_label_is_visible("EDIT | Weight Unit")
        BUTTON.click_button("Cancel")
