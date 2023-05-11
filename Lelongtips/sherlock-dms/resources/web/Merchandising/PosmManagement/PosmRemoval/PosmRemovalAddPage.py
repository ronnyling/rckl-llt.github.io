from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, DRPSINGLE, COMMON_KEY, CALENDAR
from resources.web.Merchandising.PosmManagement.PosmRequest.PosmRequestAddPage import PosmRequestAddPage


class PosmRemovalAddPage(PageObject):

    PAGE_TITLE = "Merchandising / POSM Management / POSM Removal"
    PAGE_URL = "/merchandising/direct-removal"
    REM_DETAILS = "${rem_details}"

    _locators = {
        "rem_qty_field": "(//*[contains(text(),'Removal Quantity')]/following::input)[2]"
    }

    @keyword('user creates posm removal using ${data_type} data')
    def user_creates_posm_removal(self, data_type):
        details = self.builtin.get_variable_value(self.REM_DETAILS)
        BUTTON.click_button("Direct Removal")
        if data_type == "fixed":
            cust = details['CUSTOMER']
            reason = details['REASON']
            warehouse = details['WAREHOUSE']
            route = details['ROUTE']
            posm_code = details['POSM_CODE']
            rem_qty = details['REMOVAL_QTY']

        PosmRequestAddPage().select_customer(cust)
        DRPSINGLE.select_from_single_selection_dropdown("Removal Reason", reason)
        DRPSINGLE.select_from_single_selection_dropdown("Warehouse Code", warehouse)
        DRPSINGLE.select_from_single_selection_dropdown("Route Assigned", route)
        CALENDAR.select_date_from_calendar("Removal Date", "today")
        PosmRequestAddPage().select_product(posm_code)
        COMMON_KEY.wait_keyword_success("input_text", self.locator.rem_qty_field, rem_qty)
        BUTTON.click_button("Save")
