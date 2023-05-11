from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, PAGINATION
from resources.web.Common import AlertCheck


class HolidaysListPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Holidays"
    PAGE_URL = "/setting-ui/holiday-calendar"

    _locators = {
        "Search":"//core-button[2]//span[1]//button[1]",
        "CalenderName":"(//*[contains(text(),'Description')]/following::input)[3]",
        "SelectAll":"//span[@class='ant-table-column-title']//input[@class='ant-checkbox-input ng-untouched ng-pristine ng-valid']",
        "DeleteAll":"//core-dynamic-actions[@class='selection-actions']//button[@class='ant-btn ng-star-inserted ant-btn-icon-only']",
        "Delete": "//tr[1]//td[6]//div[1]//span[1]//core-button[1]//span[1]//i[1]",
        "PopUpYes": "//*[contains(text(),'Yes')]/parent::button"
    }

    def click_add_holiday_calender_button(self):
        self._wait_for_page_refresh()
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    def user_deletes_created_holiday_calendar(self):
        BUTTON.click_inline_delete_icon(1)
        AlertCheck.AlertCheck().successfully_with_message(self,"Holiday Calender deleted","Record deleted")

    def user_deletes_holiday_calender_by_name(self):
        calendar_name = BuiltIn().get_variable_value("${HCname}")
        self.inline_search_created_calendar(calendar_name)
        delete_msg = self.builtin.wait_until_keyword_succeeds \
            (".5 min", "5 sec", "get_text", "//div[contains(text(),'Are you sure you want to delete?')]")
        checking = "Are you sure you want to delete" in delete_msg
        if checking:
            self.builtin.wait_until_keyword_succeeds \
                ("0.5 min", "2 sec", "click_element", self.locator.PopUpYes)

    def inline_search_created_calendar(self, name):
        col_list= ["Description"]
        data_list= [name]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present","Holiday Calendar","delete",col_list,data_list)
