from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, COMMON_KEY


class PosmFocusCustomersListPage(PageObject):
    PAGE_TITLE = "Merchandising / Merchandising Setup / POSM Focus Customers"
    PAGE_URL = "/merchandising/posm-focused-customers"
    POSM_DETAILS = "${posm_details}"

    _locators = {
        "posm_search": "//*[contains(text(),'POSM Focused Customers')]//following::core-button[@ng-reflect-icon='search']",
        "delete_button": "//*[contains(text(),'POSM Focused Customers')]//following::core-button[@ng-reflect-icon='delete'][2]"
    }

    @keyword('user validates buttons for ${login}')
    def user_validates_buttons(self, login):
        if login == "hq admin":
            BUTTON.validate_button_is_shown("Add")
            COMMON_KEY.wait_keyword_success("page_should_contain_element", self.locator.delete_button)
        elif login == "distributor":
            BUTTON.validate_button_is_hidden("Add")
            COMMON_KEY.wait_keyword_success("page_should_not_contain_element", self.locator.delete_button)
        COMMON_KEY.wait_keyword_success("page_should_contain_element", self.locator.posm_search)
        BUTTON.validate_icon_is_shown("filter")
