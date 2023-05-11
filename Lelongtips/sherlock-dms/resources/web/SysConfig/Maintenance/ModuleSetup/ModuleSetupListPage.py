""" Python file related to module setup UI """
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, POPUPMSG
from resources.web.Common import POMLibrary


class ModuleSetupListPage(PageObject):
    """ Functions related to module setup list page """
    PAGE_TITLE = "System Configuration / Maintenance / Module Setup"
    PAGE_URL = "/metadata-config/metadata-module"

    _locators = {
        "first_row_hyperlink": "//tr[1]//td[2]//core-cell-render//div//a"
    }

    def click_add_module_setup_button(self):
        """ Functions to click on Add button """
        POMLibrary.POMLibrary().check_page_title("ModuleSetupListPage")
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    def user_inline_search_created_module_setup(self):
        """ Functions to perform inline search """
        BUTTON.click_icon("search")
        module_logical_id = BuiltIn().get_variable_value("${module_logical_id}")
        module_title = BuiltIn().get_variable_value("${module_title}")
        POPUPMSG.insert_into_field_in_pop_up("Module Logical Id", module_logical_id)
        POPUPMSG.insert_into_field_in_pop_up("Module Title", module_title)

    def user_verify_record_shown(self):
        """ Functions to verify if record shown in the listing page """
        try:
            self.selib.page_should_contain_element(self.locator.first_row_hyperlink)
            is_record_shown = True
        except Exception as e:
            print(e.__class__, "occured")
            is_record_shown = False

        BuiltIn().set_test_variable("${is_record_shown}", is_record_shown)
