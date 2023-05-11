from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, DRPSINGLE, COMMON_KEY, TEXTFIELD


class PosmFocusCustomersAddPage(PageObject):
    PAGE_TITLE = "Merchandising / Merchandising Setup / POSM Focus Customers"
    PAGE_URL = "/merchandising/posm-focused-customers"
    POSM_DETAILS = "${posm_details}"

    _locators = {
        "cg_search": "//*[contains(text(), 'Customer Group')]//following::core-button[@ng-reflect-icon='search'][1]",
        "cg_label": "//*[contains(text(), 'ChannelB19')]",
        "popup_search": "//*[contains(text(),'ADD POSM')]//following::core-button[@ng-reflect-icon='search']",
        "search_code": "//*[contains(text(),'ADD POSM')]/following::input[3]",
        "popup_checkbox": "//*[text()='ADD POSM']//following::*[contains(@class,'checkbox')][1]",
        "posm_search": "//*[contains(text(),'POSM Focused Customers')]//following::core-button[@ng-reflect-icon='search']",
        "posm_checkbox": "//*[contains(text(), 'POSM Focused Customers')]//following::*[contains(@class,'checkbox')][1]",
        "delete_button": "//*[contains(text(),'POSM Focused Customers')]//following::core-button[@ng-reflect-icon='delete'][2]"
    }

    @keyword('user ${action} posm')
    def user_manages_posm(self, action):
        cg_details = self.builtin.get_variable_value(self.POSM_DETAILS)
        if action == "adds":
            BUTTON.click_button("Add")
            DRPSINGLE.select_from_single_selection_dropdown("Level", cg_details['LEVEL'])
            COMMON_KEY.wait_keyword_success("click_element", self.locator.popup_search)
            self.selib.input_text(self.locator.search_code, cg_details['POSM_VALUE_CODE'])
            COMMON_KEY.wait_keyword_success("click_element", self.locator.popup_checkbox)
            BUTTON.click_button("Assign")
        else:
            COMMON_KEY.wait_keyword_success("click_element", self.locator.posm_search)
            TEXTFIELD.insert_into_field("POSM Value Code", cg_details['POSM_VALUE_CODE'])
            COMMON_KEY.wait_keyword_success("click_element", self.locator.posm_checkbox)
            COMMON_KEY.wait_keyword_success("click_element", self.locator.delete_button)
            BUTTON.click_button("Yes")
