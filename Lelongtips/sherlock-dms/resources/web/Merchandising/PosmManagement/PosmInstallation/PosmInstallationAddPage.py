from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, DRPSINGLE, COMMON_KEY, CALENDAR
from resources.web.Merchandising.PosmManagement.PosmRequest.PosmRequestAddPage import PosmRequestAddPage


class PosmInstallationAddPage(PageObject):

    PAGE_TITLE = "Merchandising / POSM Management / POSM Installation"
    PAGE_URL = "/merchandising/posm-direct-installation"
    INS_DETAILS = "${ins_details}"

    @keyword('user creates posm installation using ${data_type} data')
    def user_creates_posm_installation(self, data_type):
        details = self.builtin.get_variable_value(self.INS_DETAILS)
        BUTTON.click_button("Direct Installation")
        if data_type == "fixed":
            cust = details['CUSTOMER']
            reason = details['REASON']
            warehouse = details['WAREHOUSE']
            route = details['ROUTE']
            posm_code = details['POSM_CODE']
            req_qty = details['REQUEST_QTY']

        PosmRequestAddPage().select_customer(cust)
        DRPSINGLE.select_from_single_selection_dropdown("Install Reason", reason)
        DRPSINGLE.select_from_single_selection_dropdown("Warehouse Code", warehouse)
        DRPSINGLE.select_from_single_selection_dropdown("Route Assigned", route)
        CALENDAR.select_date_from_calendar("Installation Date", "today")
        PosmRequestAddPage().select_product(posm_code)
        COMMON_KEY.wait_keyword_success("input_text", PosmRequestAddPage().locator.req_qty_field, req_qty)
        BUTTON.click_button("Save")
