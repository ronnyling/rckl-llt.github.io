from PageObjectLibrary import PageObject
from resources.web import BUTTON, TEXTFIELD
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class StockAgeingAddPage(PageObject):

    PAGE_TITLE = "Configuration / Reference Data / Stock Ageing"
    PAGE_URL = "/setting-ui/aging-period"

    _locators = {
    }

    @keyword('user creates and saves the aging period with ${status} data')
    def user_creates_and_saves_the_aging_period_with_data(self, status):
        """ Function to create page aging period """
        self.user_clicks_add_button()
        period_code = None
        period_desc = None
        if status == "fixed":
            details = BuiltIn().get_variable_value("&{aging_period_details}")
            period_code = TEXTFIELD.insert_into_field("Period Code", details['PERIOD_CD'])
            period_desc = TEXTFIELD.insert_into_field("Period Description", details['PERIOD_DESC'])
        elif status == "random":
            period_code = TEXTFIELD.insert_into_field_with_length("Period Code", "random", 20)
            period_desc = TEXTFIELD.insert_into_field_with_length("Period Description", "random", 50)
        BuiltIn().set_test_variable("${period_code}", period_code)
        BuiltIn().set_test_variable("${period_desc}", period_desc)
        self.user_clicks_save()

    def user_clicks_save(self):
        """ Function to save button """
        BUTTON.click_button("Save")
        self._wait_for_page_refresh()

    def user_clicks_add_button(self):
        """ Function to click Add Button """
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()