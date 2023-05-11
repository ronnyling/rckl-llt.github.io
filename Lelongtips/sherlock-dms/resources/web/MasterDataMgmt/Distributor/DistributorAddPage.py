from PageObjectLibrary import PageObject
from resources.web.MasterDataMgmt.Distributor import DistributorListPage
from resources.web import BUTTON, TEXTFIELD, TOGGLE, DRPSINGLE, CALENDAR
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from robot.api.deco import keyword

FAKE = Faker()

class DistributorAddPage(PageObject):
    PAGE_TITLE = "Master Data Management / Distributor"
    PAGE_URL = "/distributors?template=p"

    _locators = {
        "OpenAccountDate": "//label[text()='Open Account Date']",
        "LocalityLookup": "//*[@ng-reflect-label='Locality']/following::*[1]//core-button[@ng-reflect-icon='ellipsis']",
        "StateLookup": "//*[@ng-reflect-label='State']/following::*[1]//core-button[@ng-reflect-icon='ellipsis']",
        "CountryLookup": "//*[@ng-reflect-label='Country']/following::*[1]//core-button[@ng-reflect-icon='ellipsis']",
        "SelectElement": "//*[@href='javascript:;']",
        "CalenderIcon": "//div[@class='ant-calendar-input-wrap']"
    }

    @keyword('user saves the distributor by ${datatype} data')
    def user_saves_the_distributor_by_random_data(self, random=None):
        BUTTON.validate_button_is_shown("Add")
        DistributorListPage.DistributorListPage().click_add_distributor_info_button()
        BUTTON.validate_button_is_shown("Save")
        email = f'{FAKE.word()}{FAKE.email()}'
        details = self.builtin.get_variable_value("&{DistDetails}")
        dist_cd = TEXTFIELD.insert_into_field_with_length("Distributor Code", details['DistCode'], 10)
        dist_name = TEXTFIELD.insert_into_field_with_length("Distributor Name", details['DistName'], 10)
        TOGGLE.switch_toggle("Main Distributor Indicator", True)
        self.Select_Open_Account_Date(details['date'])
        DRPSINGLE.selects_from_single_selection_dropdown("Price Group", details['PrcGrp'])
        DRPSINGLE.selects_from_single_selection_dropdown("Other Product Type Price Group", details['OthProdTypePrcGrp'])
        DRPSINGLE.selects_from_single_selection_dropdown("Timezone", details['Timezone'])
        TEXTFIELD.insert_into_field_with_length("Email", email, 50)
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
        BuiltIn().set_test_variable("${dist_cd}", dist_cd)
        BuiltIn().set_test_variable("${dist_name}", dist_name)
        BUTTON.click_button("Save")

    def Select_Open_Account_Date(self, date):
        CALENDAR.selects_date_from_calendar("Open Account Date", date)
