from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, DRPSINGLE

class StoreSpaceListPage(PageObject):
    PAGE_TITLE = "Merchandising / Merchandising Setup / Store Space"
    PAGE_URL = "/merchandising/merc-store-space?template=p"
    STORE_SPACE_DETAILS = "${store_space_details}"

    _locators = {
        "edit_icon": "//core-button[@ng-reflect-icon='edit']",
        "add_icon": "//core-button[@ng-reflect-icon='plus-circle']",
        "delete_icon" :"//div[2]/div[3]/core-button/span/button",
        "overlay": "//ngx-spinner/div",
        "space_code_drp": "//nz-form-control/div/span/nz-select/div/div/div[1]",
        "space_desc_drp": ""
    }


    @keyword('user validates all managing buttons absent and hidden')
    def user_validates_all_managing_buttons_absent(self):
        BUTTON.validate_button_is_hidden("Add")
        self.selib.page_should_not_contain_element(self.locator.edit_icon)
        self.selib.page_should_not_contain_element(self.locator.add_icon)

    @keyword('user selects store space to ${action}')
    def user_selects_store_space_to(self,action):
        space_code = BuiltIn().get_variable_value("${space_code}")

        self.selib.click_element(self.locator.edit_icon)
        if action == "delete":
            DRPSINGLE.selects_from_single_selection_dropdown("Space Code", space_code)
            self.selib.click_element(self.locator.delete_icon)







