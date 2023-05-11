from PageObjectLibrary import PageObject
from resources.web import LABEL, BUTTON, DRPSINGLE
from robot.api.deco import keyword
from resources.web.Config.SFADashboardSetup import SFADashboardSetupAddPage


class SFADashboardSetupEditPage(PageObject):
    PAGE_TITLE = "Configuration / SFA Dashboard Setup"
    PAGE_URL = "/performance/advance-kpi"
    DASHBOARD_DETAILS = "${dashboard_details}"

    _locators = \
        {
        }

    @keyword('user is able to navigate to EDIT | SFA Dashboard Setup')
    def user_able_to_navigate_edit_page(self):
        LABEL.validate_label_is_visible("EDIT | SFA Dashboard Setup")
        LABEL.validate_column_header_label_is_visible("KPI Code")
        LABEL.validate_column_header_label_is_visible("KPI Description")
        LABEL.validate_column_header_label_is_visible("Card")
        LABEL.validate_column_header_label_is_visible("Graph")
        LABEL.validate_column_header_label_is_visible("Sequence")
        BUTTON.validate_button_is_shown("Apply")
        BUTTON.validate_button_is_shown("Save")
        BUTTON.click_button("Cancel")

    @keyword('user edits dashboard data')
    def user_edits_dashboard_data(self):
        setup = self.builtin.get_variable_value(self.DASHBOARD_DETAILS)
        LABEL.validate_label_is_visible("EDIT | SFA Dashboard Setup")
        DRPSINGLE.selects_from_single_selection_dropdown("Card", setup['new_card'])
        BUTTON.click_button("Apply")
        SFADashboardSetupAddPage.SFADashboardSetupAddPage.user_selects_KPI_card(self)
        BUTTON.click_button("Save")

    def user_updates_delivery_dashboard(self):
        setup = self.builtin.get_variable_value(self.DASHBOARD_DETAILS)
        DRPSINGLE.selects_from_single_selection_dropdown("Profile", setup['profile'])
        DRPSINGLE.selects_from_single_selection_dropdown("Dashboard", setup['dashboard'])
        DRPSINGLE.selects_from_single_selection_dropdown("Card", setup['card'])
        DRPSINGLE.selects_from_single_selection_dropdown("Graph", setup['graph'])
        BUTTON.click_button("Save")






