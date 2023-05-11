from PageObjectLibrary import PageObject
from resources.web import COMPOUND, LABEL
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class StockAgeingListingPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Stock Ageing"
    PAGE_URL = "/setting-ui/aging-period"

    _locators = {
    }

    @keyword('user deletes the created aging period')
    def user_deletes_the_created_aging_period(self):
        """ Function to delete the created aging period """
        period_code = BuiltIn().get_variable_value("${period_code}")
        LABEL.validate_label_is_visible("Add")
        COMPOUND.search_and_click_inline_delete("Period Code", period_code)