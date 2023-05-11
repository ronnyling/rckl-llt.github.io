from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, DRPSINGLE, CALENDAR
from resources.web.Merchandising.PosmManagement.PosmRemoval.PosmRemovalListPage import PosmRemovalListPage


class PosmRemovalProcessPage(PageObject):

    PAGE_TITLE = "Merchandising / POSM Management / POSM Removal"
    PAGE_URL = "/merchandising/direct-removal"
    REM_DETAILS = "${rem_details}"

    @keyword('user ${action} posm removal')
    def user_process_posm_removal(self, action):
        details = self.builtin.get_variable_value(self.REM_DETAILS)
        req_no = BuiltIn().get_variable_value("${request_no}")
        PosmRemovalListPage().user_selects_posm_removal_by_request_no(req_no)
        if action == "processes":
            BUTTON.click_button("Process Removal")
            DRPSINGLE.select_from_single_selection_dropdown("Route Assigned", details['ROUTE'])
            CALENDAR.select_date_from_calendar("Removal Date", "today")
            BUTTON.click_button("Apply")
            BUTTON.click_button("Save")
        elif action == "rejects":
            BUTTON.click_button("Reject")
            DRPSINGLE.select_from_single_selection_dropdown("Reject Reason", details['REASON'])
            BUTTON.click_button("Confirm")

