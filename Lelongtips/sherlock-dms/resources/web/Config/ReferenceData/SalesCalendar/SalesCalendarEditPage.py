from PageObjectLibrary import PageObject
from resources.web.Config.ReferenceData.SalesCalendar import SalesCalendarListPage
from resources.web import BUTTON, LABEL
from robot.api.deco import keyword


class SalesCalendarEditPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Sales Calendar"
    PAGE_URL = "/setting-ui/sales-calendar/NEW"

    _locators = {
        "dropdown": "//*[@class='cdk-overlay-pane']//following-sibling::li[contains(text(),'Q1')]",
        "quarterDropDown": "(//*[text()='Quarter']//following::*//nz-select)[7]",
        "quarterInput": "(//*[text()='Quarter']//following::*//nz-select//input)[7]"
    }

    @keyword('user updates created sales calendar with ${data_type} data')
    def user_updates_sales_calendar(self, data_type):
        """ Function to edit sales calendar """
        SalesCalendarListPage.SalesCalendarListPage().inline_search_created_calendar()
        SalesCalendarListPage.SalesCalendarListPage().user_clicks_created_sales_calendar()
        LABEL.validate_label_is_visible("EDIT")
        self.update_quarter_dropdown_value()
        BUTTON.click_button("Save")

    def update_quarter_dropdown_value(self):
        """ Function to update quarter drop down value for one particular row """
        quarter_details = self.builtin.get_variable_value("${QuarterDetails}")
        quarter_name = quarter_details["quarterName"]
        self.builtin.wait_until_keyword_succeeds("1 min", "3 sec",
                                                 "click_element",
                                                 self.locator.quarterDropDown)
        self.selib.input_text(self.locator.quarterInput, quarter_name)
        self.builtin.wait_until_keyword_succeeds("0.5 min", "3 sec", "click_element",
                                                 self.locator.dropdown)
