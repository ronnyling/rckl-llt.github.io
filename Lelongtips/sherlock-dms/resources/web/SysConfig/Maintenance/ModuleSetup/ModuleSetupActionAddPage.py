""" Python file related to module setup UI """
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE, DRPMULTIPLE


class ModuleSetupActionAddPage(PageObject):
    PAGE_TITLE = "System Configuration / Maintenance / Module Setup"
    PAGE_URL = "/metadata-config/metadata-module"

    _locator =  {
    }

    @keyword("user creates module setup actions using ${data_type} data")
    def user_creates_module_setup_actions_using_data(self, data_type):
        """ Functions to create module setup actions using random/fixed data """

        if data_type == "fixed":
            BUTTON.click_tab("Actions")
            BUTTON.click_button("Add")
            fixed_data = BuiltIn().get_variable_value("${ModuleSetupActionsDetails}")
            action_title = fixed_data["ACTION_TITLE"]
            action_desc = fixed_data["ACTION_DESC"]
            action_display = fixed_data["ACTION_DISPLAY"]
            action_name = fixed_data["ACTION_NAME"]
            BuiltIn().set_test_variable("${action_title}", action_title)
            BuiltIn().set_test_variable("${action_desc}", action_desc)
            BuiltIn().set_test_variable("${action_display}", action_display)
            BuiltIn().set_test_variable("${action_name}", action_name)

        if data_type == "fixed":
            self._wait_for_page_refresh()
            TEXTFIELD.insert_into_field("Action Title", action_title)
            TEXTFIELD.insert_into_field("Action Description", action_desc)
            TEXTFIELD.insert_into_field("Action Name", action_name)
            DRPSINGLE.select_from_single_selection_dropdown("Action Display Type", action_display)
        else:
            TEXTFIELD.insert_into_field("Action Title", "random")
            TEXTFIELD.insert_into_field("Action Description", "random")
            TEXTFIELD.insert_into_field("Action Name", "random")
            DRPSINGLE.select_from_single_selection_dropdown("Action Display Type", "random")

        self.builtin.wait_until_keyword_succeeds("0.5 min", "3 sec", "click_element",
                                                 "//i[@class='anticon anticon-form ng-star-inserted']//*[local-name()='svg']")
        DRPSINGLE.select_from_single_selection_dropdown("Button Type", "primary")
        DRPMULTIPLE.select_from_multi_selection_dropdown("Scope", "mmDevProfile.U")
        BUTTON.click_button("Ok")
        BUTTON.click_button("Save")
