""" Python file related to module setup UI """
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.web import DRPSINGLE, BUTTON


class ModuleSetupRelationshipAddPage(PageObject):
    """ Functions related to module setup relationship add page """
    PAGE_TITLE = "System Configuration / Maintenance / Module Setup"
    PAGE_URL = "/metadata-config/metadata-module"

    _locators = {
    }

    @keyword("user creates module setup relationship using ${data_type} data")
    def user_creates_module_setup_relationship_using_data(self, data_type):
        """ Functions to create module setup relationship using random/fixed data """

        if data_type == "fixed":
            BUTTON.click_tab("Relationships")
            BUTTON.click_button("Add")
            fixed_data = BuiltIn().get_variable_value("${ModuleSetupRelationshipDetails}")
            module_logical_id = fixed_data["LOGICAL_ID"]
            relationship_type = fixed_data["RELATIONSHIP_TYPE"]
            BuiltIn().set_test_variable("${module_logical_id}", module_logical_id)
            BuiltIn().set_test_variable("${relationship_type}", relationship_type)

        if data_type == "fixed":
            DRPSINGLE.selects_from_single_selection_dropdown("Target Module Logical Id", module_logical_id)
            DRPSINGLE.selects_from_single_selection_dropdown("Relationship Type", relationship_type)
        else:
            DRPSINGLE.selects_from_single_selection_dropdown("Target Module Logical Id", "random")
            DRPSINGLE.selects_from_single_selection_dropdown("Relationship Type", "random")

        BUTTON.click_button("Save")

