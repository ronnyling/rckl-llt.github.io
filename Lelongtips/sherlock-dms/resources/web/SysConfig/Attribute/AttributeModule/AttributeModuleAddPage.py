from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web.SysConfig.Attribute.AttributeModule import AttributeModuleListPage
from resources.web import TEXTFIELD, BUTTON
from robot.libraries.BuiltIn import BuiltIn


class AttributeModuleAddPage(PageObject):
    PAGE_TITLE = "System Configuration / Attribute / Attribute Module"
    PAGE_URL = "objects/module-data/module"

    _locators = {
    }

    @keyword("user creates attribute module using ${data_source} data")
    def user_creates_attribute_module_using_data(self, data_source):
        """ Functions to create attribute usage using random/given data """
        BUTTON.validate_button_is_shown("Add")
        details = BuiltIn().get_variable_value("${AttributeModuleDetails}")
        AttributeModuleListPage.AttributeModuleListPage().click_add_attribute_module_button()
        if data_source == "given":
            TEXTFIELD.insert_into_field_with_length("Code", "random", 8)
            TEXTFIELD.inserts_into_field_with_length("Module", details['amModule'], 15)
        else:
            TEXTFIELD.insert_into_field_with_length("Code", "random", 8)
            TEXTFIELD.inserts_into_field_with_length("Module", "random", 15)
        BUTTON.click_button("Save")

