from PageObjectLibrary import PageObject
from resources.web import BUTTON
from robot.api.deco import keyword


class CustomerApproval(PageObject):
    PAGE_TITLE = "Master Data Management / Customer"
    PAGE_URL = "/customer?template=p"

    timeout = "0.2 min"
    wait = "3 sec"

    @keyword("user ${action} created customer")
    def user_approve_customer(self, action):
        BUTTON.click_button(action)
        BUTTON.click_button("Yes")
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")
