from PageObjectLibrary import PageObject
from resources.web.Config.ReferenceData.Holidays import HolidaysListPage
from resources.web import DRPSINGLE, TEXTFIELD, CALENDAR, BUTTON
import secrets


class HolidaysAddPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data/ Holidays"
    PAGE_URL = "/setting-ui/holiday-calendar/NEW"

    _locators = {
        "HCList":"//div[contains(text(),'Holiday Listing')]",
        "HCType": "//div[@class='ant-select-selection__rendered']",
        "HCDescription": "//input[@id='form-input-1']",
            }

    def select_type_for_holiday_calender(self, hctype):
        DRPSINGLE.selects_from_single_selection_dropdown("Type of Holiday", hctype)

    def add_description_for_holiday_calender(self,desc):
        if desc == 'random':
            desc = "HCAL" + str(secrets.choice(range(1000,9999)))
            TEXTFIELD.insert_into_field("Description",desc)
        else:
            TEXTFIELD.insert_into_field("Description", desc)
        self.builtin.set_test_variable("${HCname}", desc)

    def select_date_for_holiday_calender(self, date):
        CALENDAR.selects_date_from_calendar("Date", date)

    def user_creates_holiday_calendar(self):
        #LABEL.validate_label_is_visible("Holiday Listing")
        self.selib.wait_until_element_is_visible(self.locator.HCList)
        HolidaysListPage.HolidaysListPage().click_add_holiday_calender_button()
        details = self.builtin.get_variable_value("&{HCDetails}")
        self.select_type_for_holiday_calender(details['type'])
        self.add_description_for_holiday_calender(details['description'])
        self.select_date_for_holiday_calender(details['date'])
        BUTTON.click_button("Save")

    def user_navigates_back_to_listing_page(self):
         BUTTON.click_button("Cancel")
         self._wait_for_page_refresh()
