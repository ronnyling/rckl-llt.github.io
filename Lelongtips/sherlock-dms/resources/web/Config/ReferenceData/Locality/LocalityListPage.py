from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, PAGINATION
from robot.libraries.BuiltIn import BuiltIn


class LocalityListPage (PageObject):
    """ Functions related to listing page of Locality """
    PAGE_TITLE = "Configuration / Reference Data / State"
    PAGE_URL = "/objects/address-state"
    UPDATED_CITY_CD = "${updated_city_cd}"

    @keyword('user selects locality to ${action}')
    def user_selects_locality_to(self, action):
        """ Function to select locality in listing to edit/delete """
        updated = BuiltIn().get_variable_value(self.UPDATED_CITY_CD)
        if updated:
            city_cd = BuiltIn().get_variable_value(self.UPDATED_CITY_CD)
            city_name = BuiltIn().get_variable_value("${updated_city_name}")
        else:
            city_cd = BuiltIn().get_variable_value("${city_cd}")
            city_name = BuiltIn().get_variable_value("${city_name}")
        col_list = ["CITY_CD", "CITY_NAME"]
        data_list = [city_cd, city_name]
        if action == 'delete':
            action = "check"
        PAGINATION.validate_the_data_is_in_the_table_and_select_to\
            ("present", "Locality", action, col_list, data_list)
        if action == 'check':
            BUTTON.click_icon("delete")

    @keyword('user clicks cancel')
    def user_clicks_cancel(self):
        self.builtin.set_test_variable(self.UPDATED_CITY_CD, self.builtin.set_test_variable("${city_cd}"))
        self.builtin.set_test_variable("${updated_city_name}", self.builtin.set_test_variable("${city_name}"))
        BUTTON.click_button("Cancel")
