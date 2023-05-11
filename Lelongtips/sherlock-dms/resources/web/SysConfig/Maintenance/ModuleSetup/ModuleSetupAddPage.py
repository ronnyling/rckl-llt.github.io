""" Python file related to module setup UI """
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.web import BUTTON, TEXTFIELD, DRPSINGLE
from resources.web.SysConfig.Maintenance.ModuleSetup import ModuleSetupListPage
from resources.web.Common import POMLibrary, AlertCheck


class ModuleSetupAddPage(PageObject):
    """ Functions related to module setup add page """

    PAGE_TITLE = "System Configuration / Maintenance / Module Setup"
    PAGE_URL = "/metadata-config/metadata-module"

    _locators = {
    }

    @keyword("user creates module setup using ${data_type} data")
    def user_creates_module_setup_using_data(self, data_type):
        """ Functions to create module setup using random/fixed data """
        BUTTON.validate_button_is_shown("Add")

        if data_type == "fixed":
            fixed_data = BuiltIn().get_variable_value("${ModuleSetupDetails}")
            module_logical_id = fixed_data["LOGICAL_ID"]
            module_title = fixed_data["TITLE"]
            BuiltIn().set_test_variable("${module_logical_id}", module_logical_id)
            BuiltIn().set_test_variable("${module_title}", module_title)
            ModuleSetupListPage.ModuleSetupListPage().user_inline_search_created_module_setup()
            ModuleSetupListPage.ModuleSetupListPage().user_verify_record_shown()
            is_record_shown = BuiltIn().get_variable_value("${is_record_shown}")
            if is_record_shown:
                return

        ModuleSetupListPage.ModuleSetupListPage().click_add_module_setup_button()
        POMLibrary.POMLibrary().check_page_title("ModuleSetupAddPage")
        if data_type == "fixed":
            TEXTFIELD.insert_into_field("Module Logical Id", module_logical_id)
            TEXTFIELD.insert_into_field("Module Title", module_title)
        else:
            TEXTFIELD.insert_into_field_with_length("Module Logical Id", "random", 8)
            TEXTFIELD.insert_into_field_with_length("Module Title", "random", 8)
        TEXTFIELD.insert_into_field_with_length("Module Description", "random", 8)
        DRPSINGLE.selects_from_single_selection_dropdown("Module Type", "Dynamic")
        TEXTFIELD.insert_into_field("Service Name", "metadata-svc")
        TEXTFIELD.insert_into_field("Service Version", "1.0")
        TEXTFIELD.insert_into_field("Service Parameters", '["module-data"]')
        BUTTON.click_button("Save")

    def user_verified_module_setup_is_created(self):
        """ Functions to verify if fixed module setup is created """
        self.user_creates_module_setup_using_data("fixed")
        is_record_shown = BuiltIn().get_variable_value("${is_record_shown}")
        if not is_record_shown:
            common = AlertCheck.AlertCheck()
            common.successfully_with_message("module setup created", "Record created successfully")
