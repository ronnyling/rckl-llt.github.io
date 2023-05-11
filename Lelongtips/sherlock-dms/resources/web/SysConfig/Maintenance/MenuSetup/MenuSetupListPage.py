""" Python file related to menu setup UI """
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn

from resources.web import POPUPMSG, BUTTON
from resources.web.Common import POMLibrary


class MenuSetupListPage(PageObject):
    """ Functions related to menu setup list page """
    PAGE_TITLE = "System Configuration / Maintenance / Menu Setup"
    PAGE_URL = "/metadata-config/setting-menu"

    _locators = {
        "first_row_hyperlink": "//tr[1]//td[2]//core-cell-render//div//a",
        "inline_search_clear_icon": "//nz-form-control//nz-input-group//i",
        "inline_search_row": "//tr[contains(@class, 'inline-filter')]"
    }

    def click_add_menu_setup_button(self):
        """ Functions to click on Add button """
        POMLibrary.POMLibrary().check_page_title("MenuSetupListPage")
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    def user_inline_search_created_menu_setup(self):
        """ Functions to perform inline search """
        BUTTON.click_icon("search")
        label = BuiltIn().get_variable_value("${label}")
        POPUPMSG.insert_into_field_in_pop_up("Label", label)
        self._wait_for_page_refresh()

    def user_verify_record_shown(self):
        """ Functions to verify if record shown in the listing page """
        try:
            self.selib.page_should_contain_element(self.locator.first_row_hyperlink)
            is_record_shown = True
        except Exception as e:
            print(e.__class__, "occured")
            is_record_shown = False

        BuiltIn().set_test_variable("${is_record_shown}", is_record_shown)
