from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE, CALENDAR, COMMON_KEY
import secrets


class PickListAddPage(PageObject):

    PAGE_TITLE = "Customer Transaction / Pick List"
    PAGE_URL = "/customer-transactions-ui/picklist/NEW"
    PICKLIST_DETAILS = "${picklist_details}"

    _locators = {
        "first_invoice": "//*[@role='row' and @row-index='0']//*[contains(@class,'ant-table-selection-column')]//*[contains(@class,'ant-checkbox-wrapper')]"
    }

    @keyword('user ${action} pick list using ${data_type} data')
    def user_creates_or_updates_pick_list(self, action, data_type):

        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        if action == "creates":
            BUTTON.click_button("Add")
            details = BuiltIn.get_variable_value(self.PICKLIST_DETAILS)
            DRPSINGLE.select_from_single_selection_dropdown("Warehouse", details['WAREHOUSE'])
            CALENDAR.select_date_from_calendar("Delivery Date From", details['DATE_FROM'])
            CALENDAR.select_date_from_calendar("Delivery date To", details['DATE_TO'])
            CALENDAR.select_date_from_calendar("Actual Delivery Date", details['ACTUAL_DATE'])
            DRPSINGLE.select_from_single_selection_dropdown("Delivery Route", details['DELIVERY_ROUTE'])
            BUTTON.click_button("Add Invoice")
            COMMON_KEY.wait_keyword_success("click_element", self.locator.first_invoice)
            BUTTON.click_button("Assign")
        BUTTON.click_button("Save")
