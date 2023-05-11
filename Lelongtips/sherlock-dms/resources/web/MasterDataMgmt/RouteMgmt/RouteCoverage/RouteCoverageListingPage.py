from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, PAGINATION, TEXTFIELD
from robot.libraries.BuiltIn import BuiltIn


class RouteCoverageListingPage(PageObject):


    @keyword('user selects route coverage to ${action}')
    def user_selects_route_coverage_to(self, action):
        """ Function to select route coverage in listing to edit/delete """
        start_date = BuiltIn().get_variable_value("${start_date}")
        end_date = BuiltIn().get_variable_value("${end_date}")
        col_list = ["FROM_DATE", "TO_DATE"]
        data_list = [start_date, end_date]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Route Coverage", action, col_list, data_list)
        if action == 'delete':
            BUTTON.click_button("Yes")