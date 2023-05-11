from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, PAGINATION
from robot.libraries.BuiltIn import BuiltIn


class CountryListPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Country"
    PAGE_URL = "/objects/address-country"
    UPDATED_COUNTRY_CD = "${updated_country_cd}"
    _locators = {
    }

    @keyword('user selects country to ${action}')
    def user_selects_country_to(self, action):
        updated = BuiltIn().get_variable_value(self.UPDATED_COUNTRY_CD)
        if updated:
            country_code = BuiltIn().get_variable_value(self.UPDATED_COUNTRY_CD)
            country_name = BuiltIn().get_variable_value("${updated_country_name}")
        else:
            country_code = BuiltIn().get_variable_value("${country_cd}")
            country_name = BuiltIn().get_variable_value("${country_name}")
        col_list = ["COUNTRY_CD", "COUNTRY_NAME"]
        data_list = [country_code, country_name]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Country", action, col_list, data_list)


    def user_clicks_cancel(self):
        self.builtin.set_test_variable("${updated_country_cd}", self.builtin.set_test_variable("${country_cd}"))
        self.builtin.set_test_variable("${updated_country_name}", self.builtin.set_test_variable("${country_name}"))
        BUTTON.click_button("Cancel")

    def click_add_country_button(self):
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()
