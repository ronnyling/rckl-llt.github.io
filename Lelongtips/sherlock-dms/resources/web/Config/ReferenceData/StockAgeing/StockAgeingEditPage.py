from PageObjectLibrary import PageObject
from resources.web import BUTTON, TEXTFIELD, COMPOUND, LABEL
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

class StockAgeingEditPage(PageObject):

    PAGE_TITLE = "Configuration / Reference Data / Stock Ageing"
    PAGE_URL = "/setting-ui/aging-period"

    _locators = {
    }

    @keyword('user edits and saves the aging period')
    def user_edits_and_saves_the_aging_period(self):
        """ Function to edit aging period """
        period_code = BuiltIn().get_variable_value("${period_code}")
        LABEL.validate_label_is_visible("Add")
        COMPOUND.search_and_click_first_item("Period Code", period_code)
        LABEL.validate_label_is_visible("EDIT | Stock Ageing")
        updated_period_desc = TEXTFIELD.insert_into_field_with_length("Period Description", "random", 50)
        BuiltIn().set_test_variable("${updated_period_desc}", updated_period_desc)
        self.user_clicks_save()

    def user_clicks_save(self):
        """ Function to save button """
        BUTTON.click_button("Save")
        self._wait_for_page_refresh()
