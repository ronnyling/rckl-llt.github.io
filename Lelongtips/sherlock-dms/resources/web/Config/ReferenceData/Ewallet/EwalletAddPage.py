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

    @keyword('user creates ewallet with ${data_type} data')
    def user_creates_kpi(self, data_type):
        if data_type == "fixed":
            BUTTON.click_button("Add")
            TEXTFIELD.insert_into_field("E-wallet Code", "Ewallet")
            TEXTFIELD.insert_into_field("E-wallet Description", "Ewallet")
            BUTTON.click_button("Save")
        if data_type == "random":
            BUTTON.click_button("Add")
            TEXTFIELD.insert_into_field("E-wallet Code", "random")
            TEXTFIELD.insert_into_field("E-wallet Description", "random")
            BUTTON.click_button("Save")

    @keyword("validate the UI items")
    def validate_ui_items(self, title):
        MenuNav.MenuNav().user_navigates_to_menu("Configuration | Reference Data | E-wallet")
        if title == "ewallet_code":
            COMMON_KEY.wait_keyword_success("page_should_contain_element",
                                            self.locator.ewallettype_code)
        elif title == "ewallet_desc":
            COMMON_KEY.wait_keyword_success("page_should_contain_element",
                                            self.locator.ewallettype_desc)
        else:
            COMMON_KEY.wait_keyword_success("page_should_contain_element",
                                            self.locator.chart_color)
