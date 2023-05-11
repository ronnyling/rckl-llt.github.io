from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn


class Logout(PageObject):

    _locators = {
        "logout_drp": "//i[contains(@ng-reflect-nz-type, 'user')]",
        "logout_btn": "//*[contains(text(),'Logout')]"
    }

    def user_logouts_from_system(self):
        self.selib.mouse_over(self.locator.logout_drp)
        BuiltIn().wait_until_keyword_succeeds("0.5 min", "3 sec", "click_element", self.locator.logout_btn)

    def user_logouts_and_closes_browser(self):
        self.user_logouts_from_system()
        self.selib.close_browser()
