from PageObjectLibrary import PageObject
from resources.web import TEXTFIELD, BUTTON


class HolidaysEditPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Holidays"
    PAGE_URL = "/setting-ui/holiday-calendar/"

    _locators = {
        "HCList":"//div[contains(text(),'Holiday Listing')]",
        "HCType": "//div[@class='ant-select-selection__rendered']",
        "HCDescription": "//input[@id='form-input-1']",
            }

    def edit_description_for_holiday_calender(self,desc):
        editdesc = "HCAL" + desc
        TEXTFIELD.insert_into_field("Description", editdesc)
        edited = TEXTFIELD.retrieves_text_field_text("Description")
        print(edited)
        self.builtin.set_test_variable("${HCname}", edited)

    def user_edits_created_holiday_calendar(self):
        self.selib.wait_until_element_is_visible(self.locator.HCList)
        BUTTON.click_hyperlink(1)
        name=self.builtin.get_variable_value("${HCname}")
        self.edit_description_for_holiday_calender(name)
        BUTTON.click_button("Save")
        self._wait_for_page_refresh()
