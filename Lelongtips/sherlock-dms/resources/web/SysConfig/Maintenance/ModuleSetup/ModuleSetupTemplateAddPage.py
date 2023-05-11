""" Python file related to module setup UI """
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web import TEXTFIELD, RADIOBTN, BUTTON, DRPSINGLE


class ModuleSetupTemplateAddPage(PageObject):
    """ Functions related to module setup add page """

    PAGE_TITLE = "System Configuration / Maintenance / Module Setup"
    PAGE_URL = "/metadata-config/metadata-module"

    _locators = {
    }

    @keyword("user creates module setup template using ${data_type} data")
    def user_creates_module_setup_template_using_data(self, data_type):
        """ Functions to create module setup template using random/fixed data """

        if data_type == "fixed":
            BUTTON.click_tab("Template Configuration")
            BUTTON.click_button("Add")
            fixed_data = BuiltIn().get_variable_value("${ModuleSetupTemplateDetails}")
            template_name = fixed_data["TEMPLATE_NAME"]
            template_desc = fixed_data["TEMPLATE_DESCRIPTION"]
            BuiltIn().set_test_variable("${template_name}", template_name)
            BuiltIn().set_test_variable("${template_desc}", template_desc)

        if data_type == "fixed":
            TEXTFIELD.insert_into_field("Template Name", template_name)
            TEXTFIELD.insert_into_field("Template Description", template_desc)
        else:
            TEXTFIELD.insert_into_field("Template Name", "random")
            TEXTFIELD.insert_into_field("Template Description", "random")

        self.builtin.wait_until_keyword_succeeds("0.5 min", "3 sec", "click_element",
                                                 "//i[@class='anticon anticon-form ng-star-inserted']//*[local-name()='svg']")
        RADIOBTN.select_from_radio_button("Panels & Container", "")
        RADIOBTN.return_selected_item_of_radio_button("Panels & Container")
        BUTTON.click_tab("Layout1")
        DRPSINGLE.selects_from_single_selection_dropdown("Display Type", "Panel")
        TEXTFIELD.insert_into_field("Title", "General Info")
        TEXTFIELD.insert_into_field("Column", "2")
        BUTTON.click_button("Ok")

        BUTTON.click_button("Save")
