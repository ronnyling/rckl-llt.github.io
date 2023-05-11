from PageObjectLibrary import PageObject
from resources.web import BUTTON
from robot.api.deco import keyword

class StepsOfCallDeletePage(PageObject):

    PAGE_TITLE = "Configuration / Steps of Call"
    PAGE_URL = "/setting-ui/steps-of-call"

    _locators = {
        "SOCList": "//div[contains(text(),'Steps of Call Listing')]",
        "AddBtn": "//core-button[@ng-reflect-label='Add']"
    }

    @keyword('user deletes the created soc')
    def user_deletes_the_created_soc(self):
        self.selib.wait_until_element_is_visible(self.locator.SOCList)
        self.selib.wait_until_element_is_visible(self.locator.AddBtn)
        BUTTON.click_icon("delete")

