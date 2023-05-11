from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, TEXTFIELD
from resources.web.Config.ReferenceData.Country import CountryListPage


class CountryAddPage(PageObject):
    """ Functions related to Country Create """
    PAGE_TITLE = "Configuration / Reference Data / Country"
    PAGE_URL = "/objects/address-country"

    _locators = {
    }
    @keyword('user creates country with ${data_type} data')
    def user_creates_country(self, data_type):
        details = self.builtin.get_variable_value("${country_details}")
        CountryListPage.CountryListPage().click_add_country_button()
        country_cd = self.user_inserts_country_cd(data_type, details)
        country_name = self.user_inserts_country_name(data_type, details)
        self.builtin.set_test_variable("${country_cd}", country_cd)
        self.builtin.set_test_variable("${country_name}", country_name)
        BUTTON.click_button("Save")

    def user_inserts_country_cd(self, data_type, details):
        if data_type == "fixed":
            country_cd = TEXTFIELD.insert_into_field("Country Code", details['country_cd'])
        elif data_type == "random":
            country_cd = TEXTFIELD.insert_into_field_with_length("Country Code", "letter", 8)
        return country_cd

    def user_inserts_country_name(self, data_type, details):
        if data_type == "fixed":
            country_name = TEXTFIELD.insert_into_field("Country Name", details['country_name'])
        elif data_type == "random":
            country_name = TEXTFIELD.insert_into_field_with_length("Country Name", "random", 8)
        return country_name







