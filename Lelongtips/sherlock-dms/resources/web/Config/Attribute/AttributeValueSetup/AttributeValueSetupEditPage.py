from robot.api.deco import keyword
from PageObjectLibrary import PageObject

from resources.web import BUTTON, LABEL
from resources.web.Config.Attribute.AttributeValueSetup import AttributeValueSetupAddPage


class AttributeValueSetupEditPage(PageObject):
    """ Functions related to Attribute Value Setup Edit """

    @keyword('user edits attribute value setup with ${data_type} data')
    def user_edits_attribute_value_setup_data(self, data_type):
        LABEL.validate_label_is_visible("EDIT | Attribute Value Setup")
        details = self.builtin.get_variable_value("${attribute_value_setup_details}")
        bank_cd = self.builtin.get_variable_value("${attribute_value_setup_cd}")
        bank_desc = AttributeValueSetupAddPage.AttributeValueSetupAddPage().user_inserts_attribute(data_type, details)
        self.builtin.set_test_variable("${attribute_value_setup_cd}", bank_cd)
        self.builtin.set_test_variable("${attribute_value_setup_val}", bank_desc)
        BUTTON.click_button("Save")
