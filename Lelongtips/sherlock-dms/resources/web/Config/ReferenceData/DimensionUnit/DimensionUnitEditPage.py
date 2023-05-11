from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, LABEL



class DimensionUnitEditPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Dimension Unit"
    PAGE_URL = "objects/dimension-unit"
    _locators = {
    }

    @keyword('user edits dimension unit with ${data_type} data')
    def user_edits_dimension_unit_using(self, data_type):
        dimension_desc = TEXTFIELD.insert_into_field_with_length("Dimension Description", "random", 50)
        TEXTFIELD.insert_into_field("Dimension Description", dimension_desc)
        self.builtin.set_test_variable("${dimension_desc}", dimension_desc)
        BUTTON.click_button("Save")

    @keyword('dimension unit viewed successfully')
    def dimension_unit_viewed_successfully(self):
        LABEL.validate_label_is_visible("EDIT | Dimension Unit")
        BUTTON.click_button("Cancel")
