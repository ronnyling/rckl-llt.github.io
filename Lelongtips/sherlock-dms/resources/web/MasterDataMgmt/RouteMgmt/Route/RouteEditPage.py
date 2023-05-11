from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD


class RouteEditPage(PageObject):
    """ Functions in Route add page """
    PAGE_TITLE = "Master Data Management / Route Management / Route"
    PAGE_URL = "/route?template=p"

    _locators = {
        "np_warehouse": "//*[text()='Non Prime Warehouse']",
        "load_image": "//div[@class='loading-text']//img"
    }

    @keyword('user updates route with ${data_type} data')
    def user_updates_route(self, data_type):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        TEXTFIELD.insert_into_field_with_length("Route Name", "random", 6)
        BUTTON.click_button("Save")

    @keyword('user validated fields are disabled and cant be edited')
    def validate_field_disabled(self):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        TEXTFIELD.verifies_text_field_is_disabled("Route Code")
        TEXTFIELD.verifies_text_field_is_disabled("Operation Type")
        TEXTFIELD.verifies_text_field_is_disabled("Company")
        TEXTFIELD.verifies_text_field_is_disabled("Main Warehouse")
        TEXTFIELD.verifies_text_field_is_disabled("LOB")

