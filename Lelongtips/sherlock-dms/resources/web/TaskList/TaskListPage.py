from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, COMMON_KEY


class TaskListPage(PageObject):

    PAGE_TITLE = "Dashboard / Task List"
    PAGE_URL = "/workflow/task"
    _locators = {
        "claim_icon": "//*[contains(text(),'Task Creation')]/following::core-button[@ng-reflect-icon='lock'][1]",
        "process_icon": "//*[contains(text(),'Task Creation')]/following::core-button[@ng-reflect-icon='play-circle'][1]",
        "release_icon": "//*[contains(text(),'Task Creation')]/following::core-button[@ng-reflect-icon='unlock'][1]"
    }

    @keyword('user validates buttons for workflow task listing page')
    def user_validates_buttons(self):
        BUTTON.validate_icon_is_shown("search")
        BUTTON.validate_icon_is_shown("filter")

    @keyword('user claims workflow task')
    def user_claim_task(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.claim_icon)

    @keyword('user processes workflow task')
    def user_process_task(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.process_icon)

    @keyword('user cancels workflow task process')
    def user_cancels_task_process(self):
        BUTTON.click_button("Cancel")

    @keyword('user releases workflow task')
    def user_release_task(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.release_icon)
