""" Python file related to module setup UI """
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web import TEXTFIELD, BUTTON, DRPSINGLE


class ModuleSetupFieldAddPage(PageObject):
    """ Functions related to module setup add page """

    PAGE_TITLE = "System Configuration / Maintenance / Module Setup"
    PAGE_URL = "/metadata-config/metadata-module"

    _locators = {
    }

    @keyword("user creates module setup fields using ${data_type} data")
    def user_creates_module_setup_fields_using_data(self, data_type):
        """ Functions to create module setup fields using random/fixed data """

        if data_type == "fixed":
            BUTTON.click_tab("Metadata Fields")
            BUTTON.click_button("Add")
            fixed_data = BuiltIn().get_variable_value("${ModuleSetupFieldsDetails}")
            field_label = fixed_data["FIELD_LABEL"]
            field_desc = fixed_data["FIELD_DESC"]
            field_name = fixed_data["FIELD_NAME"]
            field_type = fixed_data["FIELD_TYPE"]
            display_type = fixed_data["DISPLAY_TYPE"]
            BuiltIn().set_test_variable("${field_label}", field_label)
            BuiltIn().set_test_variable("${field_desc}", field_desc)
            BuiltIn().set_test_variable("${field_name}", field_name)
            BuiltIn().set_test_variable("${field_type}", field_type)
            BuiltIn().set_test_variable("${display_type}", display_type)

        if data_type == "fixed":
            TEXTFIELD.insert_into_field("Field Label", field_label)
            TEXTFIELD.insert_into_field("Field Description", field_desc)
            TEXTFIELD.insert_into_field("Field Name", field_name)
            DRPSINGLE.select_from_single_selection_dropdown("Field Type", field_type)
            DRPSINGLE.select_from_single_selection_dropdown("Display Type", display_type)
        else:
            TEXTFIELD.insert_into_field("Field Label", "random")
            TEXTFIELD.insert_into_field("Field Description", "random")
            TEXTFIELD.insert_into_field("Field Name", "random")
            DRPSINGLE.select_from_single_selection_dropdown("Field Type", "random")
            DRPSINGLE.select_from_single_selection_dropdown("Display Type", "random")

        self.builtin.wait_until_keyword_succeeds("0.5 min", "3 sec", "click_element",
                                                "//h6[contains(text(),'Displayable Fields')]//i[@class='anticon anticon-form ng-star-inserted']//*[local-name()='svg']")
        TEXTFIELD.insert_into_field("Width", "250")
        BUTTON.click_button("Ok")
        BUTTON.click_button("Save")


