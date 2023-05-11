from PageObjectLibrary import PageObject
from resources.web.Config.ReferenceData.SalesCalendar import SalesCalendarListPage
from resources.web import COMMON_KEY, TEXTFIELD, DRPSINGLE, BUTTON
import datetime
from robot.api.deco import keyword


class SalesCalendarAddPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Sales Calendar"
    PAGE_URL = "/setting-ui/sales-calendar/NEW"

    _locators = {
        "calendarName": "//label[text()= 'Calendar Name']//following::*[2]//input",
        "startDate": "//label[text()='Start Date']/following::nz-date-picker[1]",
        "endDate": "//label[text()='End Date']/following::nz-date-picker[1]",
        "toggleBtn": "//button[@class='ant-switch']",
        "generateCalendar": "//div[@class='col-md-3']//button[@class='ant-btn ng-star-inserted ant-btn-primary']",
        "calendarField": "//div[@class='ant-calendar-input-wrap']",
        "leftArrow": "//i[@class='anticon anticon-left']//*[local-name()='svg']",
        "calendarInput": "//calendar-input//input"
    }

    def enter_calendar_name_for_sales_calendar(self, calendar_name):
        if calendar_name == 'random':
            self.selib.wait_until_element_is_visible(self.locator.calendarName)
            calendar_name = TEXTFIELD.insert_into_field_with_length("Calendar Name", "random", 10)
        else:
            self.selib.wait_until_element_is_visible(self.locator.calendarName)
            calendar_name = TEXTFIELD.insert_into_field("Calendar Name", calendar_name)
        self.builtin.set_test_variable("${calendar_name}", calendar_name)

    def select_start_date_from_calendar(self, start_dt):
        if start_dt == 'random':
            first_date = (datetime.datetime.now().replace(day=1))
            start_date = first_date.strftime('%b %#d, %Y')
            self.selib.wait_until_element_is_visible(self.locator.startDate)
            self.selib.click_element(self.locator.startDate)
            COMMON_KEY.wait_keyword_success("click_element", self.locator.calendarField)
            self.selib.input_text(self.locator.calendarInput, start_date)
            COMMON_KEY.wait_keyword_success("press_keys", None, "RETURN")
        else:
            self.selib.wait_until_element_is_visible(self.locator.startDate)
            self.selib.click_element(self.locator.startDate)
            COMMON_KEY.wait_keyword_success("click_element", self.locator.calendarField)
            self.selib.input_text(self.locator.calendarInput, start_dt)
            COMMON_KEY.wait_keyword_success("press_keys", None, "RETURN")

    def select_end_date_from_calendar(self, end_dt):
        if end_dt == 'random':
            first_date = (datetime.datetime.now().replace(day=1))
            end_date = str((first_date + datetime.timedelta(days=364)).strftime("%b %#d, %Y"))
            self.selib.wait_until_element_is_visible(self.locator.endDate)
            self.selib.click_element(self.locator.endDate)
            COMMON_KEY.wait_keyword_success("click_element", self.locator.calendarField)
            self.selib.input_text(self.locator.calendarInput, end_date)
            COMMON_KEY.wait_keyword_success("press_keys", None, "RETURN")
        else:
            self.selib.wait_until_element_is_visible(self.locator.endDate)
            self.selib.click_element(self.locator.endDate)
            COMMON_KEY.wait_keyword_success("click_element", self.locator.calendarField)
            self.selib.input_text(self.locator.calendarInput, end_dt)
            COMMON_KEY.wait_keyword_success("press_keys", None, "RETURN")

    def select_auto_mode(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.toggleBtn)

    def select_week_end_day_for_sales_order(self):
        DRPSINGLE.selects_from_single_selection_dropdown("Week End Day", "random")

    def click_generate_calendar(self):
        self.selib.wait_until_element_is_visible(self.locator.generateCalendar)
        BUTTON.click_button("Generate Calendar")
        self.selib.wait_until_element_is_visible(self.locator.leftArrow)

    @keyword("user creates sales calendar with ${data_type} data")
    def user_creates_sales_calendar(self, data_type):
        """ Function to create sales calendar"""
        calendar_details = self.builtin.get_variable_value("${SCDetails}")
        calendar_name = calendar_details["calendarName"]
        start_dt = calendar_details["startDate"]
        end_dt = calendar_details["endDate"]
        SalesCalendarListPage.SalesCalendarListPage().click_add_sales_calendar_button()
        self.enter_calendar_name_for_sales_calendar(calendar_name)
        self.select_start_date_from_calendar(start_dt)
        self.select_auto_mode()
        self.select_end_date_from_calendar(end_dt)
        self.select_week_end_day_for_sales_order()
        self.click_generate_calendar()
        BUTTON.click_button("Save")
