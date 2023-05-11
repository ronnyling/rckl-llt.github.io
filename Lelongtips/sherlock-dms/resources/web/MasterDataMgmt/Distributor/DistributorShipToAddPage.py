from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, TEXTFIELD
import secrets


class DistributorShipToAddPage(PageObject):

    PAGE_TITLE = "Master Data Management / Distributor"
    PAGE_URL = "/distributors?template=p"
    SHIPTO_DETAILS = "${shipto_details}"

    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "LocalityLookup": "//*[@ng-reflect-label='Locality']/following::*[1]//core-button[@ng-reflect-icon='ellipsis']",
        "StateLookup": "//*[@ng-reflect-label='State']/following::*[1]//core-button[@ng-reflect-icon='ellipsis']",
        "CountryLookup": "//*[@ng-reflect-label='Country']/following::*[1]//core-button[@ng-reflect-icon='ellipsis']",
        "SelectElement": "//*[@href='javascript:;']"
    }

    @keyword('user ${action} ship to using ${data_type} data')
    def user_creates_or_updates_ship_to(self, action, data_type):

        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        if action == "creates":
            BUTTON.click_button("Add")
            shipto_code = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            TEXTFIELD.insert_into_field("Ship To Code", shipto_code)
            BuiltIn().set_test_variable("${shipto_code}", shipto_code)

        shipto_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        TEXTFIELD.insert_into_field("Ship To Description", shipto_desc)
        TEXTFIELD.insert_into_field_with_length("Address 1", "random", 10)
        TEXTFIELD.insert_into_field_with_length("Address 2", "random", 10)
        TEXTFIELD.insert_into_field_with_length("Address 3", "random", 10)
        TEXTFIELD.insert_into_field_with_length("Postal Code", "number", 6)
        self.selib.click_element(self.locator.LocalityLookup)
        self.selib.click_element(self.locator.SelectElement)
        self.selib.click_element(self.locator.StateLookup)
        self.selib.click_element(self.locator.SelectElement)
        self.selib.click_element(self.locator.CountryLookup)
        self.selib.click_element(self.locator.SelectElement)
        BUTTON.click_button("Save")
