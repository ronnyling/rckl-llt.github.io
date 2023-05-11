from robot.api.deco import keyword
from PageObjectLibrary import PageObject

from resources.web import BUTTON, LABEL
from resources.web.Config.Attribute.AttributeCreation.AttributeCreationAddPage import AttributeCreationAddPage


class AttributeCreationEditPage(PageObject):
    """ Functions related to Attribute Creation Edit """

    @keyword('user edits attribute creation with ${data_type} data')
    def user_edits_attribute_creation_data(self, data_type):
        LABEL.validate_label_is_visible("EDIT | Attribute Creation")
        details = self.builtin.get_variable_value("${attribute_creation_details}")
        attribute_creation_cd = self.builtin.get_variable_value("${attribute_creation_cd}")
        AttributeCreationAddPage().user_inserts_attribute(data_type, details)
        self.builtin.set_test_variable("${attribute_creation_cd}", attribute_creation_cd)
        BUTTON.click_button("Save")
