""" Python file related to menu setup UI """
import secrets
import string

from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.web.Common import POMLibrary, AlertCheck
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE
from resources.web.SysConfig.Maintenance.MenuSetup import MenuSetupListPage


class MenuSetupAddPage(PageObject):
    """ Functions related to menu setup add page """

    PAGE_TITLE = "System Configuration / Maintenance / Menu Setup"
    PAGE_URL = "/metadata-config/setting-menu"

    _locators = {
    }

    @keyword("user creates menu setup using ${data_type} data")
    def user_creates_menu_setup_using_data(self, data_type):
        """ Functions to create menu setup using random/fixed data """
        BUTTON.validate_button_is_shown("Add")

        if data_type == "fixed":
            fixed_data = BuiltIn().get_variable_value("${MenuSetupDetails}")
            label = fixed_data["LABEL"]
            selected_type = fixed_data["TYPE"]
            seq_number = fixed_data["SEQ_NUMBER"]
            BuiltIn().set_test_variable("${label}", label)
            BuiltIn().set_test_variable("${seq_number}", seq_number)
            if selected_type == "1":
                url = fixed_data["URL"]
            MenuSetupListPage.MenuSetupListPage().user_inline_search_created_menu_setup()
            print("user_verify_record_shown")
            MenuSetupListPage.MenuSetupListPage().user_verify_record_shown()
            print("start is_record_shown")
            is_record_shown = BuiltIn().get_variable_value("${is_record_shown}")
            print("is_record_shown", is_record_shown)
            if is_record_shown:
                return

        MenuSetupListPage.MenuSetupListPage().click_add_menu_setup_button()
        POMLibrary.POMLibrary().check_page_title("MenuSetupAddPage")
        if data_type == "fixed":
            TEXTFIELD.insert_into_field("Label", label)
            if selected_type == "0":
                DRPSINGLE.selects_from_single_selection_dropdown("Type", "Folder")
            else:
                DRPSINGLE.selects_from_single_selection_dropdown("Type", "Node")
                TEXTFIELD.insert_into_field("Url", url)
            TEXTFIELD.insert_into_field("Sequence", seq_number)
        else:
            TEXTFIELD.insert_into_field_with_length("Label", "random", 8)
            selected_type = DRPSINGLE.selects_from_single_selection_dropdown("Type", "random")
            TEXTFIELD.insert_into_field_with_length("Sequence", "number", 8)
            print("selected_type", selected_type)
            if selected_type == "1":
                random_word = ''.join(secrets.choice(string.ascii_letters) for _ in range(8))
                TEXTFIELD.insert_into_field("Url", "/{0}".format(random_word))
        BUTTON.click_button("Save")

    def user_verified_menu_setup_is_created(self):
        """ Functions to verify if fixed menu setup is created """
        self.user_creates_menu_setup_using_data("fixed")
        is_record_shown = BuiltIn().get_variable_value("${is_record_shown}")
        if not is_record_shown:
            common = AlertCheck.AlertCheck()
            common.successfully_with_message("menu setup created", "Record created successfully")

