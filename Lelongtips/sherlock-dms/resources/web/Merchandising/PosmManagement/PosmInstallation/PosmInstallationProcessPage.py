from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, DRPSINGLE
from resources.web.Merchandising.PosmManagement.PosmInstallation.PosmInstallationListPage import PosmInstallationListPage


class PosmInstallationProcessPage(PageObject):

    PAGE_TITLE = "Merchandising / POSM Management / POSM Installation"
    PAGE_URL = "/merchandising/posm-direct-installation"
    INS_DETAILS = "${ins_details}"

    @keyword('user ${action} posm installation')
    def user_process_posm_installation(self, action):
        details = self.builtin.get_variable_value(self.INS_DETAILS)
        req_no = BuiltIn().get_variable_value("${request_no}")
        PosmInstallationListPage().user_selects_posm_installation_by_request_no(req_no)
        if action == "processes":
            BUTTON.click_button("Process Installation")
            DRPSINGLE.select_from_single_selection_dropdown("Warehouse", details['WAREHOUSE'])
            DRPSINGLE.select_from_single_selection_dropdown("Route Assigned", details['ROUTE'])
            BUTTON.click_button("Apply")
            BUTTON.click_button("Save")
        elif action == "rejects":
            BUTTON.click_button("Reject")
            DRPSINGLE.select_from_single_selection_dropdown("Reject Reason", details['REASON'])
            BUTTON.click_button("Confirm")

