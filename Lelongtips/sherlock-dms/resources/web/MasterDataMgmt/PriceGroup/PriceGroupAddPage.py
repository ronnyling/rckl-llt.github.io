from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, TEXTFIELD
import secrets


class PriceGroupAddPage(PageObject):

    PAGE_TITLE = "Master Data Management / Price Group"
    PAGE_URL = "/pricegroup"
    PG_DETAILS = "${pg_details}"

    _locators = {
        "load_image": "//div[@class='loading-text']//img"
    }

    @keyword('user ${action} price group using ${data_type} data')
    def user_creates_or_updates_price_group(self, action, data_type):

        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        if action == "creates":
            BUTTON.click_button("Add")
            pg_code = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            TEXTFIELD.insert_into_field("Price Group Code", pg_code)
            BuiltIn().set_test_variable("${pg_code}", pg_code)
            pg_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            TEXTFIELD.insert_into_field("Price Group Description", pg_desc)
        BUTTON.click_button("Save")
