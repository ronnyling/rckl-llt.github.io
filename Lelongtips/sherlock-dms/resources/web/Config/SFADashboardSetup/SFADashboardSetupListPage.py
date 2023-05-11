from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, DRPSINGLE, PAGINATION

class SFADashboardSetupListPage(PageObject):

    PAGE_TITLE = "Configuration / SFA Dashboard Setup"
    PAGE_URL = "/performance/advance-kpi"
    DASHBOARD_DETAILS = "${dashboard_details}"

    _locators = {
   }

    @keyword('user searches created dashboard in listing page')
    def user_search_created_dashboard(self):
        BUTTON.click_icon("search")
        DRPSINGLE.select_from_single_selection_dropdown("Profile", "Delivery Rep")

    @keyword('user filters created dashboard in listing page')
    def user_filters_created_dashboard(self):
        setup = BuiltIn().get_variable_value(self.DASHBOARD_DETAILS)
        BUTTON.click_icon("filter")
        DRPSINGLE.selects_from_single_selection_dropdown("Profile", setup['profile'])
        BUTTON.click_button("Apply")

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No Delivery Dashboard in listing"

    @keyword('user perform ${action} on dashboard')
    def user_perform_on_dashboard(self, action):
        setup = BuiltIn().get_variable_value(self.DASHBOARD_DETAILS)
        setup_profile = setup['profile']
        setup_dashboard = setup['dashboard']
        col_list = ["PROFILE", "DASHBOARD"]
        data_list = [setup_profile, setup_dashboard]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to \
        ("present", "Dashboard", action, col_list, data_list)







