from PageObjectLibrary import PageObject
from resources.web import BUTTON


class StepsOfCallListingPage(PageObject):
    PAGE_TITLE = "Configuration / Steps of Call"
    PAGE_URL = "/setting-ui/steps-of-call"

    _locators = {
    }

    def user_clicks_add_button(self):
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()