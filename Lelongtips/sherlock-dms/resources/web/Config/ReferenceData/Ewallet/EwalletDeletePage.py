from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn

from resources.web import DRPSINGLE, TEXTFIELD, CALENDAR, TOGGLE, BUTTON
from robot.api.deco import keyword

from resources.web.Common import MenuNav


class EwalletAddPage(PageObject):
    """ Functions related to KPI created """
    PAGE_TITLE = "Configuration / Reference Data / E-wallet"
    PAGE_URL = "objects/e-wallet"

    _locators = {
        "ewallet_code": "(//div[contains(text(),'KPI Type Code')]/following::input)[1]",
        "ewallet_desc": "(//div[contains(text(),'KPI Type Description')]/following::input)[2]"
    }

    def user_clicks_cancel(self):
        self.builtin.set_test_variable("${updated_ewallet_cd}", self.builtin.set_test_variable("${ewallet_cd}"))
        self.builtin.set_test_variable("${updated_ewallet_name}", self.builtin.set_test_variable("${ewallet_name}"))
        BUTTON.click_button("Cancel")

    def click_add_ewallet_button(self):
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()